const getObjects = async () =>{
    return await fetch('http://127.0.0.1:8000/stocks/', {method: "GET"})
        .then((response) => {
            return response.json();
        }).catch(() => {
            return {resultCount: 0, results: []}
        })
}

export default getObjects
