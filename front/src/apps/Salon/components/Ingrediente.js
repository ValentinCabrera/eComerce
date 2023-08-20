import { useState } from "react";

function Ingrediente(props) {
    const [cantidad, setCantidad] = useState(1);

    function updateCantidad(value) {
        if (cantidad + value >= 0) {
            setCantidad(cantidad + value);
            props.updateIngredientes({ "ingrediente": props.ingrediente, "cantidad": cantidad + value });
        }
    }

    return (
        <div className="row sep">
            <p>{props.ingrediente.nombre}</p>
            <p>${props.ingrediente.precio}</p>
            <button onClick={() => { updateCantidad(-1) }}>-</button>
            <p>x{cantidad}</p>
            <button onClick={() => { updateCantidad(1) }}>+</button>
        </div>
    )
}
export default Ingrediente;