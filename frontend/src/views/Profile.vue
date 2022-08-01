<template>
  <div class="Profile">
    <span v-if="this.$store.state.user.authentificated">
      <div class="btn-group" v-if="!(editIsActive || addAchievementIsActive || addSpecIsActive)">
        <button class="btn btn-sm button_menu" type="button" data-bs-toggle="dropdown" aria-expanded="false">
          ...
        </button>
        <ul class="dropdown-menu">
          <li @click="editProfile">
            <svg width="24" height="25" viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M9 21.1827H4.5C4.30109 21.1827 4.11032 21.1037 3.96967 20.9631C3.82902 20.8224 3.75 20.6317 3.75 20.4327V16.2434C3.75 16.1449 3.7694 16.0474 3.80709 15.9564C3.84478 15.8654 3.90003 15.7827 3.96967 15.7131L15.2197 4.46308C15.3603 4.32243 15.5511 4.24341 15.75 4.24341C15.9489 4.24341 16.1397 4.32243 16.2803 4.46308L20.4697 8.65242C20.6103 8.79307 20.6893 8.98384 20.6893 9.18275C20.6893 9.38166 20.6103 9.57243 20.4697 9.71308L9 21.1827Z"
                stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M12.75 6.93274L18 12.1827" stroke="black" stroke-width="1.5" stroke-linecap="round"
                stroke-linejoin="round" />
            </svg>
            <span class="edit">Редактировать</span>
          </li>
          <li @click="addSpecIsActive = true" v-if="this.$store.state.user.admin">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M0.75 9L12 3L23.25 9L12 15L0.75 9Z" stroke="black" stroke-width="1.5" stroke-linecap="round"
                stroke-linejoin="round" />
              <path d="M17.625 22.5V12L12 9" stroke="black" stroke-width="1.5" stroke-linecap="round"
                stroke-linejoin="round" />
              <path
                d="M20.625 10.4V15.5114C20.6253 15.6731 20.573 15.8307 20.476 15.9601C19.8444 16.8005 17.18 19.875 12 19.875C6.82004 19.875 4.15558 16.8005 3.52402 15.9601C3.42699 15.8307 3.37469 15.6731 3.375 15.5114V10.4"
                stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
            <span class="spec">Добавить специализацию</span>
          </li>
          <li @click="addAchievementIsActive = true" v-if="this.$store.state.user.admin">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M11.9995 16.5C16.1416 16.5 19.4995 13.1421 19.4995 9C19.4995 4.85786 16.1416 1.5 11.9995 1.5C7.85732 1.5 4.49945 4.85786 4.49945 9C4.49945 13.1421 7.85732 16.5 11.9995 16.5Z"
                stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
              <path
                d="M11.9995 13.5C14.4847 13.5 16.4995 11.4853 16.4995 9C16.4995 6.51472 14.4847 4.5 11.9995 4.5C9.51417 4.5 7.49945 6.51472 7.49945 9C7.49945 11.4853 9.51417 13.5 11.9995 13.5Z"
                stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M16.5 14.9995V22.5L11.9993 20.25L7.5 22.5V15.0002" stroke="black" stroke-width="1.5"
                stroke-linecap="round" stroke-linejoin="round" />
            </svg>
            <span class="achievement">Добавить достижения</span>
          </li>
          <li @click="logout">
            <svg width="24" height="25" viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M14.25 8.93274V3.18274H3.75V21.1827H14.25V14.9327" stroke="black" stroke-width="1.5"
                stroke-linecap="round" stroke-linejoin="round" />
              <path
                d="M9 11.1827C8.58579 11.1827 8.25 11.5185 8.25 11.9327C8.25 12.347 8.58579 12.6827 9 12.6827V11.1827ZM21 12.6827C21.4142 12.6827 21.75 12.347 21.75 11.9327C21.75 11.5185 21.4142 11.1827 21 11.1827V12.6827ZM9 12.6827H21V11.1827H9V12.6827Z"
                fill="black" />
              <path
                d="M19.35 8.48274C19.1015 8.15137 18.6314 8.08421 18.3 8.33274C17.9686 8.58127 17.9015 9.05137 18.15 9.38274L19.35 8.48274ZM20.4 12.3827C20.6485 12.7141 21.1186 12.7813 21.45 12.5327C21.7814 12.2842 21.8485 11.8141 21.6 11.4827L20.4 12.3827ZM18.15 9.38274L20.4 12.3827L21.6 11.4827L19.35 8.48274L18.15 9.38274Z"
                fill="black" />
              <path
                d="M19.35 15.3827C19.1015 15.7141 18.6314 15.7813 18.3 15.5327C17.9686 15.2842 17.9015 14.8141 18.15 14.4827L19.35 15.3827ZM20.4 11.4827C20.6485 11.1514 21.1186 11.0842 21.45 11.3327C21.7814 11.5813 21.8485 12.0514 21.6 12.3827L20.4 11.4827ZM18.15 14.4827L20.4 11.4827L21.6 12.3827L19.35 15.3827L18.15 14.4827Z"
                fill="black" />
            </svg>
            <span class="logout">Выйти</span>
          </li>
        </ul>
      </div>
      <ProfileContainer v-bind:user=user v-if="!(editIsActive || addAchievementIsActive || addSpecIsActive)" />
      <EditProfileContainer v-bind:user=user v-else-if="editIsActive" @closeEdit="close_profile_edit" />
      <AchievementForm v-else-if="addAchievementIsActive" @close-achievement-form="addAchievementIsActive = false" />
      <SpecForm v-else-if="addSpecIsActive" @close-spec-form="addSpecIsActive = false"
        @switch-to-achievement-form="switchToAchievement" />
      <!-- <div>
        <button v-on:click="getExperts()">Все эксперты</button>
        <div v-if="this.experts.length != 0">{{this.experts}}</div>
      </div> -->
      <div class="profressBarFull" v-if="!(editIsActive || addAchievementIsActive || addSpecIsActive)">
        <p :class="'profressBar'" v-bind:style="{ width: progress + '%' }"><span v-if="progress > 0"
            class="progressLabel">{{ progress
            }}%</span></p>
        <p :class="'profressBarUngraded'" v-bind:style="{ width: ungraded + '%' }"></p>
        <div class="progress_year">{{ new Date().getFullYear() }}</div>
        <div class="progress_numbers"> {{ total_graded }}/{{ total_profile_books }} ({{ progress }}%)
        </div>
      </div>
      <AchievementList v-bind:achievements=userAchievements
        v-if="!(editIsActive || addAchievementIsActive || addSpecIsActive) && userAchievements.length" />
      <BookListParser list_id="markedListID124" v-bind:books=getMarkedBookList() v-bind:list_title='marked_list_title'
        v-if="!(editIsActive || addAchievementIsActive || addSpecIsActive) && getMarkedBookList().length"
        v-bind:userBookIds=userBookIds />
      <BookListParser list_id="unMarkedListID224" v-bind:books=getUnMarkedBookList() v-bind:list_title=usernames_list
        v-if="!(editIsActive || addAchievementIsActive || addSpecIsActive) && getUnMarkedBookList().length"
        v-bind:userBookIds=userBookIds />
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
import AchievementList from '@/components/AchievementList.vue'
import ProfileContainer from '@/components/ProfileContainer.vue'
import EditProfileContainer from '@/components/EditProfileContainer.vue'
import bookService from '@/services/bookService.js'
import userService from '@/services/userService.js'
import AchievementForm from '../components/AchievementForm.vue'
import SpecForm from '../components/SpecForm.vue'

export default {
  name: 'Profile',
  data: function () {
    return {
      editIsActive: false,
      addAchievementIsActive: false,
      addSpecIsActive: false,
      exportBooks: [],
      experts: [],
      progress: 0,
      ungraded: 0,
      userAchievements: [],
      total_profile_books: 0,
      total_graded: 0,
      userBookIds: []
    }
  },
  computed: mapState({
    user: state => state.user,
    usernames_list: () => 'Ваша коллекция',
    marked_list_title: () => 'Подтверждено',
    books: state => state.user.books,
    auth_status: state => state.authStatus
  }),
  beforeCreate: function () {
    this.$store.dispatch('getUser')
    if (this.$store.state.user.authentificated) {
      this.$store.dispatch('userbooks/getBooks')
    }
  },
  mounted () {
    this.updateUserBooks()
    this.get_progress()
    this.getUserAchievements()
    document.title = 'Профиль - Portfolio'
  },
  components: {
    BookListParser,
    ProfileContainer,
    EditProfileContainer,
    AchievementList,
    AchievementForm,
    SpecForm
  },
  methods: {
    close_profile_edit () {
      this.$store.dispatch('getUser')
      this.editIsActive = false
    },
    get_progress () {
      bookService.getProgress(this.$store.state.user.username)
        .then((res) => {
          this.progress = (res.data.progress * 100).toFixed(0)
          this.ungraded = res.data.ungraded * 100
          this.total_profile_books = res.data.total
          this.total_graded = res.data.total_graded
        })
    },
    getUserAchievements () {
      return bookService.getUserAchievements(this.$store.state.user.username)
        .then((res) => {
          console.log(res.data)
          this.userAchievements = res.data
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
    updateUserBooks: async function () {
      // this.$store.dispatch('userbooks/getBooks')
      userService.getUserBooks(this.$store.state.user.username)
        .then((resp) => {
          resp.books.forEach(element => {
            bookService.parseGoogleId(element.GoogleId).then((pb) => {
              try {
                pb[0].marked = element.marked
                pb[0].mark = element.mark
                pb[0].expert = element.expert
                pb[0].rating = element.rating
                pb = pb[0]
                // console.log(pb)
                this.exportBooks.push(pb)
                this.userBookIds.push(element.GoogleId)
              } catch (error) {
                console.log('cant load book', error)
              }
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
    },
    switchToAchievement () {
      this.addSpecIsActive = false
      this.addAchievementIsActive = true
    }
  }
}
</script>
<style>
.profressBarFull {
  height: 20px;
  width: 90vw;
  position: relative;
  left: 5vw;
  border-radius: 15px;
  background-color: #F5F0FF;
  text-align: right;
  color: #fff;
  margin-bottom: 28px;
}

.profressBar {
  /* border: 3px solid red; */
  /* background-color: rgb(149, 193, 153); */
  background: #835ED2;
  position: relative;
  /* left: -3px; */
  height: 20px;
  border-radius: 15px;
  z-index: 50;
}

.progressLabel {
  position: relative;
  left: -5px;
  top: -2px;
}

.profressBarUngraded {
  background: #DACAFC;
  /* border: 3px solid red; */
  position: relative;
  /* left: -3px; */
  height: 20px;
  border-radius: 15px;
  top: -36px;
  z-index: 45;
}

.btn-group {
  /* position: absolute; */
  color: #835ED2;
  width: 100%;
  display: flex;
  flex-flow: column nowrap;
  align-items: flex-end;
  justify-content: flex-end;
  /* border: 3px solid red; */
  /* height: 20px; */
  outline: none !important;
}

.btn-group:focus {
  outline-style: none !important;
}

.button_menu {
  letter-spacing: 3px;
  font-weight: 700;
  font-size: 20px;
  line-height: 4px;
  padding: 5px;
  margin: 5px;

}

.dropdown-menu>* {
  padding: 10px 20px;
  font-size: 16px;
}

.dropdown-menu svg {
  margin-right: 10px;
}

.dropdown-menu .edit {
  position: relative;
  top: 1px;
}

.progress_year {
  position: absolute;
  color: #C1ACE6;
  top: -25px;
  left: -5px;
  font-size: 12px;
  letter-spacing: 0.4px;
}

.progress_numbers {
  position: absolute;
  color: #C1ACE6;
  top: -25px;
  right: -5px;
  font-size: 12px;
  letter-spacing: 0.4px;
}
</style>
