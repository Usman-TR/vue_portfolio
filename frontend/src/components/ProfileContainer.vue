<template>
    <div class="user_info">
      <div class="user_info_main">
        <img class="profile_img" src="@/assets/profile-avatar.svg" alt='{{ user.username }}'>
        <p class="profile_username">{{ user.username }}</p>
        <!-- <p class="isExpert" v-if="user.expert">Эксперт</p> -->
        <p class="profile"><span v-if="user.profile.length">{{  user.profile[0].title  }}</span><span v-else>Нет профиля</span></p>
        <p class="university"><span v-if="user.university">{{  user.university.title  }}</span><span v-else>Нет университета</span></p>
        <!-- <p class="about_me">О себе: {{  user.about_me  }}</p> -->
        <RatingStars :rating=user.rating />
        <!-- <p class="email">Почта: {{ user.email }}</p> -->
        <!-- <p class="first_name">Имя: {{ user.first_name }}</p>
        <p class="last_name">Фамилия: {{ user.last_name }}</p>
        <p class="middle_name">Отчество: {{ user.middle_name }}</p> -->
      </div>
    </div>
</template>

<script>
import RatingStars from '@/components/RatingStars.vue'

export default {
  name: 'ProfileContainer',
  components: {
    RatingStars
  },
  props: {
    user: Object
  }
}
</script>

<style>

@media (min-width: 8px) {
  .profile_username{
    font-weight: 500;
    font-size: 20px;
    line-height: 28px;
  }
  .profile, .university{
    font-size: 14px;
    line-height: 20px;
    margin: 0;
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
  .checked {
    color: #F7C33E;
  }
  .fa-star {
    width: 20px;
    height: 20px;
  }
}
</style>
