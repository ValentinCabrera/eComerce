import React, { useState } from "react";
import { addProducto } from "../Utils/Fetchs";
import Ingrediente from "./Ingrediente";


function ProductoModal(props) {
    const [subTotal, setSubTotal] = useState(props.producto.precio)
    const [ingredientes, setIngredientes] = useState({})

    function updateCarrito() {
        addProducto(props.pedido.id, props.producto.id, 1, ingredientes)
            .then(pedido => {
                props.setPedido(pedido);
                props.onClose();
            });
    }

    function updateSubTotal() {
    }

    function updateIngredientes(ingrediente) {
        const nuevosIngredientes = { ...ingredientes };

        if (ingrediente.cantidad === 1) {
            delete nuevosIngredientes[ingrediente.nombre];
        } else {
            nuevosIngredientes[ingrediente.ingrediente] = ingrediente.cantidad;
        }

        setIngredientes(nuevosIngredientes);
        console.log(nuevosIngredientes);
        updateSubTotal();
    }


    return (
        <div className="modal-overlay">
            <div className="modal">
                <div className="modal-content">
                    <img className="image" src={"http://localhost:8000" + props.producto.imagen} alt={props.producto.nombre} />
                    <h2>{props.producto.nombre}</h2>
                    <div className="row sep">
                        <p>{props.producto.descripcion}</p>
                        <p>${props.producto.precio}</p>
                    </div>
                    {props.producto.ingredientes.length > 0 &&
                        <div>
                            <h4>Ingredientes</h4>
                            <div>{props.producto.ingredientes.map(ingrediente => (
                                <Ingrediente ingrediente={ingrediente} key={ingrediente.id} updateIngredientes={updateIngredientes} />))}
                            </div>
                        </div>
                    }
                    <div className="row">
                        <button onClick={props.onClose}>Volver</button>
                        <button className="w100" onClick={updateCarrito}>
                            <div className="row sep">
                                <p>Agregar al carrito</p>
                                <p>${subTotal}</p>
                            </div>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default ProductoModal;
