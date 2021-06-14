const TEST_TYPE = "TEST_TYPE";

let initialState = {

}

export const headerReducer = (state = initialState, action) => {
  switch (action.type) {
    case (TEST_TYPE):
      break
    default:
      return state;
  }
}

export const testDispatcher = () => ({type: TEST_TYPE});