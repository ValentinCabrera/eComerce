import { useState } from "react";
import ProductoModal from "./ProductoModal"; // Asegúrate de importar el componente Modal

function Producto(props) {
    const [modal, setModal] = useState(false);

    return (
        <div className="producto">
            <button onClick={() => setModal(true)}>
                <img className="image" src={"http://localhost:8000" + props.producto.imagen} alt={props.producto.nombre} />
                <p>{props.producto.nombre}</p>
                <p>{props.producto.precio}</p>
            </button>

            {modal && (
                <ProductoModal pedido={props.pedido} setPedido={props.setPedido} producto={props.producto} onClose={() => setModal(false)} />
            )}
        </div>
    )
}

export default Producto;
