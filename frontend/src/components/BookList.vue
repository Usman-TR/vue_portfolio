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
                    {{  book.description  }}
                </MDBCardText>
                </MDBCardBody>
                <MDBCardText>{{  book.authors  }}</MDBCardText>
                <MDBCardFooter class="text-muted">
                  <MDBCardLink v-bind:href=book.previewLink>Перейти</MDBCardLink>
                </MDBCardFooter>
            </MDBCard>
        </div>
    </div>
</template>

<script>
import { MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardLink, MDBCardImg, MDBCardFooter } from 'mdb-vue-ui-kit'

export default {
  name: 'BookList',
  props: {
    books: Object,
    list_title: String
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
    getImage (path) {
      return path
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
}
</style>
