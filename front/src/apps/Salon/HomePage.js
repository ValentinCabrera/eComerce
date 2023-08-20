import { getNewPedido } from "./Utils/Fetchs";
import SalonPage from "./SalonPage";
import { useState } from "react";

function HomePage() {
    const [pedido, setPedido] = useState();

    function navCategoria() {
        getNewPedido()
            .then(pedido => {
                setPedido(pedido);
            });
    }

    return (
        pedido ? <SalonPage pedido={pedido} setPedido={setPedido} /> : <button onClick={navCategoria}>Comenzar compra</button>
    )
}

export default HomePage;