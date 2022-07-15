<template>
    <div class="book-list-container">
        <div class="list_header">
          <h3>{{  list_title  }}</h3>
          <h4 class="sub_title" v-if="sub_title">{{  sub_title  }}</h4>
          <p class="list_toogle" v-on:click="this.show_full = !this.show_full"><span v-if="!this.show_full">Показать все</span><span v-else>Показать меньше</span> </p>
        </div>
        <div v-if="show_full" class="cards-container">
              <MDBCard style="width: 18rem" v-for="book in books" :key="book.title" v-on:click="showBookPage(book)">
                <MDBCardImg v-if="book.preview" top v-bind:src=book.preview class="img-fluid" />
                <img v-else top alt="Vue logo" src="../assets/default-book.png">
                <MDBCardBody>
                <MDBCardTitle>{{  cutText(book.title)  }}</MDBCardTitle>
                <MDBCardText>
                  <span v-if="book.description">
                    {{  cutText(book.description)  }}
                  </span>
                </MDBCardText>
                </MDBCardBody>
                <MDBCardText>
                  <span v-if="book.authors">
                  {{  formateAuthors(book.authors)  }}
                  </span>
                  </MDBCardText>
                <!-- <MDBCardFooter class="text-muted text-muted-DB"> -->
                  <!-- <MDBCardLink v-bind:href=createPreviewLink(book.GoogleId)>Перейти</MDBCardLink> -->
                  <!-- <MDBCardLink v-on:click="addBook(getBookSaveData(book))">Добавить</MDBCardLink> -->
                <!-- </MDBCardFooter> -->
            </MDBCard>
        </div>
        <div :id="list_id" v-if="!show_full" class="carousel carousel-dark slide" data-bs-ride="carousel">
  <div class="carousel-indicators">
    <button type="button" :data-bs-target="'#' + list_id" :data-bs-slide-to="idx" aria-label="" v-for="(book, idx) in limitItems(books)" :key="book.title" :class="{ active: idx==0 }"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item" data-bs-interval="5000"
      v-on:click="showBookPage(book)"
      v-for="(book, idx) in limitItems(books)"
      :key="book.title"
      :class="{ active: idx==0 }"
      >
      <img v-if="book.preview" top v-bind:src=book.preview class="img-fluid" />
      <img v-else top alt="Vue logo" src="../assets/default-book.png">
      <div class="carousel-caption-custom">
        <h5>{{cutText(book.title)}}</h5>
        <p v-if="book.description">{{  cutText(book.description)  }}</p>
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
<BookPage :book="active_book" v-if="BookPageActive" @hideBookPage="hideBookPage()" :isInUserBooks="userBookIds.includes(active_book.GoogleId)" />
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
    sub_title: String,
    userBookIds: Object
  },
  data: function () {
    return {
      show_full: false,
      active_book: {},
      BookPageActive: false
    }
  },
  components: {
    MDBCard,
    MDBCardBody,
    MDBCardTitle,
    MDBCardText,
    MDBCardImg,
    BookPage
  },
  methods: {
    limitItems (items, maxNum = 15) {
      return items.slice(0, maxNum)
    },
    checkKnowledge (bookId) {
      const expert = prompt('Введите логин эксперта')
      bookService.addMarkRequest(this.$store.state.user.username, bookId, expert).then((res) => alert('Отправлено'))
    },
    getImage (path) {
      return path
    },
    showBookPage (book) {
      this.active_book = book
      console.log(book)
      this.BookPageActive = true
    },
    hideBookPage () {
      this.active_book = {}
      this.BookPageActive = false
    },
    formateAuthors (authors) {
      return authors.replaceAll('[', '').replaceAll(']', '').replaceAll('\'', '')
    },
    createPreviewLink (id) {
      return 'https://books.google.ru/books?id=' + id
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
      console.log(book)
      console.log(book.preview)
      const GoogleId = this.getUrlVars(book.preview).id
      // title
      const title = book.title

      const description = book.description
      const authors = book.authors
      const preview = book.imageLink
      const language = book.language
      const publishedDate = book.publishedDate.slice(0, 4)
      const publisher = book.publisher
      console.log(GoogleId, ISBN, title)

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
.book-list-container{
    width: 100%;
    position: relative;
}
.book-item{
    text-align: center;
}
.cards-container{
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
    gap: 40px;
    margin: 20px 30px;
}
.cards-container img{
  object-fit: cover;
  width: 100%;
  height: 250px;
  max-height: 300px;
}
.carousel-item {
  height: 200px;
}
.carousel-item img{
  height: 150px;
  position: absolute;
  top: 10px;
  left: 10px;
  max-width: 40%;
}
.carousel-caption-custom {
  display: block;
  position: absolute;
  top: 10px;
  left: 40%;
}
.carousel-caption-custom h5{
  font-weight: 500;
  font-size: 14px;
  line-height: 18px;
  display: flex;
  align-items: center;
  letter-spacing: 0.1px;
  text-align: left;

}
.carousel-caption-custom p {
  font-weight: 400;
  font-size: 12px;
  line-height: 16px;
  display: flex;
  align-items: center;
  letter-spacing: 0.4px;
  color: rgba(60, 60, 67, 0.6);
  text-align: left;
}
.list_toogle {
  position: relative;
  top: 8px;
  right: 5px;
  font-size: 12px;
  line-height: 16px;

  display: flex;
  align-items: center;
  text-align: right;
  letter-spacing: 0.4px;
  color: #835ED2;
}
.list_header h3 {
  padding-left: 10px;
}
.list_header {
  display: flex;
  justify-content: space-between;
  flex-flow: row nowrap;
  align-items: flex-start;
  line-break: auto;
}

.sub_title {
  position: absolute;
  top: 25px;
  margin-bottom: 20px;
  left: 10px;
  font-size: 12px;
  line-height: 16px;
  display: flex;
  align-items: center;
  text-align: center;
  letter-spacing: 0.25px;
  color: rgba(60, 60, 67, 0.6);
}

.text-muted-DB {
  display: flex;
  justify-content: space-around;
  background: #fff !important;
}
.text-muted-DB > *{
  font-weight: 500;
  font-size: 11px;
  line-height: 11px;
  display: flex;
  align-items: center;
  text-align: center;
  letter-spacing: 0.75px;
  text-transform: uppercase;
  width: fit-content;
  color: #F2F2F7;
  background: #835ED2;
  box-shadow: 0px 24px 32px rgba(131, 94, 210, 0.24);
  border-radius: 10px;
  padding: 8px 16px;
  text-decoration: none;
}
.card {
  border: none !important;
  filter: drop-shadow(0px 4px 8px rgba(176, 65, 118, 0.26));
  padding-bottom: 16px;
}
</style>
