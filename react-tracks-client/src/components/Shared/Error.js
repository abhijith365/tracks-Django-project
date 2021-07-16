import React from "react";
import withStyles from "@material-ui/core/styles/withStyles";
// import Button from "@material-ui/core/Button";
// import Snackbar from "@material-ui/core/Snackbar";

const Error = ({ classes }) => {
  return <div>Error</div>;
};

const styles = theme => ({
  snackbar: {
    margin: theme.spacing.unit
  }
});

export default withStyles(styles)(Error);
