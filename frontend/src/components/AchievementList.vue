<template>
    <div class="achievement-list-container">
        <h3>Достижения</h3>
        <div class="cards-container">
              <MDBCard style="width: 18rem" v-for="achievement in achievements" :key="achievement.title">
                <MDBCardImg v-if="achievement.image" top v-bind:src=achievement.image class="img-fluid" />
                <img v-else top alt="Vue logo" src="../assets/default-book.png">
                <MDBCardBody>
                <MDBCardTitle>{{  achievement.title  }}</MDBCardTitle>
                <MDBCardText>
                  <span>
                    {{  achievement.description }}
                  </span>
                </MDBCardText>
                </MDBCardBody>
                <MDBCardText>
                  <p>Книги</p>
                  <p v-for="book in achievement.books" :key="book.id">
                    {{book.title}}
                  </p>
                  </MDBCardText>
            </MDBCard>
        </div>
    </div>
</template>

<script>
import { MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImg } from 'mdb-vue-ui-kit'

export default {
  name: 'AchievementList',
  props: {
    achievements: Object
  },
  components: {
    MDBCard,
    MDBCardBody,
    MDBCardTitle,
    MDBCardText,
    MDBCardImg
  },
  methods: {
    getImage (path) {
      return path
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
.card {
  padding-bottom: 16px;
}
</style>
