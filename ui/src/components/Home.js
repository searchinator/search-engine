import axios from 'axios';
import React, { useState } from 'react';


function Home() {

    const [line, setLine] = useState("");
    const [cstable, setCSTable] = useState();
    const [alphatable, setAlphaTable] = useState();

    const handleLineInput = (ev) => {
        ev.preventDefault();
        setLine(ev.target.value);
    }

    const handleSubmit = (ev) => {
        ev.preventDefault();
        if (line === "") {
            console.log("No input line entered.");
            return;
        }
        axios.post("http://localhost:5000/circular-shift", { line })
            .then(res => {
                let csLines = res.data['csLines'];
                setCSTable(generateTable(csLines));
                console.log(`handleSubmit - Response: ${res.data['csLines']}`);
                axios.get("http://localhost:5000/alphabetize")
                    .then(res => {
                        let alphaLines = res.data['alphaLines'];
                        setAlphaTable(generateTable(alphaLines));
                        console.log(`handleSubmit - Response: ${res.data['alphaLines']}`);
                    })
            })
            .catch(err => {
                console.log(`handleSubmit - Error: ${err}`);
            })
    }

    const generateTable = (list) => {
        let tableData = list.map(item => (
            <tr key={item}><td>{item}</td></tr>
        ));
        let table = (
            <table className="table table-striped">
                <tbody>
                    {tableData}
                </tbody>
            </table>
        )
        return table;
    };

    return (
        <div className="container-fluid">
            <div className="row">
                <div className="col-6">
                    <div className="mb-3">
                        <label htmlFor="inputLine" className="form-label">Input Line</label>
                        <input type="text" className="form-control" id="inputLine" onChange={handleLineInput} />
                    </div>
                    <button type="button" className="btn btn-primary" onClick={handleSubmit}>Submit</button>
                </div>
            </div>
            {cstable && <div className="row">Circular Shifts</div>}
            <div className="row">
                <div className="col-6">
                    {cstable}
                </div>
            </div>
            {alphatable && <div className="row">Alphabetic Shifts</div>}
            <div className="row">
                <div className="col-6">
                    {alphatable}
                </div>
            </div>
        </div>
    );
}

export default Home;
