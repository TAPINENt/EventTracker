import React, {Component} from "react";
import { Button, TextField } from "@material-ui/core";
import { AppBar } from "@material-ui/core";
import { Dialog } from "@material-ui/core";
import { ThemeProvider as MuiThemeProvider } from "@material-ui/core";



export class UserPayment extends Component{
    continue = e => {
        e.preventDefault();
        this.props.nextStep();
    }
    back = e => {
        e.preventDefault();
        this.props.prevStep();
    }

    render() {
        const { values, handleChange} = this.props;
        return(<>
         {/* <h1> Test </h1> */}
             <MuiThemeProvider>
                <>
                    <Dialog
                        open
                        fullWidth
                        maxWidth="sm"
                    >
                        <AppBar title="Enter Your Payment Informtion" />
                        <TextField
                            placeholder="Enter your cashApp Name"
                            label="cashApp Name"
                            onChange={handleChange('cashApp')}
                            defaultValue={values.cashApp}
                            margin="normal"
                            fullWidth
                        />
                        <br />
                        <TextField
                            placeholder="Enter your venmo Name"
                            label="venmo Name"
                            onChange={handleChange('venmo')}
                            defaultValue={values.venmo}
                            margin="normal"
                            fullWidth
                        />
                        <br />
                        <TextField
                            placeholder="Enter your payPal"
                            label="payPal"
                            onChange={handleChange('payPal')}
                            defaultValue={values.payPal}
                            margin="normal"
                            fullWidth
                        />
                        <br />
                        <Button
                            color="secondary"
                            variant="contained"
                            onClick={this.back}
                        >Back</Button>
                        
                        <Button
                            color="primary"
                            variant="contained"
                            onClick={this.continue}
                        >Continue</Button>
                    </Dialog>
                </>
            </MuiThemeProvider>
            </>
        )
    }
}

export default UserPayment