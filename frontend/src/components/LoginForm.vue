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
        <br>
        auth_status: {{  auth_status  }}<br>
        <div class="error" v-if="loginTries > 0 && auth_status === 'error'">
          <p>Неправильный email или пароль</p>
        </div>
        {{loginTries}}
        <p><router-link to="/registration">Регистрация</router-link></p>
      </form>
    </div>
    <div v-else>
      <h2>Вы авторизованы как {{  this.$store.getters.user.username  }}</h2>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'LoginForm',
  data () {
    return {
      username: '',
      password: '',
      message: '',
      loginTries: 0
    }
  },
  computed: mapState({
    auth_status: state => state.auth_status
  }),
  methods: {
    login: function () {
      this.loginTries += 1
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
