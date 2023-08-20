import React, { useEffect, useState } from 'react';
import { getCategorias } from '../Utils/Fetchs';

import Categoria from './Categoria';

function Categorias(props) {
    const [data, setData] = useState([]);

    useEffect(() => {
        getCategorias()
            .then(categorias => setData(categorias));
    }, []);

    return (
        <div>
            {data.map(categoria => (
                <Categoria categoria={categoria} navProductos={props.navProductos} key={categoria.id} />
            ))}
        </div>
    )
}

export default Categorias;