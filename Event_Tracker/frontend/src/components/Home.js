import React, { Component } from "react";
import { TextField, Button, Grid, Typography } from "@material-ui/core";
import { Link } from "react-router-dom";


export default class Home extends Component {
    constructor(props) {
      super(props);
    }

render(){
    return<html lang="en">
        <nav class="navbar navbar-dark">  
            <div class="container-fluid">
                 {/* <!-- <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navmenu">
                <span class="navbar-toggler-icon"></span>
                </button> -->  */}

            <a class="navbar-brand" style="color: black" href="/host/event/home/">
                Go Back
            </a>
            </div>
            

        <p>This is Homepage Testing 101</p>
        <p> Tryin g something else</p>
        <p> Stanly is a whore</p>
        <a href="/host/event/home/" > Test </a>
        </nav>
    </html>
}

}