<template>
  <div class="about">
    <LoginForm />
    test@mail.com<br>
    newTestUserPassword12345
  </div>
</template>

<script>
// @ is an alias to /src
// import store from '@/store/'
import LoginForm from '@/components/LoginForm.vue'
export default {
  name: 'Login',
  components: {
    LoginForm
  }
}
</script>
