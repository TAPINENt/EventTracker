import React from 'react';
import { Button, Form, FormGroup, Input, Label } from 'reactstrap';
import { Grid } from '@material-ui/core';
import axios from "axios";
import { API_URL } from '../../..';



class InformationForm extends React.Component{
    state ={
        eventName: "",
        hostName: "",
        eventOrg: "",
        instagram: "",
        twitter: ""
    };

    componentDidMount(){
        if(this.props.users){
            const { twitter, instagram } = this.props.users;
            this.setState({ twitter, instagram });
        }
    }

    onChange = e => {
        this.setState({ [e.target.twitter]: e.target.value });
    };
    
    createUser = e => {
        e.preventDefault();
        axios.post(API_URL, this.state).then(() => {
            this.props.resetState();
            this.props.toggle();
        });
    };
    
    editUser = e => {
        e.preventDefault();
        axios.post(API_URL, this.state).then(() => {
            this.props.resetState();
            this.props.toggle();
        });
    };

    defaultIfEmpty = value => {
        return value === "" ? "" : value;
    };

    render(){
        return (
            <form onSubmit={this.props.users ? this.editUser : this.createUser}>
                <FormGroup>
                    <Label for="twitter">Twitter:</Label>
                    <input
                        type="text"
                        name="twitter"
                        onChange={this.onChange}
                        value={this.defaultIfEmpty(this.state.twitter)}
                    />
                </FormGroup>
                <FormGroup>
                    <Label for="instagram">Instagram:</Label>
                    <input
                        type="text"
                        name="instagram"
                        onChange={this.onChange}
                        value={this.defaultIfEmpty(this.state.instagram)}
                    />
                </FormGroup>
                <Button>Submit</Button>
            </form>
        );
    }
}

export default InformationForm;












// const initialFValues={
//     id :0,
//     firstname :'',
//     lastname :'',
//     twitter :'',
//     instagram :''
// }

// export default function InformationForm(){

//     const [values,setValues] = useState(initialFValues);

//     return(
//         <form>
//             <Grid container>
//                 <Grid item xs={6}>
//                     <TextField 
//                     variant="outlined"
//                     label="firstname"
//                     value={values.firstname}
//                     />
//                     <TextField 
//                     variant="outlined"
//                     label="lastname"
//                     value={values.lastname}
//                     />
//                 </Grid>
//                 <Grid item></Grid>
//             </Grid>
//         </form>
//     )
// }
