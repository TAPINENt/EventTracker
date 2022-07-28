import React, {Component} from "react";
import { Button, TextField } from "@material-ui/core";
import { AppBar } from "@material-ui/core";
import { Dialog } from "@material-ui/core";
import { ThemeProvider as MuiThemeProvider } from "@material-ui/core";



export class UserAccount extends Component{
    continue = e => {
        e.preventDefault();
        this.props.nextStep();
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
                        <AppBar title="Enter Your Account Informtion" />
                        <TextField
                            placeholder="Enter your First Name"
                            label="First Name"
                            onChange={handleChange('firstName')}
                            defaultValue={values.firstName}
                            margin="normal"
                            fullWidth
                        />
                        <br />
                        <TextField
                            placeholder="Enter your Last Name"
                            label="Last Name"
                            onChange={handleChange('lastName')}
                            defaultValue={values.lastName}
                            margin="normal"
                            fullWidth
                        />
                        <br />
                        <TextField
                            placeholder="Enter your display Name"
                            label="display Name"
                            onChange={handleChange('displayName')}
                            defaultValue={values.displayName}
                            margin="normal"
                            fullWidth
                        />
                        <br />
                        <Button
                            color="primary"
                            variant="contained"
                            onClick={this.continue}
                        >
                            Continue
                        </Button>
                    </Dialog>
                </>
            </MuiThemeProvider>
            </>
        )
    }
}

export default UserAccount