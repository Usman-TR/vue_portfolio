<template>
  <div class="expert">
    <div v-if="requests.length === 0">Нет запросов на получение оценки</div>
    <div v-for="req in requests" :key="req.id" :id='"req" + req.id'>
      {{ req.id }} - {{ req.username }} - {{ req.book }} - <button v-on:click="evaluateForm(req)" v-if="!markedRequests.includes('req' + req.id)">Оценить</button><span v-else>Оценено</span>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import bookService from '../services/bookService'

export default {
  name: 'Expert',
  data: function () {
    return {
      requests: [],
      markedRequests: []
    }
  },
  computed: mapState({
    user: state => state.user
  }),
  mounted () {
    this.updateRequestList()
  },
  components: {
  },
  methods: {
    updateRequestList () {
      const username = this.$store.state.user.username
      console.log(username)
      bookService.getRequests(username)
        .then((reqs) => {
          this.requests = reqs.data.requests
          console.log(reqs)
        })
    },
    evaluateForm (req) {
      let mark = prompt('Введите оценку от 2 до 5')
      console.log(mark)
      while (!(mark === '2' || mark === '3' || mark === '4' || mark === '5')) {
        if (mark === '' || mark === null) {
          break
        }
        mark = prompt('Введите корректную оценку от 2 до 5')
      }

      if (mark !== null || mark !== '') {
        bookService.setMark(req.id, this.$store.state.user.username, mark).then(() => {
          this.markedRequests.push('req' + req.id)
        })
      }
    }
  }
}
</script>
