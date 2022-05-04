// import api from '@/services/api'
// import Cookies from 'js-cookie'

export default {
  parseISBN: async function (isbn) {
    const url = 'https://www.googleapis.com/books/v1/volumes?q='
    const searchSeq = 'isbn:' + isbn
    console.log('searchSeq', searchSeq)
    const response = await fetch(url + searchSeq)
    if (response.ok) {
      const json = await response.json()
      console.log(json)
      const volume = json.items
      // console.log(element)
      const exportBooks = this.parse_volume(volume)
      // this.books = exportBooks
      console.log('exportBooks:', exportBooks)
      return exportBooks
    } else {
      console.log('Ошибка HTTP: ' + response.status)
    }
  },
  parse_volume (volume) {
    const exportBooks = []
    volume.forEach(element => {
      const title = element.volumeInfo.title
      const authors = element.volumeInfo.authors
      const description = element.volumeInfo.description
      const publishedDate = element.volumeInfo.publishedDate
      const previewLink = element.volumeInfo.previewLink
      const language = element.volumeInfo.language
      const canonicalVolumeLink = element.volumeInfo.canonicalVolumeLink
      let imageLink = false
      if (typeof (element.volumeInfo.imageLinks) === 'object') {
        if (typeof (element.volumeInfo.imageLinks.thumbnail) === 'string') {
          imageLink = element.volumeInfo.imageLinks.thumbnail
        } else if (typeof (element.volumeInfo.imageLinks.smallThumbnail) === 'string') {
          imageLink = element.volumeInfo.imageLinks.smallThumbnail
        }
      }
      exportBooks.push({
        title: title,
        authors: authors,
        description: description,
        publishedDate: publishedDate,
        previewLink: previewLink,
        language: language,
        canonicalVolumeLink: canonicalVolumeLink,
        imageLink: imageLink
      })
    })
    return exportBooks
  },
  async search_books (obj) {
    const text = obj.text
    const isbn = obj.isbn
    const url = 'https://www.googleapis.com/books/v1/volumes?q='
    console.log('search_books 1')
    if (text) {
      const searchSeq = String(text).replaceAll('  ', ' ').replaceAll(' ', '+')
      const response = await fetch(url + searchSeq)
      if (response.ok) {
        const json = await response.json()
        console.log(json)
        const volume = json.items
        const exportBooks = this.parse_volume(volume)
        // this.searchedBooks = exportBooks
        console.log('search_books 2')
        return exportBooks
      } else {
        console.log('Ошибка HTTP: ' + response.status)
      }
    } else if (isbn) {
      const searchSeq = 'isbn:' + isbn
      const response = await fetch(url + searchSeq)
      if (response.ok) {
        const json = await response.json()
        console.log(json)
        const volume = json.items
        const exportBooks = this.parse_volume(volume)
        // this.books = exportBooks
        console.log('search_books 3')
        return exportBooks
      } else {
        console.log('Ошибка HTTP: ' + response.status)
      }
    }
  }
}
