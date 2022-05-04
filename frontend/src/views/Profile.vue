<template>
  <div class="Profile">
    <span v-if="this.$store.state.user.authentificated">
      <a @click="logout">Logout</a>
      <p @click="editProfile">Редактировать</p>
      <ProfileContainer v-bind:user=user v-if="!editIsActive" />
      <EditProfileContainer v-bind:user=user v-else />
      <BookList v-bind:books=exportBooks v-bind:list_title=usernames_list />
    </span>
    <span v-else>
      <h1>Авторизуйтесь для доступа</h1>
    </span>
  </div>

</template>

<script>
// @ is an alias to /src
// import store from '@/store/'
import { mapState } from 'vuex'
import BookList from '@/components/BookList.vue'
import ProfileContainer from '@/components/ProfileContainer.vue'
import EditProfileContainer from '@/components/EditProfileContainer.vue'
import bookService from '@/services/bookService.js'
export default {
  name: 'Profile',
  data: function () {
    return {
      editIsActive: false,
      exportBooks: []

    }
  },
  computed: mapState({
    user: state => state.user,
    usernames_list: () => 'Ваша коллекция',
    books: state => state.user.books,
    auth_status: state => state.authStatus
  }),
  beforeCreate: function () {
    this.$store.dispatch('getUser')
  },
  mounted () {
    this.updateUserBooks(this.books)
  },
  components: {
    BookList,
    ProfileContainer,
    EditProfileContainer
  },
  methods: {
    editProfile: function () {
      this.editIsActive = true
    },
    updateUserBooks: async function (books) {
      books.forEach(element => {
        bookService.parseISBN(element.ISBN).then((pb) => this.exportBooks.push(pb[0]))
      })
    },
    logout: function () {
      this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/login')
        })
        .catch(err => console.log(err))
    }
  }
}
</script>
