import axios from 'axios';
import React, { useState } from 'react';


function Home() {

    const [query, setQuery] = useState("");
    const [searchResultTable, setSearchResultTable] = useState();
    const [searchResult, setSearchResult] = useState([]);
    const [currPage, setCurrPage] = useState(0);
    const [totalPages, setTotalPages] = useState(0);

    const handleLineInput = (ev) => {
        ev.preventDefault();
        setQuery(ev.target.value);
    }

    const handlePagination = (num) => {
        makeRequest(query, currPage + num, 10);
    }

    const makeRequest = (query, page_num, page_size) => {
        axios.post("http://127.0.0.1:5000/search", { page_size, page_num }, { params: { query } })
            .then(res => {
                console.log(res.data);
                setSearchResult(res.data);
                setSearchResultTable(generateTable(res.data.queryResult));
                setCurrPage(page_num);
                setTotalPages(res.data.total_pages)
            })
            .catch(err => {
                console.log(`handleSubmit - Error: ${err}`);
            })
    }

    const handleSearch = (ev) => {
        ev.preventDefault();
        if (query === "") {
            console.log("No input line entered.");
            return;
        }
        makeRequest(query, 1, 10);
        // axios.post("http://127.0.0.1:5000/search", { page_size: 10, page_num: 1 }, { params: { query } })
        //     .then(res => {
        //         console.log(res.data);
        //         setSearchResult(res.data);
        //         setSearchResultTable(generateTable(res.data.queryResult));
        //         setCurrPage(1);
        //         setTotalPages(res.data.total_pages)
        //     })
        //     .catch(err => {
        //         console.log(`handleSearch - Error: ${err}`);
        //     })
    }

    const generateTable = (list) => {
        let resultList = list.map(item => (
            <div style={{ paddingTop: 10 }}>
                <div className="card" style={{ width: 900 }} key={item.id}>
                    <div className="card-body">
                        <p className="card-text">{item.desc}</p>
                        <a href={item.url}>{item.url}</a>
                    </div>
                </div>
            </div>
        ))
        return resultList;
    };

    return (
        <div className="container-fluid">
            <div className="row" style={{ paddingTop: 10 }}>
                <div className="col-3"></div>
                <div className="col-6">
                    <div className="mb-3">
                        <input type="text" className="form-control" id="inputLine" onChange={handleLineInput} />
                    </div>
                    <button type="button" className="btn btn-primary" onClick={handleSearch}>Search</button>
                </div>
            </div>
            <div className="row" style={{ paddingTop: 10 }}>
                <div className="col-3"></div>
                <div className="col-9">
                    {searchResultTable}
                </div>
            </div>
            <nav aria-label="Page navigation example">
                <ul className="pagination justify-content-center">
                    <li className={`page-item ${currPage <= 1 ? "disabled" : ""}`}>
                        <a className="page-link" onClick={(ev) => { handlePagination(-1) }} tabindex="-1">Previous</a>
                    </li>
                    {currPage} / {totalPages}
                    <li className={`page-item ${currPage >= totalPages ? "disabled" : ""}`}>
                        <a className="page-link" onClick={(ev) => { handlePagination(1) }}>Next</a>
                    </li>
                </ul>
            </nav>
        </div>
    );
}

export default Home;
