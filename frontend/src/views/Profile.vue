<template>
  <div class="Profile">
    <a v-if="this.$store.state.user.authentificated" @click="logout">Logout</a>
    <ProfileContainer v-bind:user=user />
    <BookList v-bind:books=books v-bind:list_title=usernames_list />
    {{  this.$store.state.user  }}
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
  beforeCreate: function () {
    this.$store.dispatch('getUser')
  },
  components: {
    BookList,
    ProfileContainer
  },
  methods: {
    logout: function () {
      this.$store.dispatch('logout')
        .then(() => {
          // this.$store.commit('setUser')
          this.$router.push('/login')
        })
        .catch(err => console.log(err))
    }
  }
}
</script>
