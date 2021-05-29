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

export default {
  name: 'Index',
  components: {
    BookList
  },
  data: function () {
    return {
      books_data: [
        { title: 'something nice to say', author: 'good boy' },
        { title: 'something nice to say again', author: 'bad boy' }]
    }
  },
  computed: {
    books () {
      return [
        { title: 'something nice to say', author: 'good boy' },
        { title: 'something nice to say again', author: 'bad boy' }
      ]
    }
  }
}
</script>
