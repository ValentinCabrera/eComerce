import { useEffect, useState } from "react";
import { getProductos } from "../Utils/Fetchs";
import Producto from "./Producto";

function Productos(props) {
    const [data, setData] = useState();

    useEffect(() => {
        getProductos(props.categoria.id)
            .then(productos => setData(productos));
    }, []);

    return (
        <div className="productos">
            {data && data.map(producto => (
                <Producto producto={producto} pedido={props.pedido} key={producto.id} setPedido={props.setPedido} />
            ))}
        </div>
    )
}

export default Productos;