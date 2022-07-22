<template>
  <div class="static">
    <h5 class="static__title">Статистика</h5>
    <ul>
      <StaticItem
        v-for="item in staticItems"
        :staticItem="item"
        :key="item.id"
      />
    </ul>
  </div>
</template>

<script>
import StaticItem from '../components/StaticItem.vue'
import userService from '../services/userService'
export default {
  components: { StaticItem },
  data () {
    return {
      staticItems: []
    }
  },
  created () {
    this.staticItems = userService.getUserStatistics(this.$store.state.user.username)
      .then(data => {
        this.staticItems = data.progress
      })
  }

}
</script>

<style scoped>
ul {
  padding: 0;
}

.static {
  padding: 1rem;
}

.static__title {
  text-align: start;
  font-size: 24px;
  line-height: 28px;
  font-weight: 400;
  margin-bottom: 1rem;
}

.btn {
  color: #835ed2;
}
</style>
