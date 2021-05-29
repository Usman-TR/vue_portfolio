<template>
  <div class="Profile">
    <h1>This is a Profile page of {{ username }}</h1>
  </div>
</template>

<script>
// @ is an alias to /src
// import store from '@/store/'
import { mapState } from 'vuex'

export default {
  name: 'Profile',
  computed: mapState({
    username: state => state.username
  })
}
</script>
