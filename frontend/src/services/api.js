import axios from 'axios'
import Cookies from 'js-cookie'

// const backendURL = process.env.VUE_APP_API_URL

const api = axios.create({
  baseURL: '/',
  timeout: 5000,
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': Cookies.get('csrftoken')
  }
})

api.interceptors.request.use(function (config) {
  const token = localStorage.getItem('token')
  config.headers.Authorization =  token ? `Token ${token}` : '';
  return config;
})

export default api
