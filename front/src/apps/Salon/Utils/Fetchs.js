
export async function getCategorias() {
    const response = await fetch("http://localhost:8000/productos/categorias/");
    const data = await response.json();
    return data;
}

export async function getProductos(categoria) {
    const response = await fetch("http://localhost:8000/productos/productos/",
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ "categoria": categoria })
        });
    const data = await response.json();
    return data;
}

export async function getNewPedido() {
    const response = await fetch("http://localhost:8000/pedidos/crear/")
    const data = await response.json();
    return data;
}

export async function addProducto(pedido, producto, cantidad, ingredientes) {
    const response = await fetch("http://localhost:8000/pedidos/agregar/",
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ "pedido": pedido, "producto": producto, "cantidad": cantidad, "ingredientes": ingredientes })
        });

    const data = await response.json();
    return data;
}