import axios from 'axios';
import React, { useState } from 'react';
import icon from '../images/icon.jpeg';

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
    }

    const generateTable = (list) => {
        let resultList = list.map(item => (
            <div style={{ paddingTop: 10 }}>
                <div className="card" style={{ width: 900 }} key={item.id}>
                    <div className="card-body">
                        <h5 className="card-title">{item.desc.length > 90 ? (item.desc.substring(0, 90) + "...") : (item.desc)}</h5>
                        <a href="#" className="card-link text-success"><h6>{item.url}</h6></a>
                    </div>
                </div>
            </div>
        ))
        return resultList;
    };



    const defaultIcon = (customWidth, customHeight, marginTop) => {
        return (
            <img src={icon} className="rounded img-fluid" alt="searchinator" style={{
                width: customWidth,
                height: customHeight,
                marginTop: marginTop
            }} />
        );
    }

    const homePageLayout = () => {
        return (
            <div className="container-fluid">
                <div className="row" style={{ paddingTop: 150 }}>
                    <div className="col-4"></div>
                    <div className="col-4">
                        {defaultIcon("550px", "250px")}
                    </div>
                </div>
                <div className="row" style={{ paddingTop: 10 }}>
                    <div className="col-3">
                    </div>
                    <div className="col-6">
                        <div className="mb-3">
                            <input type="text" className="form-control" id="inputLine" onChange={handleLineInput} />
                        </div>
                    </div>
                </div>
                <div className="row justify-content-md-center">
                    <div className="col-4"></div>
                    <div className="col-1"></div>
                    <div className="col-2">
                        <button type="button" className="btn btn-primary" onClick={handleSearch}>Search</button>
                    </div>
                    <div className="col-4"></div>
                </div>
            </div>
        )
    }

    const searchResultLayout = () => {
        return (
            <div className="container-fluid">
                <div className="row bg-light" style={{ paddingTop: 10 }}>
                    <div className="col-1">
                        {defaultIcon("100px", "50px", "10px")}
                    </div>
                    <div className="col-6">
                        <div className="mb-3">
                            <input type="text" style={{ marginTop: 20 }} className="form-control" id="inputLine" onChange={handleLineInput} defaultValue={query} />
                        </div>
                    </div>
                    <div className="col-3">
                        <button type="button" style={{ marginTop: 20 }} className="btn btn-primary" onClick={handleSearch}>Search</button>
                    </div>
                </div>
                <div className="row" style={{ paddingTop: 10 }}>
                    <div className="col-1"></div>
                    <div className="col-9">
                        {searchResultTable}
                    </div>
                </div>
                {searchResult.length != 0 && <nav style={{ paddingTop: 15 }}>
                    <ul className="pagination justify-content-center">
                        <li className={`page-item ${currPage <= 1 ? "disabled" : ""}`}>
                            <a className="page-link" onClick={(ev) => { handlePagination(-1) }} tabIndex="-1">Previous</a>
                        </li>
                        <div style={{ paddingTop: 5, paddingLeft: 6, paddingRight: 6 }}>
                            {currPage} / {totalPages}
                        </div>
                        <li className={`page-item ${currPage >= totalPages ? "disabled" : ""}`}>
                            <a className="page-link" onClick={(ev) => { handlePagination(1) }}>Next</a>
                        </li>
                    </ul>
                </nav>}
            </div>
        )
    };

    return (
        <div>
            {searchResult.length === 0 && homePageLayout()}
            {searchResult.length !== 0 && searchResultLayout()}
        </div>
        // <div className="container-fluid">
        //     {searchResult.length === 0 && defaultIcon("300px")}
        //     <div className="row" style={{ paddingTop: 10 }}>
        //         <div className="col-1">
        //             {searchResult.length !== 0 && searchResultIcon()}
        //         </div>
        //         <div className="col-6">
        //             <div className="mb-3">
        //                 <input type="text" className="form-control" id="inputLine" onChange={handleLineInput} />
        //             </div>
        //             {/* <button type="button" className="btn btn-primary" onClick={handleSearch}>Search</button> */}
        //         </div>
        //     </div>
        //     <div className="row justify-content-md-center">
        //         <div className="col-4"></div>
        //         <div className="col-1"></div>
        //         <div className="col-2">
        //             <button type="button" className="btn btn-primary" onClick={handleSearch}>Search</button>
        //         </div>
        //         <div className="col-4"></div>
        //     </div>
        //     <div className="row" style={{ paddingTop: 10 }}>
        //         <div className="col-3"></div>
        //         <div className="col-9">
        //             {searchResultTable}
        //         </div>
        //     </div>
        //     {searchResult.length !== 0 && <nav style={{ paddingTop: 10 }}>
        //         <ul className="pagination justify-content-center">
        //             <li className={`page-item ${currPage <= 1 ? "disabled" : ""}`}>
        //                 <a className="page-link" onClick={(ev) => { handlePagination(-1) }} tabIndex="-1">Previous</a>
        //             </li>
        //             {currPage} / {totalPages}
        //             <li className={`page-item ${currPage >= totalPages ? "disabled" : ""}`}>
        //                 <a className="page-link" onClick={(ev) => { handlePagination(1) }}>Next</a>
        //             </li>
        //         </ul>
        //     </nav>}
        // </div>
    );
}

export default Home;
