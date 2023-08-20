from django.db import models

from django.contrib.auth.hashers import make_password, check_password
import uuid
from datetime import datetime, timedelta


class User(models.Model):
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.user

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def verify_password(self, password):
        return check_password(password, self.password)

    def full_clean(self, *args, **kwargs):
        try:
            user = User.objects.get(user=self.user)

            if self.password != user.password:
                self.set_password(self.password)

        except:
            self.set_password(self.password)

        super().full_clean(*args, **kwargs)

    def create_token(self):
        token = Token(user=self)
        token.save()

        return token

    def asset_token(self):
        for i in self.tokens.all():
            if i.is_asset():
                i.update_asset()
                return i

        return None

    def get_token(self):
        active = self.asset_token()
        return active if active else self.create_token()


class Token(models.Model):
    key = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tokens")
    asset = models.DateTimeField(default=datetime.now() + timedelta(days=1))

    def __str__(self):
        return str(self.key)

    def is_asset(self):
        return self.asset >= datetime.now()

    def update_asset(self):
        self.asset = datetime.now() + timedelta(days=1)


class Localidad(models.Model):
    localidad = models.CharField(max_length=40)


class Domicilio(models.Model):
    localidad = models.ForeignKey(Localidad, on_delete=models.RESTRICT)
    calle = models.CharField(max_length=40)
    numero = models.PositiveSmallIntegerField()
    torre = models.PositiveBigIntegerField()
    departamento = models.CharField(max_length=10)
    piso = models.PositiveSmallIntegerField()


class Cliente(User):
    dni = models.PositiveIntegerField()
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField()
    telefono = models.PositiveBigIntegerField()
    nacimiento = models.DateField()
    domicilio = models.ForeignKey(Domicilio, on_delete=models.RESTRICT)


class Cadete(models.Model):
    nombre = models.CharField(max_length=40)
