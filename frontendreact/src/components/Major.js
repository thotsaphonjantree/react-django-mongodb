import React, { Component } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom';

export class Major extends Component {
    constructor(props) {
        super(props)

        this.state = { rows: [] }
    }

    componentDidMount() {

        { this.getMajor() }
    }

    getMajor = () => {
        var dataAllMajor = []
        axios.defaults.baseURL = 'http://localhost:8082/api/';
        axios.get('major/').then(result => {
            console.log(result.data)
            result.data.forEach(item => {
                dataAllMajor.push(item)
            })
            this.setState({ rows: dataAllMajor })
        })
    }
    render() {
        return (
            <div>
                <center>
                    <h1>Majors</h1>
                    <table border='1' width='50%' cellSpacing="0">
                        <tbody>
                            <tr>
                                <th>No.</th><th>Major</th>
                            </tr>
                            {this.state.rows.map((item,index) => (
                                <tr key={index}>
                                    <td>{index+1}</td>
                                    <td><Link to={`/sbymajor/${item.id}`}>{item.major_name}</Link></td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </center>
            </div>
        )
    }
}

export default Major
