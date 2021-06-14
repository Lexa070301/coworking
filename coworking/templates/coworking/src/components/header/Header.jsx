import {NavLink} from "react-router-dom";
import logo from "../../assets/logo.svg";

const Header = (props) => {
  const logIn = () => {
    props.login()
  }

  const logOut = () => {
    props.logout()
  }

  return (
      <header className={"header"}>
        <div className={"container-fluid"}>
          <div className="header-card d-flex justify-content-between align-items-center">
            <NavLink to={"/"}><img src={logo} className={"logo"} alt="Logo"/></NavLink>
            <ul className={"menu"}>
              <li className={"menu__item"}>
                <NavLink to={"/"} className={"menu__item__link"}>Main</NavLink>
                <NavLink to={"/test"} className={"menu__item__link"}>Test 2</NavLink>
              </li>
            </ul>
            <div>
              {
                props.isAuth ?
                    <button className={"btn btn-success"} onClick={logOut}>Log out</button> :
                    <button className={"btn btn-danger"} onClick={logIn}>Log in</button>
              }
            </div>
          </div>
        </div>
      </header>
  );
}

export default Header;