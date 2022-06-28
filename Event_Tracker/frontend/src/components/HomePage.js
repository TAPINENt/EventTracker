import React, { Component } from "react";
import EventJoinPage from "./EventJoinPage";
import CreateRoomPage from "./CreateRoomPage";
import Event from "./Event";
import Home from "./Home";
import { BrowserRouter as Router, Switch, Route, Link, Redirect, } from "react-router-dom";


export default class App extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return (
        <Router>
            <switch>
<<<<<<< HEAD
                {/* <Route exact path= '/'>
                    <p>This is Homepage Testing 101</p>
                    <p> Tryin g something else</p>
                    <a href="/host/event/home/" > Test </a>
                </Route> */}
                <Route path='/' component={Home} ></Route>
=======
                <Route exact path= '/'>
                    <p>This is Homepag</p>
                </Route>
>>>>>>> origin/master
                <Route path='/join' component={EventJoinPage} ></Route>
                <Route path='/create' component={CreateRoomPage} ></Route>
                <Route path='/event/:eventCode' component={Event}></Route>
            </switch>
        </Router>);
    }
}