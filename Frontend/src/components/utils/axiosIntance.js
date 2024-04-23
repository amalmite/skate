import axios from 'axios';

// const baseURL = 'http://127.0.0.1:8000/';
const baseURL = 'https://devv.pythonanywhere.com/'
// const token = localStorage.getItem('tokens');
// const t=JSON.parse(token)
// console.log(t.access);

const axiosInstance = axios.create({
  baseURL,
  headers: {
    // Authorization: t ? `Bearer ${t.access}` : null,
  },
});

export default axiosInstance;
