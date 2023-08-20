import ItemPedido from "./ItemPedido";

function Pedido(props) {
    return (
        <div className="pedido">
            {props.pedido.id}
            {props.pedido.items.map(item => (
                <ItemPedido item={item} key={item.id} pedido={props.pedido} setPedido={props.setPedido} />
            ))}
            <p>{props.pedido.total}</p>
            <button>finalizar pedido</button>
        </div>
    );
}

export default Pedido;