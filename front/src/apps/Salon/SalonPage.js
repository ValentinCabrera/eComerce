import { useEffect, useState } from "react";
import Categorias from "./components/Categorias";
import Productos from "./components/Productos";
import Pedido from "./components/Pedido";

function SalonPage(props) {
    const [categoria, setCategoria] = useState(false);

    function productoFrame(categoria) {
        setCategoria(categoria);
    };

    function categoriaFrame() {
        setCategoria(false);
    }

    return (
        <div className="salonPage">
            {categoria ?
                < div >
                    <button onClick={categoriaFrame}>Volver</button>
                    <p>{categoria.nombre}</p>
                    <Productos navCategoria={categoriaFrame} categoria={categoria} pedido={props.pedido} setPedido={props.setPedido} />
                </div>
                :
                <Categorias navProductos={productoFrame} />}

            <Pedido pedido={props.pedido} setPedido={props.setPedido} />
        </div >
    );
}

export default SalonPage;