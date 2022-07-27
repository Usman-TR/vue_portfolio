<template>
    <div class="user_info">
      <span class="button_back" v-on:click="close_edit()">
        <svg width="12" height="22" viewBox="0 0 12 22" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M11 21L1 11L11 1" stroke="#835ED2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </span>
      <div class="edit_profile_header"><span class="edit_profile_title">Редактирование</span><span class="edit_profile_button" v-on:click="updateProfile()">Готово</span></div>
      <form class="user_info_main">
        <img class="profile_img" src="@/assets/profile-avatar.svg" alt='{{ user.username }}'>
        <p class="first_name edit_profile_input_wrapper">
          <span class="validation_label" v-if="!validators.first_name && btn_pressed">Укажите имя</span>
          <input type="text" class="form-control" placeholder="Имя" aria-label="Имя" v-model="this.first_name">
        </p>
        <p class="last_name edit_profile_input_wrapper"><span class="validation_label" v-if="!validators.last_name && btn_pressed">Укажите фамилию</span>
          <input type="text" class="form-control" placeholder="Фамилия" aria-label="Фамилия" v-model="this.last_name"></p>
        <p class="middle_name edit_profile_input_wrapper">
          <input type="text" class="form-control" placeholder="Отчество" aria-label="Отчество" v-model="this.middle_name"></p>
        <p class="edit_profile_label">Выберите ВУЗ и специальность</p>
        <p class="university_container">
          <span class="validation_label" v-if="!validators.university && btn_pressed">Укажите университет</span>
          <select class="form-select" name="university" id="university_select" v-model="this.university">
          <option v-for="university in universities" v-bind:value="university.id" :key="university.id">
            {{university.title}}
          </option>
          </select>
        </p>
        <p class="profile_container">
          <span class="validation_label" v-if="!validators.profile && btn_pressed">Укажите профиль</span>
          <select class="form-select" name="profile" id="profile_select" v-model="this.profile">
          <option v-for="profile in profiles" v-bind:value="profile.id" :key="profile.id">
            {{profile.title}}
          </option>
          </select>
        </p>
        <p class="edit_profile_label">Расскажите немного о себе, эта информация пойдет в ваше резюме</p>
        <p class="about_me edit_profile_input_wrapper"><textarea type="text" class="form-control" placeholder="О себе" aria-label="О себе" v-model="about_me"></textarea></p>
      </form>
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
      profiles: [],
      universities: [],
      btn_pressed: false,
      validators: {
        first_name: false,
        last_name: false,
        university: false,
        profile: false
      }
    }
  },
  computed () {
    // profiles = this.getProfiles()
  },
  mounted () {
    this.setDefData()
  },
  methods: {
    validate () {
      if (this.first_name.length) {
        this.validators.first_name = true
      } else {
        this.validators.first_name = false
      }

      if (this.last_name.length) {
        this.validators.last_name = true
      } else {
        this.validators.last_name = false
      }

      if (!isNaN(this.university)) {
        this.validators.university = true
      } else {
        this.validators.university = false
      }

      if (!isNaN(this.profile)) {
        this.validators.profile = true
      } else {
        this.validators.profile = false
      }

      return Object.values(this.validators).every(
        value => value
      )
    },
    getProfiles: function () {
      formService.getProfiles()
        .then((res) => {
          this.profiles = res.data.profiles
        })
    },
    getUniversities: function () {
      formService.getUniversities()
        .then((res) => {
          this.universities = res.data.universities
        })
    },
    setDefData: function () {
      const user = this.$store.state.user

      this.first_name = user.first_name
      this.last_name = user.last_name
      this.middle_name = user.middle_name
      this.profile_obj = user.profile
      this.university_obj = user.university
      this.aboutMe = user.aboutMe

      this.btn_pressed = false

      this.getProfiles()
      this.getUniversities()

      if (this.profile_obj.length) {
        this.profile = this.profile_obj[0].id
      }

      if (this.university_obj) {
        this.university = user.university.id
      }
    },
    updateProfile: function () {
      this.btn_pressed = true
      const form = {
        about_me: this.about_me,
        first_name: this.first_name,
        last_name: this.last_name,
        middle_name: this.middle_name,
        profile: this.profile,
        university: this.university
      }
      console.log(form)

      if (!this.validate()) return -1

      formService.updateProfile(this.$store.state.user.username, form)
        .then(() => this.$emit('closeEdit'))
    },
    close_edit: function () {
      this.$emit('closeEdit')
    }
  }
}
</script>

<style>
@media (min-width: 8px) {
  .user_info {
    margin-top: 30px;
  }
  .user_info select, .user_info input, .user_info input::placeholder {
    color: #9788B8;
    background: #FAF7FF;
    /* padding: 12px; */
    margin: 12px 0;
  }
  .edit_profile_title {
   font-size: 16px;
   line-height: 24px;
   text-align: center;
   letter-spacing: 0.44px;
  }
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
  .edit_profile_input_wrapper{
    margin: 6px 12px;
  }
  .edit_profile_label {
    font-size: 14px;
    font-weight: 400;
    line-height: 20px;
    letter-spacing: 0.25px;
    text-align: left;
    color: rgba(60, 60, 67, 0.6);
    margin: 24px 12px 8px 12px;
  }
  .edit_profile_button {
    position: absolute;
    display: block;
    top: 30px;
    right: 14px;
    z-index: 100;
    color: #835ED2;
  }
  .edit_profile_header {
    display: flex;
    justify-content: space-around;
  }
  .university_container, .profile_container {
    margin: 6px 12px;
  }
  .university_container select, .profile_container select {
    background-color: #FAF7FF;
  }
  .validation_label {
    font-size: 0.875em;
    color: #dc3545;
    text-align: left;
    width: 100%;
    display: block;
    position: relative;
    top: 10px;
  }
  .button_back{
    position: absolute;
    left: 13px;
  }

}
</style>
