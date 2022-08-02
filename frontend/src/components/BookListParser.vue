<template>
  <div class="book-list-container">
    <div class="list_header">
      <h3>{{ list_title }}</h3>
      <p class="list_toogle" v-if="books.length" v-on:click="this.show_full = !this.show_full"><span
          v-if="!this.show_full">Показать
          все</span><span v-else>Показать меньше</span> </p>
    </div>

    <div v-if="show_full && books.length" class="cards-container">
      <p v-if="!books.length">Нет книг</p>
      <MDBCard style="width: 18rem" v-for="(book, idx) in books" :key="'card' + idx + book.title"
        v-on:click="showBookPage(book)">
        <MDBCardImg v-if="book.imageLink" top v-bind:src=getImage(book.imageLink) class="img-fluid" />
        <img v-else top alt="Vue logo" src="../assets/default-book.png">
        <MDBCardBody>
          <MDBCardTitle>{{ book.title }}</MDBCardTitle>
          <MDBCardText>
            <span v-if="book.description">
              {{ cutText(book.description) }}
            </span>
          </MDBCardText>
        </MDBCardBody>
        <MDBCardText>
          <span v-if="book.authors">
            {{ book.authors.join(", ") }}
          </span>
        </MDBCardText>
        <!-- <MDBCardFooter class="text-muted"> -->
        <!-- <MDBCardLink v-bind:href=book.previewLink>Перейти</MDBCardLink> -->
        <!-- <MDBCardLink v-on:click="addBook(getBookSaveData(book))">Добавить {{getBookSaveData(book).GoogleId}}</MDBCardLink> -->
        <!-- <MDBCardLink v-on:click="checkKnowledge(getBookSaveData(book).GoogleId)">Получить оценку</MDBCardLink> -->
        <!-- </MDBCardFooter> -->
      </MDBCard>
      <div class="pagination_parser">
        <span v-if="page > 1" v-on:click="this.changePage(0)">
          <svg width="12" height="22" viewBox="0 0 12 22" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M11 21L1 11L11 1" stroke="#835ED2" stroke-width="2" stroke-linecap="round"
              stroke-linejoin="round" />
          </svg>
          <svg width="12" height="22" viewBox="0 0 12 22" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M11 21L1 11L11 1" stroke="#835ED2" stroke-width="2" stroke-linecap="round"
              stroke-linejoin="round" />
          </svg>

        </span>
        <span v-if="page > 0" v-on:click="this.changePage(page - 1)">
          <svg width="12" height="22" viewBox="0 0 12 22" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M11 21L1 11L11 1" stroke="#835ED2" stroke-width="2" stroke-linecap="round"
              stroke-linejoin="round" />
          </svg>

        </span>
        <span v-if="!isNaN(page)">{{ page }}{{ page + 1 }}</span>
        <span v-if="books.length > maxBooksPerPage" v-on:click="this.changePage(page + 1)">
          <svg width="12" height="22" viewBox="0 0 12 22" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M1 1L11 11L1 21" stroke="#835ED2" stroke-width="2" stroke-linecap="round"
              stroke-linejoin="round" />
          </svg>
        </span>
      </div>
    </div>
    <div :id="list_id" v-if="!show_full && books.length" class="carousel carousel-dark slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" :data-bs-target="'#' + list_id" :data-bs-slide-to="idx" aria-label=""
          v-for="(book, idx) in limitItems(books)" :key="'slider' + book.title" :class="{ active: idx == 0 }"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item" data-bs-interval="5000" v-on:click="showBookPage(book)"
          v-for="(book, idx) in limitItems(books)" :key="'slider' + book.title" :class="{ active: idx == 0 }">
          <img v-if="book.imageLink" top v-bind:src="getImage(book.imageLink)" class="img-fluid" />
          <img v-else top alt="Vue logo" src="../assets/default-book.png">
          <div class="carousel-caption-custom">
            <h5>{{ cutText(book.title) }}</h5>
            <p v-if="book.description">{{ cutText(book.description) }}</p>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" :data-bs-target="'#' + list_id" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" :data-bs-target="'#' + list_id" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <BookPage :book="active_book" v-if="BookPageActive" @hideBookPage="hideBookPage()"
      :isInUserBooks="userBookIds.includes(active_book.GoogleId)" />
  </div>
</template>

<script>
import { MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImg } from 'mdb-vue-ui-kit'
import bookService from '@/services/bookService.js'
import BookPage from '@/components/BookPage.vue'

export default {
  name: 'BookList',
  props: {
    books: Object,
    list_title: String,
    add_books_button: Boolean,
    list_id: String,
    maxBooksPerPage: Number,
    page: Number,
    userBookIds: Object
  },
  components: {
    MDBCard,
    MDBCardBody,
    MDBCardTitle,
    MDBCardText,
    MDBCardImg,
    BookPage
  },
  data: function () {
    return {
      show_full: false,
      active_book: {},
      BookPageActive: false
    }
  },
  methods: {
    changePage (page) {
      console.log('changePage', page)
      this.$emit('changePage', { page: page })
    },
    prepBookForPage (bookParsed) {
      console.log('***', bookParsed)
      const book = {
        authors: bookParsed.authors,
        description: bookParsed.description,
        title: bookParsed.title,
        preview: bookParsed.imageLink,
        language: bookParsed.language,
        publishedDate: bookParsed.publishedDate.slice(0, 4),
        publisher: bookParsed.publisher,
        GoogleId: this.getBookSaveData(bookParsed).GoogleId
      }
      return book
    },
    limitItems (items, maxNum = 6) {
      console.log(items)
      return items.slice(0, maxNum)
    },
    showBookPage (book) {
      this.active_book = this.prepBookForPage(book)
      this.BookPageActive = true
    },
    hideBookPage () {
      this.active_book = {}
      this.BookPageActive = false
    },
    checkKnowledge (bookId) {
      const expert = prompt('Введите логин эксперта')
      bookService.addMarkRequest(this.$store.state.user.username, bookId, expert).then((res) => alert('Отправлено'))
    },
    getImage (path) {
      return path
    },
    cutText (str) {
      return str.slice(0, 100) + '...'
    },
    getISBN (arr) {
      try {
        if (arr[0].identifier) {
          return arr[0].identifier
        }
      } catch (e) {
        return ''
      }
    },
    getUrlVars (location) {
      var vars = {}
      location.replace(/[?&]+([^=&]+)=([^&]*)/gi,
        function (m, key, value) {
          vars[key] = value
        })
      return vars
    },
    getBookSaveData (book) {
      // ISBN
      const ISBN = this.getISBN(book.industryIdentifiers)

      // etag
      const GoogleId = this.getUrlVars(book.previewLink).id
      // title
      const title = book.title

      const description = book.description
      const authors = book.authors
      const preview = book.imageLink
      const language = book.language
      const publishedDate = book.publishedDate.slice(0, 4)
      const publisher = book.publisher
      return { GoogleId, ISBN, title, preview, description, authors, language, publishedDate, publisher }
    },
    addBook (data) {
      const username = this.$store.state.user.username
      bookService.addBook(username, data).then((result) => {
        if (result.status === 200) {
          alert('добавлено')
        } else {
          alert('Ошибка', result)
        }
      })
    },
    parsed_books (books) {
      const outputList = []
      books.forEach(element => {
        fetch('https://www.googleapis.com/books/v1/volumes/' + element.GoogleId)
          .then(response => response.json())
          .then(result => {
            outputList.push({
              title: result.items[0].volumeInfo.title,
              imageLink: result.items[0].volumeInfo.imageLinks[0] || '#',
              description: result.items[0].volumeInfo.description,
              authors: result.items[0].volumeInfo.authors,
              previewLink: result.items[0].volumeInfo.previewLink || '#'
            })
          })
          .catch(error => console.log(error))
      })
      return outputList
    }
  }
}
</script>

<style>
.book-list-container {
  width: 100%;
}

.book-item {
  text-align: center;
}

.cards-container {
  display: flex;
  flex-flow: row wrap;
  justify-content: center;
  gap: 40px;
  margin: 20px 30px;
}

.cards-container img {
  object-fit: cover;
  width: 100%;
  height: 250px;
  max-height: 300px;
}

.pagination_parser {
  position: relative;
  display: flex;
  justify-content: space-around;
}

.pagination_parser span {
  margin: 0px 10px;
}

.card {
  border: none !important;
  filter: drop-shadow(0px 4px 8px rgba(176, 65, 118, 0.26));
  padding-bottom: 16px;

}
</style>
