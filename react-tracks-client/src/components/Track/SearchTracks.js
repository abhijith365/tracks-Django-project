import React from "react";
import withStyles from "@material-ui/core/styles/withStyles";
// import TextField from "@material-ui/core/TextField";
// import ClearIcon from "@material-ui/icons/Clear";
// import Paper from "@material-ui/core/Paper";
// import IconButton from "@material-ui/core/IconButton";
// import SearchIcon from "@material-ui/icons/Search";

const SearchTracks = ({ classes }) => {
  return <div>SearchTracks</div>;
};

const styles = theme => ({
  root: {
    padding: "2px 4px",
    margin: theme.spacing.unit,
    display: "flex",
    alignItems: "center"
  }
});

export default withStyles(styles)(SearchTracks);
