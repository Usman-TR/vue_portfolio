<template>
  <div class="achivements_page">
    <AchievementList :achievements="achievements" :listTitle="'Все достижения'" />
    <div class="profile_form">
      <p>Выберите специальность</p>
      <select class="form-select form-select-lg mb-3" aria-label=".form-select-lg example" v-model="profileID" @change="loadProfileBooks(profileID)">
        <option v-for="profile in profiles" :key="profile.id" :value="profile.id">{{profile.title}}</option>
      </select>
    </div>
    <BookListDB :books='profileBooks' :userBookIds="userBookIds" :list_id="'achievementsPageListID234'"
    :list_title="'Книги по специальности'"
    />
  </div>
</template>

<script>
import userService from '../services/userService'
import AchievementList from '@/components/AchievementList.vue'
import BookListDB from '@/components/BookListDB.vue'
import bookService from '../services/bookService'

export default {
  components: {
    AchievementList,
    BookListDB
  },
  data () {
    return {
      achievements: [],
      profileBooks: [],
      userBookIds: [],
      profileID: null,
      profiles: []
    }
  },
  mounted () {
    this.loadAchievements()
    this.loadDefaultBooks()
    this.updateUserBookIds()
    this.loadProfiles()
  },
  methods: {
    loadDefaultBooks () {
      this.profileID = this.$store.state.user.profile.id
      this.loadProfileBooks(this.profileID)
    },
    loadProfiles () {
      bookService.getProfiles()
        .then((res) => {
          try {
            this.profiles = res.data.profiles
          } catch (error) {
            console.log(error)
          }
        })
    },
    loadAchievements () {
      bookService.getAllAchievements()
        .then((res) => {
          this.achievements = res.data
        })
    },
    updateUserBookIds: async function () {
      userService.getUserBooks(this.$store.state.user.username)
        .then((resp) => {
          resp.books.forEach(element => {
            this.userBookIds.push(element.GoogleId)
          })
        })
        .catch((err) => {
          console.log('cant load user books', err)
        })
    },
    async loadProfileBooks (profileID) {
      bookService.getProfileBooks(profileID)
        .then((res) => {
          this.profileBooks = res.data.books
        })
    }
  }
}
</script>

<style scoped>
.achivements_page {
  margin-top: 16px;
}

</style>
