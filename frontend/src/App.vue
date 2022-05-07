<template>
  <div id="nav">
    <router-link to="/">Главная</router-link> |
    <router-link v-if="this.$store.state.user.expert" to="/expert">Кабинет эксперта</router-link> |
    <router-link v-if="this.$store.state.user.authentificated" to="/profile">{{  this.$store.state.user.username  }}</router-link>
    <router-link v-else to="/login">Войти</router-link>
    <!-- <div>{{this.$store.state}}</div> -->
  </div>
  <router-view/>
</template>

<style lang="scss">

@media (min-width: 8px) {
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  #nav {
    padding: 30px;

    a {
      font-weight: bold;
      color: #2c3e50;

      &.router-link-exact-active {
        color: #42b983;
      }
    }
  }
}
</style>
