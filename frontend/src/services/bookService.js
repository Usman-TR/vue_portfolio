import api from '@/services/api'
// import Cookies from 'js-cookie'

export default {
  parseGoogleId: async function (GoogleId) {
    const url = 'https://www.googleapis.com/books/v1/volumes/'
    const searchSeq = GoogleId

    const response = await fetch(url + searchSeq)
    const volume = await response.json()

    const exportBooks = this.parse_volume([volume])
    return exportBooks
  },
  parse_volume (volume) {
    const exportBooks = []

    volume.forEach(element => {
      try {
        const title = element.volumeInfo.title
        const authors = element.volumeInfo.authors
        const description = element.volumeInfo.description
        const publishedDate = element.volumeInfo.publishedDate
        const publisher = element.volumeInfo.publisher
        const previewLink = element.volumeInfo.previewLink
        const language = element.volumeInfo.language
        const canonicalVolumeLink = element.volumeInfo.canonicalVolumeLink
        const industryIdentifiers = element.volumeInfo.industryIdentifiers
        let imageLink = false
        if (typeof (element.volumeInfo.imageLinks) === 'object') {
          if (typeof (element.volumeInfo.imageLinks.thumbnail) === 'string') {
            imageLink = element.volumeInfo.imageLinks.thumbnail
          } else if (typeof (element.volumeInfo.imageLinks.smallThumbnail) === 'string') {
            imageLink = element.volumeInfo.imageLinks.smallThumbnail
          }
        }
        exportBooks.push({
          title,
          authors,
          description,
          publishedDate,
          publisher,
          previewLink,
          language,
          canonicalVolumeLink,
          imageLink,
          industryIdentifiers
        })
      } catch (error) {
        console.log('cant load book', error)
        return exportBooks
      }
    })
    return exportBooks
  },
  addBookGet (username, GoogleId) {
    return api.get(`/api/v1/users/${username}/books/add/${GoogleId}`)
  },
  addBook (username, data) {
    console.log(data)
    return api.post(`/api/v1/users/${username}/books/add/`, {
      GoogleId: data.GoogleId,
      ISBN: data.ISBN,
      title: data.title,
      authors: data.authors,
      description: data.description,
      preview: data.preview,
      language: data.language,
      publisher: data.publisher,
      publishedDate: data.publishedDate
    })
  },
  addProfile (data) {
    return api.post('api/v1/users/profiles/add', {
      title: data.title,
      description: data.description,
      achievements: data.achievements
    })
  },
  addAchievement (data) {
    const formData = new FormData()
    formData.append('file', data.file)
    formData.append('title', data.title)
    formData.append('description', data.description)
    formData.append('books', JSON.stringify(data.books))

    return api.post('api/v1/users/achievements/add', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
  },
  addMarkRequest (username, GoogleId, expert) {
    return api.get(`/api/v1/users/${username}/request/${expert}/${GoogleId}`)
  },
  cancelMarkRequest (username, GoogleId, expert) {
    return api.get(`/api/v1/users/${username}/cancelrequest/${expert}/${GoogleId}`)
  },
  setMark (requestId, username, rating) {
    return api.get(`/api/v1/users/${username}/evaluate/${requestId}/${rating}`)
  },
  getRequests (username) {
    return api.get(`/api/v1/users/${username}/requests`)
  },
  getExperts () {
    return api.get('/api/v1/users/experts')
  },
  getProgress (username) {
    return api.get(`/api/v1/users/${username}/progress`)
  },
  getAllAchievements () {
    return api.get('/api/v1/users/achievements')
  },
  getUserAchievements (username) {
    return api.get(`/api/v1/users/${username}/achievements`)
  },
  getProfiles () {
    return api.get('/api/v1/users/profiles')
  },
  getProfileBooks (profileId) {
    return api.get(`/api/v1/users/profiles/${profileId}/books`)
  },
  getRecomendationBooks () {
    return api.get('/api/v1/users/recomendation')
  },
  getPopularBooks () {
    return api.get('/api/v1/users/popular')
  }
}
