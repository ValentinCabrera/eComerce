import { addProducto } from "../Utils/Fetchs";

function ItemPedido(props) {
    function updateCantidad(cantidad) {
        addProducto(props.pedido.id, props.item.producto.id, cantidad)
            .then(pedido => props.setPedido(pedido));
    }



    return (
        <div className="itemPedido">
            <p>x{props.item.cantidad}</p>
            <p>{props.item.producto.nombre}</p>
            <button onClick={() => updateCantidad(1)}>+</button>
            <button onClick={() => updateCantidad(-1)}>-</button>

        </div>
    )
}

export default ItemPedido;