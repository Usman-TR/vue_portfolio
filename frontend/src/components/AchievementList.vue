<template>
    <div class="achievement-list-container">
      <div class="list_header">
        <h3>Достижения</h3>
          <p class="list_toogle" @click="showFull = !showFull"><span v-if="!showFull">Показать все</span><span v-else>Показать меньше</span> </p>
        </div>
        <div class="cards-container achievement-list" :class="{'cards-container-row': !showFull}">
              <MDBCard :class="{'card-row': !showFull}" v-for="achievement in achievements" :key="achievement.title">
                <MDBCardImg v-if="achievement.image" top v-bind:src=achievement.image class="img-fluid" />
                <img v-else top alt="Vue logo" src="../assets/default-book.png">
                <MDBCardBody>
                  <MDBCardTitle class="card__title">{{  cutText(achievement.title, 40)  }}</MDBCardTitle>
                  <template v-if="showFull">
                      <MDBCardText>
                      <span>
                        {{  cutText(achievement.description, 50) }}
                      </span>
                    </MDBCardText>
                    <MDBCardText>
                    <p>Книги:</p>
                    <ul>
                      <li v-for="book in achievement.books" :key="book.id">
                      {{ cutText(book.title, 40) }}
                      </li>
                    </ul>

                    </MDBCardText>
                  </template>
                </MDBCardBody>
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
  data () {
    return {
      showFull: false
    }
  },
  methods: {
    cutText (str, len) {
      try {
        if (str.length > len) {
          return str.slice(0, len) + '...'
        } else {
          return str
        }
      } catch (error) {
        console.log(error)
      }
      return ''
    },
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

.cards-container{
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
    gap: 40px 10px;
    margin: 20px 0;
    padding-inline: 30px;
}
.cards-container-row {
  flex-flow: row wrap;
  overflow-y: hidden;
  padding-top: 10px;
  padding-bottom: 20px;
  max-height: 230px;
}
.card-row {
  width: 120px;
  padding-bottom: 0;
  background: none;

}
.card-row .img-fluid {
  width: 120px;
  height: 120px;
}
.card-row .card-body {
  padding: 0;
}
.card-row .card__title {
  font-size: 1rem;
  margin-bottom: 0;
  padding: 0.5rem 0;
}
.cards-container img{
  object-fit: cover;
  width: 100%;
  height: 100%;
}
</style>
