<template>
  <div class="Profile">
    <ProfileContainer v-bind:user=user />
    <BookList v-bind:books=books v-bind:list_title=usernames_list />
  </div>

</template>

<script>
// @ is an alias to /src
// import store from '@/store/'
import { mapState } from 'vuex'
import BookList from '@/components/BookList.vue'
import ProfileContainer from '@/components/ProfileContainer.vue'

export default {
  name: 'Profile',
  computed: mapState({
    user: state => state.user,
    usernames_list: () => 'Ваша коллекция',
    books: state => state.user.books
  }),
  created: function () {
    this.$store.dispatch('getUser')
  },
  components: {
    BookList,
    ProfileContainer
  }
}
</script>
