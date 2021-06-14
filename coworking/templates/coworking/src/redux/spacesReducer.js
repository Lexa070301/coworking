import {spacesAPI} from "../api/api";

const SET_SPACES = "SET_SPACES";

let initialState = {
  Spaces: [
    {
      address: "ул. Пушкина д. Колотушкина",
      capacity: 5,
      name: "Райский остров",
      area: 4000,
      daily_cost: 2000,
      description: "Показательный пример – рондо мгновенно. Очевидно, что плавно-мобильное голосовое поле многопланово продолжает резкий эффект \"вау-вау\". Рондо однократно. Говорят также о фактуре, типичной для тех или иных жанров (\"фактура походного марша\", \"фактура вальса\" и пр.), и здесь мы видим, что плавно-мобильное голосовое поле начинает однокомпонентный фузз. Полимодальная организация варьирует модальный гармонический интервал. Гипнотический рифф полифигурно выстраивает самодостаточный динамический эллипсис, хотя это довольно часто напоминает песни Джима Моррисона и Патти Смит.",
      feature: [
        1
      ],
    },
  ]
}

export const spacesReducer = (state = initialState, action) => {
  switch (action.type) {
    case (SET_SPACES):
      return {
        ...state,
        Spaces: [
          ...action.data
        ]
      }
    default:
      return state;
  }
}

export const setSpacesAC = (data) => ({type: SET_SPACES, data});

export const setSpaces = () => async (dispatch) => {
  let response = await spacesAPI.getSpaces()
  dispatch(setSpacesAC(response))
}