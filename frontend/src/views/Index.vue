<template>
  <div class="home">
    <div>
       <input v-model.lazy="searchSeq" placeholder='Поисковой запрос'>
       <button v-on:click="search_books({ text: searchSeq })">Найти</button>
       <BookList v-bind:books=searchedBooks
          v-bind:list_title=searchSeq
          />
     </div>
    <BookList v-if="this.$store.state.user.authentificated" v-bind:books=books
    v-bind:list_title=usernames_list
     />
     <div v-else>
       <router-link to="/login">Войдите в аккаунт</router-link>
     </div>
  </div>
</template>

<script>
import BookList from '@/components/BookList.vue'

export default {
  name: 'Index',
  components: {
    BookList
  },
  data: function () {
    return {
      books: this.$store.getters.books,
      searchSeq: '',
      searchedBooks: {}
    }
  },
  beforeCreate: function () {
    // this.$store.dispatch('getUser')
    this.$store.dispatch('userbooks/getBooks', this.$store.state.user.username)
  },
  computed: {
    usernames_list () {
      return this.$store.state.user.username + '\'s books'
    }
  },
  methods: {
    async search_books (obj) {
      const text = obj.text
      const isbn = obj.isbn
      const url = 'https://www.googleapis.com/books/v1/volumes?q='
      if (text) {
        const searchSeq = String(text).replaceAll('  ', ' ').replaceAll(' ', '+')
        const response = await fetch(url + searchSeq)
        if (response.ok) {
          const json = await response.json()
          console.log(json)
          const volume = json.items
          const exportBooks = this.parse_volume(volume)
          this.searchedBooks = exportBooks
          // return exportBooks
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
          this.books = exportBooks
          // return exportBooks
        } else {
          console.log('Ошибка HTTP: ' + response.status)
        }
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
    }
  }
}
</script>
