import * as axios from "axios";


const instance = axios.create({
  // withCredentials: true,
  baseURL: "http://127.0.0.1:8000/",
  // headers: {
  //   "API-KEY": "77e9a31a-c3e8-44e3-857f-f3ed39be205a"
  // }
});

export const usersAPI = {
  getUsers() {
    return instance.get(`api/users`)
        .then(response => response.data);
  },
}

export const spacesAPI = {
  getSpaces() {
    return instance.get(`spaces/api/spaces`)
        .then(response => {
          return response.data
        });
  },
  getSpace(index) {
    return instance.get(`spaces/api/spaces/${index}`)
        .then(response => {
          return response.data
        });
  },
}
