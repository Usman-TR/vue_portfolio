<template>
  <div class="home">
    <div>
       <input v-model.lazy="searchSeq" placeholder='Поисковой запрос'>
       <button v-on:click="search_books({ text: searchSeq })">Найти</button>
       <BookList v-bind:books=searchedBooks
          v-bind:list_title=searchSeq
          />
     </div>
  </div>
</template>

<script>
import BookList from '@/components/BookList.vue'
import bookService from '../services/bookService'

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
      const url = 'https://www.googleapis.com/books/v1/volumes?q='
      const params = '&maxResults=40&startIndex=1'
      if (text) {
        const searchSeq = String(text).replaceAll('  ', ' ').replaceAll(' ', '+')
        const response = await fetch(url + searchSeq + params)
        if (response.ok) {
          const json = await response.json()
          console.log(json)
          const volume = json.items
          const exportBooks = bookService.parse_volume(volume)
          this.searchedBooks = exportBooks
          // return exportBooks
        } else {
          console.log('Ошибка HTTP: ' + response.status)
        }
      }
    }
  }
}
</script>
