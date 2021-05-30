<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
<!--    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <BookList v-bind:books=books
    list_title="List title"
     />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import BookList from '@/components/BookList.vue'
import api from '@/services/api'

export default {
  name: 'Index',
  components: {
    BookList
  },
  data: function () {
    return {
      books: {}
    }
  },
  computed: {
  },
  mounted () {
    api
      .get('/users/admin/books/')
      .then(response => {
        this.books = response.data
        console.log(response.data)
        console.log('working here')
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>
