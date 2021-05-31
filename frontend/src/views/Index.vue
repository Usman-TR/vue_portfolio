<template>
  <div class="home">
    <BookList v-bind:books=books
    v-bind:list_title=usernames_list
     />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import BookList from '@/components/BookList.vue'
// import api from '@/services/api'

export default {
  name: 'Index',
  components: {
    BookList
  },
  data: function () {
    return {
      books: this.$store.state.user.books
    }
  },
  computed: {
    usernames_list () {
      return this.$store.state.user.username + '\'s books'
    }
  }

}
</script>
