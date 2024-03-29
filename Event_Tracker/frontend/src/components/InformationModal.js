import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from 'reactstrap';
import { Link } from "react-router-dom";
import InformationForm from "./informationform";


class InformationModal extends Component {
    state = {
        modal: false
    };

    toggle = () => {
        this.setState(previous => ({
            modal: !previous.modal
        }));
    };

    render(){
        const create = this.props.create;

        var title = "Editing Info";
        var button = <Button 
        color="secondary"
        className="float-right"
        color = "#0000ff"
        variant="contained"
        style={{ minWidth: "200px"}}
        onClick={this.toggle}> Edit</Button>
        if(create){
            title = "Creating User Information";

            button = (
                <Button
                    className="float-right"
                    onClick={this.toggle}
                    style={{ minWidth: "200px", backgroundColor: "red"}}
                    >
                        Create New
                    </Button>
            );
        }

        return(
            <Fragment>
                {button}
                <Modal isOpen={this.state.modal} toggle={this.toggle}>
                    <ModalHeader toggle={this.toggle}>{title}</ModalHeader>
                    <ModalBody>
                        <InformationForm/>
                        {/* <InformationForm
                            resetState={this.props.resetState}
                            toggle={this.toggle}
                            users={this.props.users}
                            /> */}
                    </ModalBody>
                </Modal>
            </Fragment>
        );
    }
}

export default InformationModal
