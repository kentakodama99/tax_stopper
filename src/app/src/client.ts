import axios from 'axios';

export const client =
  axios.create({
  baseURL: '', // your endpoint
})