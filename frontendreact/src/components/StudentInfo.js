import React, { Component } from 'react'
import axios from 'axios'
export default class StudentInfo extends Component {
    constructor(props) {
        super(props)
        this.state = { student: '', major: [], rows: [''] }

        this.handleDelete = this.handleDelete.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSelectChange = this.handleSelectChange.bind(this)
    }
    componentDidMount() {
        { this.getStudentbyID() }
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

    getStudentbyID() {
        const { match: { params } } = this.props;
        axios.defaults.baseURL = 'http://localhost:8082/api/';
        axios.get(`student/${params.studentId}/`).then(result => {
            this.setState({ student: result.data, major: result.data.Major })
            console.log(result.data);
        })
    }

    handleDelete() {
        const { match: { params } } = this.props;
        axios.defaults.baseURL = 'http://localhost:8082/api/';
        axios.delete(`student/${params.studentId}/`)
            .then((res) => {
                console.log(res);
                console.log(res.data);
            });
        //window.location = '/students/';
    }

    handleInputChange(event) {
        const target = event.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = event.target.name;
        this.setState(prevState => ({
            ...prevState, student: {
                ...prevState.student, [name]: value
            }
        }));
    }

    handleSelectChange(event) {
        this.setState({
            major: event.target.value
        }
        );
    }

    handleSubmit = event => {
        event.preventDefault();
        const { match: { params } } = this.props;
        axios.defaults.baseURL = 'http://localhost:8082/api/';
        axios.put(`student/${params.studentId}/`, {
            student_code: this.state.student.student_code,
            first_name: this.state.student.first_name,
            last_name: this.state.student.last_name,
            Major: this.state.major
        })
            .then(res => {
                console.log(res);
                console.log(res.data);
            })
        console.dir(this.state);
        //window.location = '/students/';
    }


    render() {
        return (
            <div>
                <center>
                    <h1>Edit Student</h1>
                    <table width="50%">
                        <tbody>
                            <tr><td>Student ID</td><td><input type="text" name="student_code" size="80" value={this.state.student.student_code || ''} onChange={this.handleInputChange} /></td></tr>
                            <tr><td>First Name</td><td><input type="text" name="first_name" size="80" value={this.state.student.first_name || ''} onChange={this.handleInputChange} /></td></tr>
                            <tr><td>Last Name</td><td><input type="text" name="last_name" size="80" value={this.state.student.last_name || ''} onChange={this.handleInputChange} /></td></tr>
                            <tr><td>Major</td><td>
                                <select name="Major" value={this.state.major.id} onChange={this.handleSelectChange}>
                                <option disabled={true} value="">Please select one</option>
                                    {this.state.rows.map((item, index) => (
                                        <option value={item.id} key={index} >{item.major_name}</option>
                                    ))}
                                </select></td></tr>
                            <tr><td colSpan="2" align="center"><button onClick={this.handleSubmit}>Edit</button><button onClick={this.handleDelete}>Delete</button></td></tr>
                        </tbody>
                    </table>
                </center>


            </div>
        )
    }
}
