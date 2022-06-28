import React, { Component } from "react";
import EventJoinPage from "./EventJoinPage";
import CreateRoomPage from "./CreateRoomPage";
import Event from "./Event";
import { BrowserRouter as Router, Switch, Route, Link, Redirect, } from "react-router-dom";


export default class App extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return (
        <Router>
            <switch>
                <Route exact path= '/'>
                    <p>This is Homepag</p>
                </Route>
                <Route path='/join' component={EventJoinPage} ></Route>
                <Route path='/create' component={CreateRoomPage} ></Route>
                <Route path='/event/:eventCode' component={Event}></Route>
            </switch>
        </Router>);
    }
}