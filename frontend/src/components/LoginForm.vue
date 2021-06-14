<template>
  <div class="login_component">
    <div>
   <form class="login" @submit.prevent="login">
     <h1>Авторизация</h1>
     <p v-if="message">{{  message  }}</p>
     <input required v-model="username" type="text" placeholder="Логин" />
     <input required v-model="password" type="password" placeholder="Пароль" />
     <hr/>
     <button type="submit">Login</button>
   </form>
 </div>
    <p><router-link to="/registration">Registration</router-link></p>
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
        .then(() => {
          // this.$store.commit('setUser', { username: username, authentificated: true })
          if (this.$store.state.user.authentificated === true) {
            this.$router.push('/')
          } else {
            this.message = 'Непровильный логин или пароль'
            this.$router.push('/login')
          }
        })
        .catch(err => console.log(err))
    }
  }
}
</script>
