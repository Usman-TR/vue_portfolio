<template>
  <div class="home">
    <div>
       <input v-model.lazy="searchSeq" placeholder='Поисковой запрос'>
       <button v-on:click="search_books({ text: searchSeq })">Найти</button>
       <BookListParser v-bind:books=searchedBooks
          v-bind:list_title=searchTitle
          />
       <BookListDB v-bind:books=profileBooks
          v-bind:list_title="'Книги по специальности ' + this.$store.state.user.profile[0].title"
          />
     </div>
  </div>
</template>

<script>
import BookListParser from '@/components/BookListParser.vue'
import BookListDB from '@/components/BookListDB.vue'
import bookService from '@/services/bookService.js'

export default {
  name: 'Index',
  components: {
    BookListParser,
    BookListDB
  },
  data: function () {
    return {
      books: this.$store.getters.books,
      searchSeq: '',
      searchedBooks: [],
      profileBooks: []
    }
  },
  beforeCreate: function () {
    this.$store.dispatch('userbooks/getBooks', this.$store.state.user.username)
  },
  mounted () {
    this.loadProfileBooks()
  },
  computed: {
    usernames_list () {
      return this.$store.state.user.username + '\'s books'
    },
    searchTitle () {
      if (this.searchSeq === '') {
        return ''
      } else {
        return 'Результаты поиска по запросу "' + this.searchSeq + '"'
      }
    }
  },
  methods: {
    async search_books (obj) {
      const text = obj.text
      const url = 'https://www.googleapis.com/books/v1/volumes?q='
      const params = '&maxResults=12&startIndex=1'
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
    },
    async loadProfileBooks () {
      const profileId = this.$store.state.user.profile[0].id
      console.log('profileId', profileId)
      bookService.getProfileBooks(profileId)
        .then((res) => {
          this.profileBooks = res.data.books
          console.log(res)
        })
    }
  }
}
</script>
