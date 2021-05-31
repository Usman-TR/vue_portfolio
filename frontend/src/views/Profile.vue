<template>
  <div class="Profile">
    <h1>This is a Profile page of {{ user.username }}</h1>
    <p>id: {{  user.id  }}</p>
    <p>username: {{  user.username  }}</p>
    <p>email: {{  user.email  }}</p>
    <p>is_expert: {{  user.is_expert  }}</p>
    <p>description: {{  user.description  }}</p>
    <p>rating: {{  user.rating  }}</p>
  </div>
</template>

<script>
// @ is an alias to /src
// import store from '@/store/'
import { mapState } from 'vuex'

export default {
  name: 'Profile',
  computed: mapState({
    user: state => state.user
  }),
  created: function () {
    this.$store.dispatch('getUser')
  }
}
</script>
