<template>
  <div class="home">
    <div>
       <input v-model.lazy="searchSeq" placeholder='Поиск книг'>
       <button v-on:click="search_books(searchSeq)">Поиск книг</button>
       <BookList v-bind:books=searchedBooks
          v-bind:list_title=searchSeq
          />
     </div>
    <BookList v-bind:books=books
    v-bind:list_title=usernames_list
     />
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
      books: this.$store.state.user.books,
      searchSeq: '',
      searchedBooks: ''
    }
  },
  beforeCreate: function () {
    this.$store.dispatch('getUser')
    this.books = this.$store.state.user.books
  },
  computed: {
    usernames_list () {
      return this.$store.state.user.username + '\'s books'
    }
  },
  methods: {
    async search_books (text) {
      console.log(self.name)
      const searchSeq = String(text).replaceAll('  ', ' ').replaceAll(' ', '+')
      const url = 'https://www.googleapis.com/books/v1/volumes?q='
      const response = await fetch(url + searchSeq)
      if (response.ok) {
        const json = await response.json()
        const volume = json.items
        const exportBooks = []
        volume.forEach(element => {
          const title = element.volumeInfo.title
          const authors = element.volumeInfo.authors
          const description = element.volumeInfo.description
          const publishedDate = element.volumeInfo.publishedDate
          const previewLink = element.volumeInfo.previewLink
          const language = element.volumeInfo.language
          const canonicalVolumeLink = element.volumeInfo.canonicalVolumeLink
          let imageLink = element.volumeInfo.imageLinks.thumbnail
          if (typeof (imageLink) === 'undefined') {
            imageLink = false
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
        this.searchedBooks = exportBooks
        console.log(this.searchedBooks)
      } else {
        console.log('Ошибка HTTP: ' + response.status)
      }
    }
  }
}
</script>
