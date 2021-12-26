import { Link } from "react-router-dom";
import HeaderComp from "../components/HeaderComp.js";



function ObjectPage(params) {
    const stockList = params.location.data
    return (
        <div>
            <HeaderComp></HeaderComp>
            <h2>Название типа акции: {stockList.namestock}</h2>
            <h4>Описание типа акции:</h4>
            <p>{stockList.description}</p>
            <Link to="/Stocks"><button>Назад</button></Link>
        </div>
    );
}


export default ObjectPage;

