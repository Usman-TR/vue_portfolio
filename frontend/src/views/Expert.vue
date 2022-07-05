<template>
  <div class="expert">

    <div class="expert_page_label" v-if="requests.length === 0">Нет запросов на получение оценки</div>
    <div class="expert_page_label" v-else>Запросы оценок</div>
    <div class="request_items">
<div v-for="(val, index) in this.sortRequests(requests)" :key="index">
  <p>
    <a class="btn request_button" type="button" v-on:click="dropDown(index)" data-bs-toggle="collapse" :data-bs-target="'#' + index" aria-expanded="false" :aria-controls="index">
      <div class="request_items_profile">
        <img class="request_items_profile_image" v-if="val.image" v-bind:src=val.image>
        <img class="request_items_profile_image" v-else src='@/assets/profile-avatar.svg'>
        </div>
      <div class="request_items_labels">
        <p class="request_items_labels_username" v-if="(val[0].firstName + val[0].lastName).length > 0">{{val[0].firstName}} {{val[0].lastName}}</p>
        <p class="request_items_labels_username" v-else>{{val[0].username}}</p>
        <p class="request_items_labels_profile"><span v-if="val[0].profile != 'нет'">{{val[0].profile}}</span><span v-else>нет профиля</span></p>
        <p class="request_items_labels_university"><span v-if="val[0].university != 'нет'">{{val[0].university}}</span><span v-else>нет университета</span></p>
      </div>
      <div class="request_items_arrow_container">
        <p class="request_items_arrow_container_counter">
          <span>{{ val.length }}</span>
        </p>
        <svg v-if="pressedList[index]" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M19.5 9L12 16.5L4.5 9" stroke="#DACAFC" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <svg v-else width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M3 15.75L10.5 8.25L18 15.75" stroke="#DACAFC" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
    </a>
  </p>
  <div class="collapse" :id="index">
<div class="request_item" v-for="req in val" :key="req.id">
        <div class="request_item_image_container">
          <img v-if="req.bookImage" :src="getImage(req.bookImage)" />
        </div>
        <div class="request_item_labels_container">
          <div class="request_item_labels">
            <p class="request_item_labels_title">{{cutText(req.bookTitle, 52)}}</p>
            <p class="request_item_labels_authors">{{formateAuthors(req.bookAuthors)}}</p>
          </div>
          <div class="request_item_buttons">
            <button class="request_item_buttons_rate" v-on:click="showGradeMenu(req)" v-if="!markedRequests.includes('req' + req.id) && !cancelledRequests.includes('req' + req.id)">Подтвердить</button>
            <span v-else class="request_item_buttons_done">Оценено</span>
            <button class="request_item_buttons_cancel" v-on:click="cancelEval(req)" v-if="!markedRequests.includes('req' + req.id) && !cancelledRequests.includes('req' + req.id)">Отклонить</button>
          </div>
        </div>
    </div>
  </div>
</div>
    </div>

<div class="expert_grade_container" v-if="show_grade_container">
        <div class="expert_grade_container_form">
          <h2 class="expert_grade_container_label">Выберите оценку: {{current_grade}}</h2>
          <input type="range" class="form-range" min="0" max="10" v-model="current_grade">
          <div class="select_expert_container_form_buttons">
            <span class="select_expert_container_form_button_cancel" v-on:click="hideGradeMenu()">Отмена</span>
            <span class="select_expert_container_form_button" v-on:click="evaluateForm()">Отправить</span>
          </div>
        </div>
      </div>

  <div v-if="popup_is_active" class="alert d-flex align-items-center expert_popup" role="alert">
          <p>{{popup_msg}}</p>
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
      cancelledRequests: [],
      pressedList: {},
      current_grade: 5,
      current_req: {},
      show_grade_container: false,
      popup_is_active: false,
      popup_msg: ''
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
    popup_message (msg) {
      this.popup_msg = msg
      this.popup_is_active = true
      this.delay(2000).then(() => { this.popup_is_active = false })
    },
    delay (time) {
      return new Promise(resolve => setTimeout(resolve, time))
    },
    hideGradeMenu () {
      this.show_grade_container = false
    },
    showGradeMenu (req) {
      this.current_req = req
      this.show_grade_container = true
    },
    cutText (str, len) {
      if (str.length < len) {
        return str
      } else {
        return str.slice(0, len) + '...'
      }
    },
    cancelEval (req) {
      bookService.cancelMarkRequest(req.username, req.GoogleId, this.$store.state.user.username)
        .then(() => {
          this.cancelledRequests.push('req' + req.id)
          this.popup_message('Отклонено')
        })
        .catch((err) => {
          console.log(err)
          this.popup_message('Ошибка, повторите позже')
        })
    },
    dropDown (index) {
      this.pressedList[index] = !this.pressedList[index]
      console.log(this.pressedList)
    },
    sortRequests (reqs) {
      const output = {}
      reqs.forEach(element => {
        if (output[element.username] !== undefined) {
          output[element.username].push(element)
        } else {
          output[element.username] = []
          output[element.username].push(element)
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
    evaluateForm () {
      const mark = this.current_grade
      const req = this.current_req
      if (mark !== null || mark !== '') {
        bookService.setMark(req.id, this.$store.state.user.username, mark)
          .then(() => {
            this.markedRequests.push('req' + req.id)
            this.hideGradeMenu()
            this.popup_message('Отправлено')
          })
          .catch((err) => {
            console.log(err)
            this.hideGradeMenu()
            this.popup_message('Ошибка, повторите позже')
          })
      }
    }
  }
}
</script>

<style>
.request_item {
  display: flex;
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

  font-weight: 400 !important;
font-size: 24px !important;
line-height: 24px !important;
/* identical to box height, or 150% */

text-align: center;
letter-spacing: 0.44px;

/* Label Color / Light / Primary */

color: #000000;
}

/* .request_item img {
  width: 100px;
  height: 100px;
} */

.request_item_image_container {
  width: 56px !important;
  height: 77px !important;
  flex-shrink: 0;
}
.request_item_image_container img{
  width: 100%;
  height: auto;
}

.request_item_labels_title {
  font-weight: 500;
  font-size: 12px;
  line-height: 16px;
  text-align: left;
  letter-spacing: 0.4px;
  margin-left: 12px;
}

.request_item_labels_authors {
  font-weight: 400;
  font-size: 10px;
  line-height: 16px;
  letter-spacing: 0.4px;
  text-align: center;
  color: rgba(60, 60, 67, 0.6);
  width: 100%;

}

.request_item_buttons > *{
  padding: 6px 10px;
  font-size: 10px;
  line-height: 16px;
  letter-spacing: 0.4px;
  color: #FFFFFF;
  outline: none;
  border: none;
  margin: 4px;
  border-radius: 6px;

}

.request_item_buttons_rate {
  background: #835ED2;
}

.request_item_buttons_done {
  background: #EEE7FF;
  color: #835ED2;
}

.request_item_buttons_cancel {
  background: #EEE7FF;
  color: #835ED2;
}

.request_button {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.request_item_labels_container {
  flex-grow: 1;
}
.request_items_labels {
  flex-grow: 1;
}
.request_items_labels > *{
  margin: 0;
  padding: 0;
}
.request_items_labels_username {
  font-weight: 400;
  font-size: 16px;
  line-height: 24px;
  display: flex;
  align-items: center;
  letter-spacing: 0.44px;
  color: #000000;

}
.request_items_labels_profile {
  font-weight: 400;
  font-size: 12px !important;
  line-height: 16px;
  display: flex;
  align-items: center;
  letter-spacing: 0.4px;
  color: #8E8E93;
}
.request_items_labels_university {
  font-weight: 400;
font-size: 12px !important;
line-height: 16px;
display: flex;
align-items: center;
letter-spacing: 0.4px;
color: rgba(60, 60, 67, 0.3);
}
.request_button svg{
  position: relative;
  top: -2px;
  right: -10px;
}
.request_items_profile_image {
  width: 56px;
  height: 56px;
  border-radius: 112px;
  margin-right: 12px;
}
.request_items_arrow_container {
  display: flex;
  justify-content: center;
  width: 50px;

}
.request_items_arrow_container_counter {
  position: relative;
  background-color: #835ED2;
  border-radius: 50px;
  width: 20px;
  height: 20px;
  font-weight: 500 !important;
  font-size: 14px !important;
  line-height: 18px !important;
  text-align: center;
  letter-spacing: 0.1px !important;
  color: #FFFFFF;
  right: -6px;

}
.request_items_arrow_container_counter span {
  position: relative;
  top: 1px;
  left: 0.3px;
  font-weight: 500 !important;
}
.expert_grade_container {
  top: 0;
  bottom:0;
  right: 0;
  left: 0;
  position:fixed;
  overflow-y:scroll;
  overflow-x:hidden;
  background-color: #fff;
  z-index: 110;
  background: #00000099;
  display: flex;
  justify-content: center;
  align-items: center;
}
.expert_grade_container_form {
  min-width: 270px;
  min-height: 100px;
  background: #fff;
  padding: 16px 12px;
  border-radius: 10px;
}

.select_expert_container_form_buttons {
  display: flex;
  justify-content: center;
}
.select_expert_container_form_button, .select_expert_container_form_button_cancel {
  padding: 6px 10px;
  width: 86px;
  height: 28px;
  background: #835ED2;
  border-radius: 6px;
  font-size: 10px;
  line-height: 16px;
  display: flex;
  align-items: center;
  letter-spacing: 0.4px;
  color: #FFFFFF;
  text-align: center;
  display: flex;
  justify-content: center;
  margin-top: 20px;
  margin: 20px auto 0px auto;
}

.select_expert_container_form_button_cancel {
  background: #EEE7FF;
  color: #835ED2;
}

.expert_grade_container_label {
  font-size: 16px;
line-height: 24px;
/* identical to box height, or 150% */

display: flex;
align-items: center;
letter-spacing: 0.44px;

color: #000000;
}
.expert_popup {
  border: 3px solid #835ED2;
  border-radius: 12px;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80vw;
  left: 10vw;
  position: fixed;
  bottom: 20vh;
  background: #fff;
}
.expert_popup p {
  margin: 0;
  color: #835ED2;
}
</style>
