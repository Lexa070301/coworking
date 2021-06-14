import React from 'react'
import {compose} from "redux";
import {connect} from "react-redux";
import {login, logout} from "../../redux/authReducer";
import Header from "./Header";

class HeaderAPIComponent extends React.Component {
  render() {
    return (
        <Header isAuth={this.props.isAuth}
                login={this.props.login}
                logout={this.props.logout}/>
    )
  }
}

let mapStateToProps = (state) => {
  return {
    isAuth: state.Auth.isAuth
  }
}

export default compose(
    connect(mapStateToProps,
        {
          login,
          logout
        }
    ),
)(HeaderAPIComponent);