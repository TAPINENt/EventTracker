import React, {Component} from "react";
import { Button, TextField } from "@material-ui/core";
import { AppBar } from "@material-ui/core";
import { Dialog } from "@material-ui/core";
import { ThemeProvider as MuiThemeProvider } from "@material-ui/core";
import { List, ListItem, ListItemText } from "@material-ui/core";



export class Confirm extends Component{
    continue = e => {
        e.preventDefault();
        //Process Form//
        this.props.nextStep();
    };
    back = e => {
        e.preventDefault();
        this.props.prevStep();
    };

    handleClose = () => {
        setOpen(false);
    };

    render() {

        //const [ open, setOpen] = React.useState(false)
        const { values: { displayName, firstName, lastName, bio, snapChat, instagram, twitter, cashApp, venmo, payPal }} = this.props;
        return(<>
         {/* <h1> Test </h1> */}
             <MuiThemeProvider>
                <>
                    <Dialog
                        open
                        fullWidth
                        maxWidth="sm"
                    >
                        <AppBar title="Confirm User Data" />
                        <List>
                            <ListItem>
                                <ListItemText primary="First Name" secondary={firstName} />
                            </ListItem>
                            <ListItem>
                                <ListItemText primary="Last Name" secondary={lastName} />
                            </ListItem>
                            <ListItem>
                                <ListItemText primary="display Name" secondary={displayName} />
                            </ListItem>
                            <ListItem>
                                <ListItemText primary="cashApp" secondary={cashApp} />
                            </ListItem>
                            <ListItem>
                                <ListItemText primary="venmo" secondary={venmo} />
                            </ListItem>
                            <ListItem>
                                <ListItemText primary="payPal" secondary={payPal} />
                            </ListItem>
                        </List>
                        <br />
                        <Button
                            color="primary"
                            variant="contained"
                            onClick={this.back}
                        >
                            Back
                        </Button>
                        <Button
                            color="primary"
                            variant="contained"
                            onClick={this.continue}
                        >
                            Confirm & Continue
                        </Button>
                    </Dialog>
                </>
            </MuiThemeProvider>
            </>
        )
    }
}

export default Confirm