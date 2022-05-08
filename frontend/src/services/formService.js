import api from '@/services/api'
// import Cookies from 'js-cookie'

export default {
  getProfiles () {
    return api.get('/api/v1/users/profiles')
  },
  getUniversities () {
    return api.get('/api/v1/users/universities')
  },
  updateProfile (username, payload) {
    return api.post(`/api/v1/users/${username}/update`, payload)
  }
}
