<template>
    <div class="book-list-container">
        <h3>{{  list_title  }}</h3>
        <div class="cards-container">
            <MDBCard style="width: 18rem" v-for="book in books" :key="book.title" v-bind:books=books>
                <MDBCardImg top src="https://mdbootstrap.com/img/new/standard/city/062.jpg" alt="..."/>
                <MDBCardBody>
                <MDBCardTitle>{{  book.title  }}</MDBCardTitle>
                <MDBCardText>
                    {{  book.description  }}
                </MDBCardText>
                </MDBCardBody>
                <MDBCardText>Оценка: {{  book.my_rating  }}</MDBCardText><br>
                <MDBCardText>{{  book.authors  }}</MDBCardText>
                <MDBCardBody>
                <MDBCardLink href="#">Перейти</MDBCardLink>
                </MDBCardBody>
            </MDBCard>
        </div>
    </div>
</template>

<script>
import { MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardLink, MDBCardImg } from 'mdb-vue-ui-kit'

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
    MDBCardImg
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
</style>
