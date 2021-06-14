import React from 'react'
import {compose} from "redux";
import {connect} from "react-redux";
import {setSpaces} from "../../redux/spacesReducer";
import SpaceFull from "./SpaceFull";
import {withRouter} from "react-router";

class SpaceFullAPIComponent extends React.Component {
  componentDidMount() {
    let index = this.props.match.params.index;
    // this.props.setSpaces(index);
  }

  render() {
    return (
        <SpaceFull spaces={this.props.Spaces}/>
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
    withRouter,
)(SpaceFullAPIComponent);