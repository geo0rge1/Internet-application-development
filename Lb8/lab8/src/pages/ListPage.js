import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import HeaderComp from "../components/HeaderComp.js";
import getObjects from "../modules/GetObjects.js";
import ObjectPage from "./ObjectPage.js"


function ListPage() {

    const [stockList, setstockList] = useState([])
    const [stockNames, setstockNames] = useState([])

    const handleObjectsList = async () => {
        const names = []
        const stocks = await getObjects()
        for (let stock of stocks) {
            names.push(stock["namestock"]);
        }
        setstockList(stocks)
        setstockNames(names)
    }

    useEffect(()=>{
        handleObjectsList()
    }, [])

    return (
        <div>
            <HeaderComp></HeaderComp>
            <h2>список Stocks</h2>
            <ul>
                {stockNames.map((namestock)=>{
                    return (
                        <li key={namestock}>
                            <Link to={{pathname: "/stocks/object", data: stockList.find(o => o.namestock == namestock)}}>{namestock}</Link>
                        </li>
                   )
                })}
            </ul>
        </div>
    );
}

export default ListPage;

