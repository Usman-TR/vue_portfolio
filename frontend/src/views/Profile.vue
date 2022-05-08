<template>
  <div class="Profile">
    <span v-if="this.$store.state.user.authentificated">
      <a @click="logout">Logout</a>
      <p @click="editProfile">Редактировать</p>
      <p>Прогресс {{progress}}%</p>
      <div class="profressBarFull">
        <p :class="'profressBar'" v-bind:style="{ width: progress + '%' }"><span class="progressLabel">{{progress}}%</span></p>
      </div>
      <ProfileContainer v-bind:user=user v-if="!editIsActive" />
      <EditProfileContainer v-bind:user=user v-else />
      <div>
        <button v-on:click="getExperts()">Все эксперты</button>
        <div v-if="this.experts.length != 0">{{this.experts}}</div>
      </div>
      <BookListParser v-bind:books=getMarkedBookList() v-bind:list_title='marked_list_title' />
      <BookListParser v-bind:books=getUnMarkedBookList() v-bind:list_title=usernames_list />
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
import BookListParser from '@/components/BookListParser.vue'
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
      experts: [],
      progress: 0
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
    this.get_progress()
  },
  components: {
    BookListParser,
    ProfileContainer,
    EditProfileContainer
  },
  methods: {
    get_progress () {
      bookService.getProgress(this.$store.state.user.username)
        .then((res) => {
          this.progress = res.data.progress * 100
        })
    },
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
<style>
.profressBarFull {
  height: 20px;
  width: 60vw;
  position: relative;
  left: 20vw;
  border-radius: 15px;
  background-color: rgb(192, 157, 157);
  text-align: right;
  color: #fff;
}
.profressBar {
  /* border: 3px solid red; */
  background-color: rgb(149, 193, 153);
  position: relative;
  left: -3px;
  height: 20px;
  border-radius: 15px;
}
.progressLabel{
  position: relative;
  left: -10px;
  top: -2px;
}
</style>
