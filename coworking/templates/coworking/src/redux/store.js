import {applyMiddleware, combineReducers, compose, createStore} from "redux";
import {headerReducer} from "./headerReducer";
import thunkMiddleware from "redux-thunk"
import {authReducer} from "./authReducer";
import {spacesReducer} from "./spacesReducer";

let reducers = combineReducers({
  Header: headerReducer,
  Auth: authReducer,
  Spaces: spacesReducer
});

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(reducers,composeEnhancers(
    applyMiddleware(thunkMiddleware)
));


export default store;