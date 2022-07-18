<template>
  <div class="register">
    <h4>Регистрация</h4>
    <form class="form" @submit.prevent="register">
      <fieldset class="form-field">
        <label for="name">Имя</label>
        <input :class="{ 'input-error': v$.name.$errors.length }" class="register__input" id="name" type="text"
          v-model="name" required autofocus>
      </fieldset>
      <fieldset class="form-field">
        <label for="email">Адрес электронной почты</label>
        <input :class="{ 'input-error': v$.email.$errors.length }" class="register__input" id="email" type="email"
          v-model="email" required>
        <div class="error" v-if="v$.email.$errors.length">Проверьте правильность введённого адреса электронной почты
        </div>
      </fieldset>
      <fieldset class="form-field">
        <label for="password">Пароль</label>
        <input :class="{ 'input-error': v$.password.$errors.length }" class="register__input" id="password"
          type="password" v-model="password" required>
        <div class="error" v-if="v$.password.$errors.length">Длина пароля не может быть меньше 8 символов</div>
      </fieldset>
      <fieldset class="form-field">
        <label for="password-confirm">Подтвердить пароль</label>
        <input :class="{ 'input-error': v$.password_confirmation.$errors.length }" class="register__input"
          id="password-confirm" type="password" v-model="password_confirmation" required>
        <div class="error" v-if="v$.password_confirmation.$errors.length">Введенные пароли не совпадают</div>
      </fieldset>
      <button class="register__btn" type="submit">Зарегистрироваться</button>
    </form>
    <p>newTestUser <br> newTestUser@mail.com<br> newTestUserPassword12345</p>
  </div>
</template>

<script>
import useVuelidate from '@vuelidate/core'
import { required, minLength, email, alphaNum, sameAs } from '@vuelidate/validators'
import userService from '../services/userService'
export default {
  name: 'LoginForm',
  data () {
    return {
      name: '',
      email: '',
      password: '',
      password_confirmation: ''
    }
  },
  validations () {
    return {
      name: {
        required,
        username (value) {
          return /^[A-z]+[0-9]*/.test(value)
        }
      },
      email: { required, email },
      password: { required, alphaNum, min: minLength(8) },
      password_confirmation: { required, sameAs: sameAs(this.password) }
    }
  },
  methods: {
    async register () {
      const data = {
        username: this.name,
        email: this.email,
        password1: this.password,
        password2: this.password_confirmation
      }
      const isFormCorrect = await this.v$.$validate()
      if (!isFormCorrect) return
      userService.register(data).then((res) => {
        console.log(res)
        this.$router.push('/login')
      }).catch((err) => {
        console.error(err)
      })
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
.register {
  padding-top: 7vh;
  max-width: 375px;
  margin-inline: auto;
}

.register__btn {
  display: grid;
  place-content: center;
  color: #fff;
  background-color: #835ED2;
  border-radius: 6px;
  border: none;
  width: 100%;
  height: 2.6rem;
  margin-top: 1.5rem;
}

.register__btn:hover {
  color: #835ED2;
  background-color: #EEE7FF;
}

.form {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.2rem;
  margin-top: 1.2rem;
  width: 100%;
  padding-inline: 1rem;
}

.form-field {
  display: flex;
  flex-direction: column;
  align-items: start;
  gap: 4px;
  width: 100%;
}

.form-field label {
  font-weight: 700;
}

.register__input {
  padding: 8px;
  font-size: 1rem;
  color: #000;
  border: 0.5px solid #DACAFC;
  border-radius: 6px;
  background: #FAF7FF;
  width: 100%;
}

.register__input:hover {
  border-color: #ae8cf7;
  background-color: #fff;
}

.register__input::placeholder {
  color: #9788B8;
  opacity: 1;
}

.register__input:focus {
  outline: 1px solid #835ED2;
  background-color: #fff;
}

.register__input:focus::placeholder {
  color: #9788B8;
  opacity: .4;
}

.input-error,
.input-error:focus {
  outline: 1.4px solid #ee3f58;
}

.error {
  color: #ee3f58;
  font-size: 0.875rem;
  line-height: 20px;
  text-align: start;
}
</style>
