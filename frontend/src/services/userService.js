import api from '@/services/api'

export default {
  fetchUser (username) {
    return api.get(`/users/${username}`)
      .then(response => response.data)
  },
  fetchBooks (username) {
    return api.get(`/users/${username}/books/`)
      .then(response => response.data)
  },
  postBook (payload) {
    return api.post(`/users/${payload.username}/books/`, payload)
      .then(response => response.data)
  },
  deleteBook (username, bookId) {
    return api.delete(`/users/${username}/${bookId}`)
      .then(response => response.data)
  }
}
