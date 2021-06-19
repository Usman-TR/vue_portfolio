import api from '@/services/api'
import Cookies from 'js-cookie'

export default {
  fetchUser (username) {
    return api.get(`/api/v1/users//${username}`)
      .then(response => response.data)
  },
  login (user) {
    return api.post('/api/v1/users/login/', user,
      {
        headers:
        {
          'Content-Type': 'application/json',
          'X-CSRFToken': Cookies.get('csrftoken')
        }
      })
      .then(response => response.data)
  },
  register (user) {
    return api.post('/api/v1/users/registration/', user)
      .then(response => response.data)
  },
  getUserBooks (username) {
    return api.get(`/api/v1/users/${username}/books/`)
      .then(response => response.data)
  },
  deleteBook (username, bookId) {
    return api.delete(`/users/${username}/${bookId}`)
      .then(response => response.data)
  }
}
