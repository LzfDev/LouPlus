import React, { Component } from 'react';
import Cookies from 'js-cookie';
import Row from 'react-bootstrap/lib/Row';
import Col from 'react-bootstrap/lib/Col';
import Button from 'react-bootstrap/lib/Button';
import Glyphicon from 'react-bootstrap/lib/Glyphicon';
import Api from '../Logic/Api';
import swal from 'sweetalert';


class SharePanel extends Component {
    constructor(props){
        super(props);
        this.state = {
            file: null
        };
    }
    
    componentDidMount(){
        const path = this.props.path;
        Api.getFileInfoWithShareUrl(path)
        .then(response => {
            if(response.ok){
                response.json()
                    .then(responseJson =>{
                        this.setState({
                            file: responseJson.data
                        });

                        // 设置Cookie用于下载认证
                        var token = Cookies.get('token');
                        if (token){
                            return;
                            
                        } else if (responseJson.data.open_private_share){
                            swal({
                                text: 'Please type the password',
                                content: {
                                    element: "input",
                                    attributes:{
                                        placeholder:"Type your password",
                                        type: "password",
                                    },
                                },
                                button: {
                                    text: "Go",
                                    closeModal: false,
                                    closeOnEsc: false,
                                },
                                closeOnClickOutside: false,
                            })
                            .then(password => {
                                Api.getFileInfoWithShareUrl(path, password)
                                .then(response => {
                                    response.json()
                                    .then(responseJson => {
                                        // 密码正确，设置Token
                                        if(responseJson.data.token){
                                            Cookies.set('token', responseJson.data.token, { expires: 1});
                                            swal.close();
                                        } else {
                                            swal("Wrong password");
                                        }
                                    });
                                })
                            })
                        }
                        
                        if (responseJson.data.token){
                            Cookies.set('token', responseJson.data.token, { expires: 1});
                        }
                    })
            }
        })
    }
    
    render(){
        if (!this.state.file){
            return (
                    <Col md={4} mdOffset={4}>
                        <span> The file you are requesting does not exists!</span>
                    </Col>

                    );
        }
        return (
                <Row>
                    <Col md={1} mdOffset={4}>
                        <Glyphicon glyph='file' style={{ 'fontSize': '90px'}}/>
                    </Col>
                    <Col md={4}>
                    <p>{this.state.file.filename}</p>
                    <Button style={{ 'marginTop': '25px' }} href={Api.generateShareFileDownloadUrl(this.props.path)}><Glyphicon glyph='save-file' />Download</Button>
                    </Col>
                </Row>
                );
    }
    
}


export default SharePanel;