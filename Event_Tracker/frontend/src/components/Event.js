import React, { Component } from 'react';

export default class Event extends Component {
    constructor(props){
        super(props);
        this.state = {
            eventName : "Open Mic",
            hostName : "Stalanic",
            eventOrg : "Bust Boys"
        };
        this.eventCode = this.props.match.params.eventCode;
    }

    render(){
        return <div>
            <h3>{this.eventCode}</h3>
            <p> Event Name; {this.state.eventName}</p>
            <p> Host; {this.state.hostName}</p>
            <p> Org; {this.state.eventOrg}</p>
        </div>
    }
}