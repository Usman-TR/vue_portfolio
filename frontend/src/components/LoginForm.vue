<template>
  <div class="login_component">
    <template v-if="!getAuthStatus()">
      <form class="login" @submit.prevent="login">
        <h1 class="login__title">Авторизация</h1>
        <p v-if="message">{{  message  }}</p>
        <fieldset class="login-field">
          <input :class="{'input-error': v$.username.$errors.length && username.length}" class="login__input" required v-model="username" type="text" placeholder="Логин" />
          <input :class="{'input-error': v$.password.$errors.length && username.length}" class="login__input" required v-model="password" type="password" placeholder="Пароль" />
          <div v-if="v$.password.$errors.length || v$.password.$errors.length || auth_status === 'error'" class="error">Неправильный логин или пароль</div>
          <a class="tip" href="#">Забыли пароль?</a>
        </fieldset>
        <button class="login__btn" type="submit">Войти</button>
        <p>Ещё нет аккаунта? <router-link to="/registration">Зарегистрируйтесь</router-link></p>
      <br>
        auth_status: {{  auth_status  }}<br>
        {{loginTries}}
      </form>
    </template>
    <div v-else>
      <h2>Вы авторизованы как {{  this.$store.getters.user.username  }}</h2>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import useVuelidate from '@vuelidate/core'
import { required, minLength, or, email, alpha, alphaNum } from '@vuelidate/validators'
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
  computed: mapGetters({
    auth_status: 'authStatus'
  }),
  methods: {
    async login () {
      this.loginTries += 1
      const username = this.username
      const password = this.password
      const isFormCorrect = await this.v$.$validate()
      if (!isFormCorrect) return
      await this.$store.dispatch('login', { username, password })
    },
    getAuthStatus () {
      if (this.$store.getters.user.authentificated) this.$router.push('/')
      return this.$store.getters.user.authentificated
    }
  },
  validations () {
    return {
      username: { required, or: or(email, alpha), min: minLength(4) },
      password: { required, min: minLength(8), alphaNum }
    }
  },
  setup () {
    return {
      v$: useVuelidate()
    }
  }
}
</script>
<style scoped>
.login {
  max-width: 375px;
  margin-inline: auto;
  padding-top: 10vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  width: 100%;
  padding-inline: 1rem;
}
.login-field {
  display: flex;
  flex-direction: column;
  align-content: center;
  gap: 1rem;
  width: 100%;
}
.login a {
  text-decoration: none;
  color: #835ED2;
}
.login__btn {
    border-radius: 6px;
    display: grid;
    place-content: center;
    color: #835ED2;
    background-color: #EEE7FF;
    border: none;
    width: 100%;
    height: 2.6rem;
  }
.login__btn:hover {
  color: #fff;
  background-color: #835ED2;
  transition-duration: 400ms;
}
.login__input {
  padding: 8px;
  font-size: 1rem;
  color: #000;
  border: 0.5px solid #DACAFC;
  border-radius: 6px;
  background: #FAF7FF;
}
.login__input:hover {
  border-color: #ae8cf7;
  background-color: #fff;
}
.login__input::placeholder {
    color: #9788B8;
    opacity: 1;
}
.login__input:focus {
    background-color: #fff;
  outline: 1px solid #835ED2;
}
.login__input:focus::placeholder {
  color: #9788B8;
  opacity: .6;
}
.tip {
  font-size: 0.75rem;
  align-self: flex-end;
  text-decoration: none;
}
.login p {
  font-size: 0.875rem;
}
.input-error, .input-error:focus {
  outline: 1.4px solid red;
}
.error {
  color: red
}
</style>
