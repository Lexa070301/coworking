import React from 'react'
import {compose} from "redux";
import {connect} from "react-redux";
import Spaces from "./Spaces";
import {setSpaces} from "../../redux/spacesReducer";
import {Route} from "react-router-dom";
import SpaceFullContainer from "./SpaceFullContainer";

class SpacesAPIComponent extends React.Component {
  componentDidMount() {
    this.props.setSpaces();
  }

  render() {
    return (
        <>
          <Route path={"/spaces/:index"}>
            <SpaceFullContainer/>
          </Route>
          <Route path={"/spaces"} exact={true}>
            <Spaces spaces={this.props.Spaces}/>
          </Route>
        </>
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