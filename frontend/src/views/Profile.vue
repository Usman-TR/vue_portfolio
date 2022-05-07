<template>
  <div class="Profile">
    <span v-if="this.$store.state.user.authentificated">
      <a @click="logout">Logout</a>
      <p @click="editProfile">Редактировать</p>
      <ProfileContainer v-bind:user=user v-if="!editIsActive" />
      <EditProfileContainer v-bind:user=user v-else />
      <div>
        <button v-on:click="getExperts()">Все эксперты</button>
        <div v-if="this.experts.length != 0">{{this.experts}}</div>
      </div>
      <BookList v-bind:books=getMarkedBookList() v-bind:list_title='marked_list_title' />
      <BookList v-bind:books=getUnMarkedBookList() v-bind:list_title=usernames_list />
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
import userService from '@/services/userService.js'

export default {
  name: 'Profile',
  data: function () {
    return {
      editIsActive: false,
      exportBooks: [],
      experts: []
    }
  },
  computed: mapState({
    user: state => state.user,
    usernames_list: () => 'Ваша коллекция',
    marked_list_title: () => 'Подтвержденная коллекция',
    books: state => state.user.books,
    auth_status: state => state.authStatus
  }),
  beforeCreate: function () {
    this.$store.dispatch('getUser')
    this.$store.dispatch('userbooks/getBooks')
  },
  mounted () {
    this.updateUserBooks(this.exportBooks)
  },
  components: {
    BookList,
    ProfileContainer,
    EditProfileContainer
  },
  methods: {
    getExperts () {
      bookService.getExperts()
        .then((res) => {
          this.experts = res.data.experts
        })
    },
    editProfile: function () {
      this.editIsActive = true
    },
    getMarkedBookList: function () {
      const markedBookList = []
      this.exportBooks.forEach(book => {
        if (book.marked) {
          markedBookList.push(book)
        }
      })
      return markedBookList
    },
    getUnMarkedBookList: function () {
      const markedBookList = []
      this.exportBooks.forEach(book => {
        if (!book.marked) {
          markedBookList.push(book)
        }
      })
      return markedBookList
    },
    updateUserBooks: async function (books) {
      // this.$store.dispatch('userbooks/getBooks')
      userService.getUserBooks(this.$store.state.user.username)
        .then((resp) => {
          resp.books.forEach(element => {
            bookService.parseGoogleId(element.GoogleId).then((pb) => {
              pb[0].marked = element.marked
              pb[0].mark = element.mark
              pb[0].expert = element.expert
              pb[0].rating = element.rating
              pb = pb[0]
              console.log(pb)
              this.exportBooks.push(pb)
            })
          })
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
