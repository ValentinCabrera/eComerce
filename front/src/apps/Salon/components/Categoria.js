function Categoria(props) {
    return (
        <button onClick={() => props.navProductos(props.categoria)}>{props.categoria.nombre}</button>
    )
}

export default Categoria;