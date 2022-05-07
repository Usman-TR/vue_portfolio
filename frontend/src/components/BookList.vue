<template>
    <div class="book-list-container">
        <h3>{{  list_title  }}</h3>
        <div class="cards-container">
              <MDBCard style="width: 18rem" v-for="book in books" :key="book.title">
                <MDBCardImg v-if="book.imageLink" top v-bind:src=getImage(book.imageLink) class="img-fluid" />
                <img v-else top alt="Vue logo" src="../assets/default-book.png">
                <MDBCardBody>
                <MDBCardTitle>{{  book.title  }}</MDBCardTitle>
                <MDBCardText>
                  <span v-if="book.description">
                    {{  cutText(book.description)  }}
                  </span>
                </MDBCardText>
                </MDBCardBody>
                <MDBCardText>
                  <span v-if="book.authors">
                  {{  book.authors.join(", ")  }}
                  </span>
                  </MDBCardText>
                <MDBCardFooter class="text-muted">
                  <MDBCardLink v-bind:href=book.previewLink>Перейти</MDBCardLink>
                  <MDBCardLink v-on:click="addBook(getBookSaveData(book))">Добавить</MDBCardLink>
                  <MDBCardLink v-on:click="checkKnowledge(getBookSaveData(book).GoogleId)">Получить оценку</MDBCardLink>
                </MDBCardFooter>
            </MDBCard>
        </div>
    </div>
</template>

<script>
import { MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardLink, MDBCardImg, MDBCardFooter } from 'mdb-vue-ui-kit'
import bookService from '@/services/bookService.js'

export default {
  name: 'BookList',
  props: {
    books: Object,
    list_title: String,
    add_books_button: Boolean
  },
  components: {
    MDBCard,
    MDBCardBody,
    MDBCardTitle,
    MDBCardText,
    MDBCardLink,
    MDBCardImg,
    MDBCardFooter
  },
  methods: {
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
        console.log('cant find ISBN')
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
      console.log(GoogleId, ISBN, title)

      return { GoogleId: GoogleId, ISBN: ISBN, title: title }
    },
    addBook (GoogleId, ISBN, title) {
      const username = this.$store.state.user.username
      bookService.addBook(username, GoogleId, ISBN, title).then((result) => {
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
      console.log(outputList)
      return outputList
    }
  }
}
</script>

<style>
.book-list-container{
    width: 100%;
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
</style>
