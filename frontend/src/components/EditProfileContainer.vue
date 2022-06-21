<template>
    <div class="user_info">
      Редактировать профиль
      <div class="user_info_main">
        <img class="profile_img" src="@/assets/profile-avatar.svg" alt='{{ user.username }}'>
        <p class="profile_container">Профиль:
          <select name="profile" id="profile_select" v-model="this.profile">
          <option v-for="profile in profiles" v-bind:value="profile.id" :key="profile.id">
            {{profile.title}}
          </option>
          </select>
        </p>
        <p class="university_container">Университет:
          <select name="university" id="university_select" v-model="this.university">
          <option v-for="university in universities" v-bind:value="university.id" :key="university.id">
            {{university.title}}
          </option>
          </select>
        </p>
        <p class="about_me">О себе: <input type="text" v-model="about_me">{{  this.about_me  }}</p>
        <p class="first_name">Имя: <input type="text" v-model="this.first_name"></p>
        <p class="last_name">Фамилия: <input type="text" v-model="this.last_name"></p>
        <p class="middle_name">Отчество: <input type="text" v-model="this.middle_name"></p>
        <p><button v-on:click="updateProfile()">Обновить</button></p>
      </div>
    </div>
</template>

<script>
import formService from '@/services/formService.js'

export default {
  name: 'ProfileContainer',
  props: {
    user: Object
  },
  data: function () {
    return {
      name: '',
      surname: '',
      middle_name: '',
      first_name: '',
      last_name: '',
      profile: '',
      university: '',
      about_me: '',
      profiles: []
    }
  },
  computed () {
    // profiles = this.getProfiles()
  },
  mounted () {
    this.setDefData()
  },
  methods: {
    getProfiles: function () {
      formService.getProfiles()
        .then((res) => {
          this.profiles = res.data.profiles
        })
    },
    getUniversities: function () {
      console.log('getUniversities')
      formService.getUniversities()
        .then((res) => {
          console.log('getUniversities', res.data.universities)
          this.universities = res.data.universities
        })
    },
    setDefData: function () {
      const user = this.$store.state.user
      this.name = user.first_name
      this.surname = user.last_name
      this.middleName = user.middleName
      this.profile = user.profile
      this.university = user.university
      this.aboutMe = user.aboutMe

      this.getProfiles()
      this.getUniversities()
    },
    updateProfile: function () {
      const form = {
        about_me: this.about_me,
        first_name: this.first_name,
        last_name: this.last_name,
        middle_name: this.middle_name,
        profile: this.profile,
        university: this.university
      }
      console.log(form)
      formService.updateProfile(this.$store.state.user.username, form)
        .then()
    }
  }
}
</script>

<style>
@media (min-width: 8px) {
  .user_info_main{
    align-items: center;
    text-align: center;
    width: 100%;
  }
  .user_info_main .profile_username{
    padding: 0;
    font-size: x-large;
    margin: 10px;
  }
  .user_info_main .level{
    padding: 0;
    margin: 20px 10px 10px 10px;
    font-size: medium;
  }
  .user_info_main .university{
    padding: 0;
    margin: 10px;
  }
  .user_info_main .rating{
    padding: 0;
    margin: 25px;
  }
  .profile_img{
    width: 200px;
    border-radius: 100%;
  }
}
</style>
