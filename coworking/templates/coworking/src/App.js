import './App.css';
import {BrowserRouter, Route} from "react-router-dom";
import {Component} from "react";
import {Provider} from "react-redux";
import store from "./redux/store";
import HeaderContainer from "./components/header/HeaderContainer";
import SpacesContainer from "./components/spaces/SpacesContainer";
import SpaceFullContainer from "./components/spaces/SpaceFullContainer";

class App extends Component {
  render() {
    return (
        <BrowserRouter>
          <Provider store={store}>
            <div className="App">
              <HeaderContainer/>
              <main>
                <Route path={"/spaces"}>
                  <SpacesContainer/>
                </Route>
              </main>
            </div>
          </Provider>
        </BrowserRouter>
    );
  }
}


export default App;
