<template>
  <div class="expert">

    <div class="expert_page_label" v-if="requests.length === 0">Нет запросов на получение оценки</div>
    <div class="expert_page_label" v-else>Запросы оценок</div>

    <div class="request_items">
{{pressedList}}
<div v-for="(val, index) in this.sortRequests(requests)" :key="index">
  <p>
    <a class="btn" type="button" v-on:click="pressedList[index] != true" data-bs-toggle="collapse" :data-bs-target="'#' + index" aria-expanded="false" :aria-controls="index">
      <h3>{{index}}</h3>
      <svg v-if="pressedList[index]" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M19.5 9L12 16.5L4.5 9" stroke="#DACAFC" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>

    </a>
  </p>
  <div class="collapse" :id="index">
<div class="request_item" v-for="req in val" :key="req.id">
        <img v-if="req.bookImage" :src="getImage(req.bookImage)" class="img-fluid" />
        <p>{{req.boolTitle}}</p>
        <p>{{formateAuthors(req.bookAuthors)}}</p>
        <p>{{req.firstName}} {{req.lastName}}</p>
        <p>{{req.profile}}</p>
        <p>{{req.university}}</p>
        <button v-on:click="evaluateForm(req)" v-if="!markedRequests.includes('req' + req.id)">Оценить</button><span v-else>Оценено</span>
    </div>
  </div>
</div>

  <!-- <div v-for="(val, index) in this.sortRequests(requests)" :key="index">
    <h3>{{index}}</h3>
    <div class="request_item" v-for="req in val" :key="req.id">
        <img v-if="req.bookImage" :src="getImage(req.bookImage)" class="img-fluid" />
        <p>{{req.boolTitle}}</p>
        <p>{{formateAuthors(req.bookAuthors)}}</p>
        <p>{{req.firstName}} {{req.lastName}}</p>
        <p>{{req.profile}}</p>
        <p>{{req.university}}</p>
        <button v-on:click="evaluateForm(req)" v-if="!markedRequests.includes('req' + req.id)">Оценить</button><span v-else>Оценено</span>
    </div>
  </div> -->
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
      markedRequests: [],
      pressedList: {}
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
    sortRequests (reqs) {
      const output = {}
      reqs.forEach(element => {
        if (output[element.username] !== undefined) {
          output[element.username].push(element)
        } else {
          output[element.username] = []
          output[element.username].push(element)
          this.pressedList[element.username] = false
        }
      })
      return output
    },
    getImage (path) {
      return path
    },
    formateAuthors (authors) {
      if (authors) {
        return authors.toString().replaceAll('[', '').replaceAll(']', '').replaceAll('\'', '')
      } else {
        return ''
      }
    },
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

<style>
.request_item {
  display: block;
  width: 90vw;
  margin-left: 5vw;
  margin-bottom: 12px;
  padding: 12px 8px;
  background: #FFFFFF;
  box-shadow: 0px 8px 16px rgba(131, 94, 210, 0.12);
  border-radius: 6px;
}
.expert_page_label {
  margin-top: 40px;
  margin-bottom: 36px;

  font-weight: 400;
font-size: 24px;
line-height: 24px;
/* identical to box height, or 150% */

text-align: center;
letter-spacing: 0.44px;

/* Label Color / Light / Primary */

color: #000000;
}

.request_item img {
  width: 100px;
  height: 100px;
}
</style>
