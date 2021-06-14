const LOGIN = "LOGIN";
const LOGOUT = "LOGOUT";

let initialState = {
  isAuth: true
}

export const authReducer = (state = initialState, action) => {
  switch (action.type) {
    case (LOGIN):
      return {
        ...state,
        isAuth: action.data

      }
    case (LOGOUT):
      return {
        ...state,
        isAuth: action.data
      }
    default:
      return state;
  }
}

export const login = () => ({type: LOGIN, data: true});
export const logout = () => ({type: LOGOUT, data: false});