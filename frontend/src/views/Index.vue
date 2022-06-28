<template>
  <div class="home">
    <div>
      <div class="search_container">
        <div class="search_icon">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M7.25 12.5C10.1495 12.5 12.5 10.1495 12.5 7.25C12.5 4.35051 10.1495 2 7.25 2C4.35051 2 2 4.35051 2 7.25C2 10.1495 4.35051 12.5 7.25 12.5Z" stroke="#B195EB" stroke-width="1.28" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M10.9622 10.9625L13.9997 14.0001" stroke="#B195EB" stroke-width="1.28" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        </div>
       <input v-model="searchSeq" placeholder='Название или автор' @input="search_books({ text: searchSeq, page: searchPage })">
       </div>
       <BookListParser v-if="searchTitle" v-bind:books=searchedBooks
          v-bind:list_title=searchTitle v-bind:list_id="'searchedListID6452'" v-bind:page=searchPage v-bind:maxBooksPerPage=12
          @changePage="(e) => { changePage(e.page)}"
          />
       <BookListDB v-if="profileBooks.length > 0" v-bind:books=profileBooks
          v-bind:list_title="'Специализация'" v-bind:list_id="'popularListID546'"
          />
        <BookListDB v-bind:books=recomendationBooks
          v-bind:list_title="'Рекомендации'" v-bind:sub_title="recomendationTitle" v-bind:list_id="'recomendationListID854'"
          />
        <BookListDB v-bind:books=popularBooks
          v-bind:list_title="'Популярные'" v-bind:list_id="'popularListID239'"
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
      searchPage: 0,
      searchedBooks: [],
      profileBooks: [],
      recomendationBooks: [],
      popularBooks: [],
      recomendationTitle: ''
    }
  },
  beforeCreate: function () {
    this.$store.dispatch('userbooks/getBooks', this.$store.state.user.username)
  },
  mounted () {
    this.loadProfileBooks()
    this.loadRecomendationBooks()
    this.loadPopularBooks()
  },
  computed: {
    usernames_list () {
      return this.$store.state.user.username + '\'s books'
    },
    searchTitle () {
      if (this.searchSeq === '') {
        return ''
      } else {
        return 'Поиск:"' + this.searchSeq + '"'
      }
    }
  },
  methods: {
    changePage (page) {
      this.searchPage = page
      this.search_books({ text: this.searchSeq, page: this.searchPage })
    },
    async search_books (obj) {
      const text = obj.text
      const url = 'https://www.googleapis.com/books/v1/volumes?q='
      const params = `&maxResults=25&startIndex=${obj.page * 15}`
      if (text) {
        const searchSeq = String(text).replaceAll('  ', ' ').replaceAll(' ', '+')
        const response = await fetch(url + searchSeq + params)
        if (response.ok) {
          const json = await response.json()
          const volume = json.items
          const exportBooks = bookService.parse_volume(volume)
          console.log('exportBooks', exportBooks.length, exportBooks)
          this.searchedBooks = exportBooks
          // return exportBooks
        } else {
          console.log(response)
        }
      }
    },
    async loadProfileBooks () {
      if (this.$store.state.user.authentificated) {
        const profileId = this.$store.state.user.profile[0].id
        bookService.getProfileBooks(profileId)
          .then((res) => {
            this.profileBooks = res.data.books
          })
      }
    },
    async loadRecomendationBooks () {
      bookService.getRecomendationBooks()
        .then((res) => {
          this.recomendationBooks = res.data.books
          this.recomendationTitle = res.data.title
        })
    },
    async loadPopularBooks () {
      bookService.getPopularBooks()
        .then((res) => {
          this.popularBooks = res.data.books
        })
    }
  }
}
</script>

<style scoped>
.search_container, input {
 background-color: #F5F0FF;
 outline: none;
 border: none;
 border-radius: 6px;
}
.search_container input {
  border-radius: 60px;
  color: #b295eb;
}
.search_container {
  margin: 20px 12px;
  display: flex;
  padding: 6px 12px;
}
.search_container ::placeholder {
  color: #b295ebb1;
}
.search_icon {
  position: relative;
  right: 3px;
}

</style>
