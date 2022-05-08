<template>
    <div class="user_info">
      <div class="user_info_main">
        <img class="profile_img" src="@/assets/profile-avatar.svg" alt='{{ user.username }}'>
        <p class="profile_username">Логин: {{ user.username }}</p>
        <p class="isExpert" v-if="user.expert">Эксперт</p>
        <p class="profile">Профиль: {{  user.profile[0].title  }}</p>
        <p class="university">Университет: {{  user.university.title  }}</p>
        <p class="about_me">О себе: {{  user.about_me  }}</p>
        <p class="rating">Рейтинг: {{  user.rating  }}</p>
        <p class="email">Почта: {{ user.email }}</p>
        <p class="first_name">Имя: {{ user.first_name }}</p>
        <p class="last_name">Фамилия: {{ user.last_name }}</p>
        <p class="middle_name">Отчество: {{ user.middle_name }}</p>
      </div>
    </div>
</template>

<script>

export default {
  name: 'ProfileContainer',
  props: {
    user: Object
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
    font-size: small;
  }
  .user_info_main .rating{
    padding: 0;
    margin: 25px;
    font-size: small;
  }
  .profile_img{
    width: 200px;
    border-radius: 100%;
  }
}
</style>
