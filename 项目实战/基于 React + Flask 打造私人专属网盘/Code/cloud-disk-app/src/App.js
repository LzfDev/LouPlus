import React, { Component } from 'react';
import Cookies from 'js-cookie';
import Navbar from 'react-bootstrap/lib/Navbar';
import Row from 'react-bootstrap/lib/Row';
import Grid from 'react-bootstrap/lib/Grid';
import Glyphicon from 'react-bootstrap/lib/Glyphicon';
import Col from 'react-bootstrap/lib/Col';
import Button from 'react-bootstrap/lib/Button';
import {BrowserRouter as Router, Route} from 'react-router-dom';

import './App.css';
import Api from './Logic/Api';
import 'bootstrap/dist/css/bootstrap.min.css';
import swal from 'sweetalert';

//引入新增的组件
import LoginForm from './Component/LoginForm';
import MainPanel from './Component/MainPanel';
import SharePanel from './Component/SharePanel';


// 主页面
class MainPage extends Component {
    constructor(props){
        super(props);
        this.state = {
            login: false
        };

        this.onLogin = this.onLogin.bind(this);

    }

    componentDidMount(){
        var token = Cookies.get('token');
        if(token){
            // 验证token
            Api.auth(token)
                .then(response => {
                    if (response.ok){
                        this.setState({
                            login: true
                        });
                    }
                })
        }
    }

    onLogin(data){
        Cookies.set('token', data.token, { expires: 7 });
        this.setState({
            login: true
        });
    }

    render(){
        var content;
        if (this.state.login){
            content = <MainPanel />;
        } else {
            content = <LoginForm onLogin={this.onLogin} />;
        }
        return content;
    }
}


// 分享页面
class SharePage extends Component {
    constructor(props){
        super(props);
    }
    
    render(){
        return <SharePanel path={this.props.match.params.path} />;
    }
}

// 路由
const App = () =>(
        <Router>
            <Grid>
                <Row>
                    <Navbar>
                        <Navbar.Header>
                            <Navbar.Brand>
                                <a href="/">CloudDisk</a>
                            </Navbar.Brand>
                        </Navbar.Header>
                    </Navbar>
                    <Route path="/" exact component={MainPage} />
                    <Route path="/s/:path" component={SharePage} />
                </Row>
            </Grid>
        </Router>
        );


export default App;
