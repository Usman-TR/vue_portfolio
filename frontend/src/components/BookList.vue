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
                  <MDBCardLink v-if="getIndustryId(book.industryIdentifiers)!= ''" v-on:click="addBook(getIndustryId(book.industryIdentifiers))">Добавить</MDBCardLink>
                  <MDBCardLink v-on:click="checkKnowledge(getIndustryId(book.industryIdentifiers))">Проверить усвоение</MDBCardLink>
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
      let expert = prompt("Введите логин эксперта")
      bookService.addMarkRequest(this.$store.state.user.username, bookId, expert).then((res) => alert("Отправлено"))
    },
    getImage (path) {
      return path
    },
    cutText (str) {
      return str.slice(0, 100) + '...'
    },
    getIndustryId (arr) {
      if (arr[0].identifier) {
        return arr[0].identifier
      } else {
        return ''
      }
    },
    addBook (isbn) {
      const username = this.$store.state.user.username
      bookService.addBook(username, isbn).then((result) => {
        if (result.status === 200) {

        }
      })
    },
    parsed_books (books) {
      const outputList = []
      books.forEach(element => {
        // console.log(element.ISBN)
        fetch('https://www.googleapis.com/books/v1/volumes?q=isbn:' + element.ISBN)
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
