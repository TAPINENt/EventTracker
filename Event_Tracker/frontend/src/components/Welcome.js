import React, { Component } from "react";
import { TextField, Button, Grid, Typography } from "@material-ui/core";
import { Link } from "react-router-dom";
import InformationForm from "./pages/Information/informationform";
import InformationModal from "./pages/Information/InformationModal";
// import { TextField, Button, Grid, Typography } from "@material-ui/core";
// import { Link } from "react-router-dom";


export default class Home extends Component {
    constructor(props) {
      super(props);
    }


render(){
    return(<html>
            <Grid container spacing={1} className="center">
                <Grid item xs={12} align="center">
                    <Button variant="contained" color="primary" onClick={this.eventButtonProssed}>
                        <InformationModal/>
                    </Button>
                    <Button variant="contained" color="secondary" to="/event/927aebef-92ef-4897-8f1f-0daf0f937f62" component={Link}> 
                        <InformationModal/>
                    </Button>
                </Grid>
            </Grid>
        </html>
        
        
    );
        
    // return<html lang="en">
    //     <nav class="navbar navbar-dark">  
    //         <div class="container-fluid">
    //                 {/* <!-- <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navmenu">
    //             <span class="navbar-toggler-icon"></span>
    //             inputProps={{style:{textAlign: "center"}}}
    //             </button> -->  */}

    //         <a  style={{"color": "yellow"}} href="/host/event/home/">
    //             Go Back
    //         </a>
    //         </div>
           
    //         <div> <p>This is Homepage Testing 101</p> </div>
    //         <div><p> Tryin g something else</p> </div>
    //         <div><p> Stanly is a whore</p> </div>
    //         <a class="test" href="/host/event/home/" > Test </a>
    //     </nav>     
    //         <div className="center">
    //             <button type="button" class="btn btn-primary btn-lg"> Guest</button>
    //             <button type="button" class="btn btn-primary btn-lg" to="/"> Performer</button>
    //         </div>

    //         {/* <Grid item xs={12} align="center">
    //       <Button variant="contained" color="secondary" to="/" component={Link}> 
    //         Back
    //       </Button>
    //     </Grid> */}

        
    // </html>
}

}