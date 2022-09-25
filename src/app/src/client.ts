import axios from 'axios';

export const client =
  axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL, // your endpoint
  headers: {
    "Access-Control-Allow-Origin" : process.env.VUE_APP_API_BASE_URL,
    "Access-Control-Allow-Private-Network": true,
    "Access-Control-Request-Private-Network" : true
  }
})

