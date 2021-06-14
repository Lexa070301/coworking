import React from 'react'
import {compose} from "redux";
import {connect} from "react-redux";
import Spaces from "./Spaces";
import {spacesAPI} from "../../api/api";
import {setSpaces} from "../../redux/spacesReducer";

class SpacesAPIComponent extends React.Component {
  componentDidMount() {
    spacesAPI.getSpaces().then(response => {debugger});

  }

  render() {
    return (
        <Spaces spaces={this.props.Spaces}/>
    )
  }
}

let mapStateToProps = (state) => {
  return {
    Spaces: state.Spaces.Spaces
  }
}

export default compose(
    connect(mapStateToProps,
        {
          setSpaces,
        }
    ),
)(SpacesAPIComponent);