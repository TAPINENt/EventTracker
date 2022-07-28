import React from 'react';
import { Button, Form, FormGroup, Input, Label } from 'reactstrap';
import { Grid } from '@material-ui/core';
import axios from "axios";
import { API_URL } from '..';



class InformationForm extends React.Component{
    constructor(props){
        super(props)

        this.state ={
            displayName: "",
            firstName: "", //optional
            lastName: "", //optional
            bio: "",
            snapChat: "",
            instagram: "",
            twitter: "",
            cashApp: "",
            venmo: "",
            payPal: "",
        }
    }

    // state ={
    //     displayName: "",
    //     firstName: "", //optional
    //     lastName: "", //optional
    //     bio: "",
    //     snapChat: "",
    //     instagram: "",
    //     twitter: "",
    //     cashApp: "",
    //     venmo: "",
    //     payPal: "",
    // };

    // componentDidMount(){
    //     if(this.props.users){
    //         const { twitter, instagram } = this.props.users;
    //         this.setState({ twitter, instagram });
    //     }
    // }

    onChange = (e) => {
        console.log({ [e.target.name]: e.target.value });
        // this.setState({ [e.target.name]: e.target.value });
    };
    
    // createUser = e => {
    //     e.preventDefault();
    //     axios.post(API_URL, this.state).then(() => {
    //         this.props.resetState();
    //         this.props.toggle();
    //     });
    // };
    
    // editUser = e => {
    //     e.preventDefault();
    //     axios.post(API_URL, this.state).then(() => {
    //         this.props.resetState();
    //         this.props.toggle();
    //     });
    // };

    // defaultIfEmpty = value => {
    //     return value === "" ? "" : value;
    // };

    handlesubmit = (e) => {
        console.log('${this.state.twitter} ${this.state.instagram}')
        // alert('${this.state.twitter} ${this.state.instagram}')
    }

   // handleTwitterchange = e => {

    //}

    render(){
        return (
            // <form onSubmit={this.props.users ? this.editUser : this.createUser}>
            // <form onSubmit={this.handlesubmit}>
            //     <FormGroup>
            //         <Label for="twitter">Twitter:</Label>
            //         <input
            //             type="text"
            //             name="twitter"
            //             value={this.state.twitter}
            //             // value={this.defaultIfEmpty(this.state.twitter)}
            //             onChange={this.onChange}
            //         />
            //     </FormGroup>
            //     <FormGroup>
            //         <Label for="instagram">Instagram:</Label>
            //         <input
            //             type="text"
            //             name="instagram"
            //             onChange={this.onChange}
            //             value={this.state.instagram}
            //             // value={this.defaultIfEmpty(this.state.instagram)}
            //         />
            //     </FormGroup>
            //     <button type='submit'>Submit</button>
            //     {/* <Button type='submit'>Submit</Button> */}
            // </form>


            <form onSubmit={this.handlesubmit}>
                    <label for="twitter">Twitter:</label>
                    <input
                        type="text"
                        name="twitter"
                        value={this.state.twitter}
                        // value={this.defaultIfEmpty(this.state.twitter)}
                        onChange={this.onChange}
                    />
                    <label for="instagram">Instagram:</label>
                    <input
                        type="text"
                        name="instagram"
                        onChange={this.onChange}
                        value={this.state.instagram}
                        // value={this.defaultIfEmpty(this.state.instagram)}
                    />
                <button type='submit'>Submit</button>
                {/* <Button type='submit'>Submit</Button> */}
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
