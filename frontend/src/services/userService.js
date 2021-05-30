import api from '@/services/api'

export default {
  fetchBooks () {
    return api.get('/users/admin/books/')
      .then(response => response.data)
  },
  postBook (payload) {
    return api.post('messages/', payload)
      .then(response => response.data)
  },
  deleteBook (msgId) {
    return api.delete('messages/{msgId}')
      .then(response => response.data)
  }
}
