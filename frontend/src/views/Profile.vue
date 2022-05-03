<template>
  <div class="Profile">
    <span v-if="this.$store.state.user.authentificated">
      <a @click="logout">Logout</a>
      <p @click="editProfile">Редактировать</p>
      <ProfileContainer v-bind:user=user v-if="!editIsActive" />
      <EditProfileContainer v-bind:user=user v-else />
      <BookList v-bind:books=getParsedBooks(books) v-bind:list_title=usernames_list />
      books: {{  books[0]  }} <br>
      {{  this.$store.state.userbooks.books  }}
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
export default {
  name: 'Profile',
  data: function () {
    return {
      editIsActive: false
    }
  },
  computed: mapState({
    user: state => state.user,
    usernames_list: () => 'Ваша коллекция',
    books: state => state.user.books,
    auth_status: state => state.authStatus,
  }),
  beforeCreate: function () {
    this.$store.dispatch('getUser')
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
    logout: function () {
      this.$store.dispatch('logout')
        .then(() => {
          // this.$store.commit('setUser')
          this.$router.push('/login')
        })
        .catch(err => console.log(err))
    },
    getParsedBooks: function (books) {
      if (books) {
        books.forEach(element => {
          this.parseISBN(element.ISBN)
        })
      }
    },
    parseISBN: async function (isbn) {
      const url = 'https://www.googleapis.com/books/v1/volumes?q='
      const searchSeq = 'isbn:' + isbn
      const response = await fetch(url + searchSeq)
      if (response.ok) {
        const json = await response.json()
        console.log(json)
        // const volume = json.items
        // element = volume
        // console.log(element)
        // const exportBooks = this.parse_volume(volume)
        // this.books = exportBooks
        // return exportBooks
      } else {
        console.log('Ошибка HTTP: ' + response.status)
      }
    }
  }
}
</script>
