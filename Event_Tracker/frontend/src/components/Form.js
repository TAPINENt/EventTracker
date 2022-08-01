import React, {useState} from "react";
import { Link } from "react-router-dom";
import { Button, TextField } from "@material-ui/core";
import { AppBar } from "@material-ui/core";
import { Dialog } from "@material-ui/core";
import { ThemeProvider as MuiThemeProvider } from "@material-ui/core";
import UserAccount from "./UserAccount";
import UserPayment from "./UserPayment";
import UserSocials from "./UserSocials";
import UserBio from "./UserBio";
import Confirm from "./Confirm";


function Form(){
    const[page,setPage] = useState(0);
    
    const [formData, setFormData] = useState({
        displayName: "",
        email: "",
        firstName: "",
        lastName: "",
        twitter: "",
        instagram: "",
        snapchat: "",
        cashApp: "",
        venmo: "",
        paypal: "",
        bio: ""

      });

    const FormTitles = ["Performer Info","Socials","Payments","Bio","Summary"];

    const PageDisplay = () => {
        if (page === 0){
            return <UserAccount formData={formData} setFormData={setFormData}/>;
        } else if (page === 1){
            return <UserSocials formData={formData} setFormData={setFormData}/>;
        } else if (page === 2){
            return <UserPayment formData={formData} setFormData={setFormData}/>;
        } else if (page === 3){
            return <UserBio formData={formData} setFormData={setFormData}/>;
        } else {
            return <Confirm/>;
        }
    }

    return(
        <div className="form">
            <div className="progressbar"></div>
            <div className="form-container">
                <div className="header">
                    <h1>{FormTitles[page]}</h1>
                </div>
                <div className="form-body">{PageDisplay()}</div>
                <div className="footer">
                    <Button variant="contained" color='secondary'
                     disabled = {page == 0}
                    onClick={() => {setPage((currPage) => currPage-1)}}>
                    Prev</Button>

                    <Button variant="contained" color='primary'
                     disabled = {page == FormTitles.length -1}
                    onClick={() => {setPage((currPage) => currPage+1)}}>
                    Next</Button>
                
                </div>
            </div>
        </div>
    )
}

export default Form;