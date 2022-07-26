import React, { Component } from "react";
import InformationForm from "./informationform";
import InformationModal from "./InformationModal";
import axios from "axios";
import { API_URL } from "..";


export default class Home extends Component {
    constructor(props) {
      super(props);
    }

    render(){
        return <html>
            <div className="center">
                <p>This is Homepage Testing 101</p>
                <p> Tryin g something else</p>
                <p> Stanly is a whore</p>
                <a href="/host/event/home/" > Test </a>
                <InformationForm/>
                <InformationModal/>
            </div>
        </html>
    }
}