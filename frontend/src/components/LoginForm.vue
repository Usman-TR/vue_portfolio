<template>
  <div class="login_component">
    <div v-if="!getAuthStatus()">
      <form class="login" @submit.prevent="login">
        <h1>Авторизация</h1>
        <p v-if="message">{{  message  }}</p>
        <input required v-model="username" type="text" placeholder="Логин" />
        <input required v-model="password" type="password" placeholder="Пароль" />
        <hr/>
        <button type="submit">Login</button>
        <p><router-link to="/registration">Регистрация</router-link></p>
      </form>
    </div>
    <div v-else>
      <h2>Вы авторизованы как {{  this.$store.getters.user.username  }}</h2>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data () {
    return {
      username: '',
      password: '',
      message: ''
    }
  },
  methods: {
    login: function () {
      const username = this.username
      const password = this.password
      this.$store.dispatch('login', { username, password })
        .then(() => { this.$router.push('/login') })
        .catch(err => console.log(err))
    },
    getAuthStatus: function () { return this.$store.getters.user.authentificated }
  }
}
</script>
