<template>
  <div class="book_page">
    <div class="book_page_back" v-on:click="emitHideBookPage()">
      <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M19 26L9 16L19 6" stroke="#835ED2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>

    <div class="addBook" v-if="isInUserBooks || added" v-on:click="popup_message('Уже добавлено')">
    <svg width="18" height="22" viewBox="0 0 18 22" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M15.5 0.4375H2.5C2.06915 0.437926 1.65608 0.609267 1.35142 0.913922C1.04677 1.21858 0.875426 1.63165 0.875001 2.0625V20.75C0.87484 20.8916 0.91171 21.0308 0.981954 21.1537C1.0522 21.2767 1.15337 21.3792 1.27544 21.4509C1.3975 21.5227 1.53622 21.5613 1.67782 21.5629C1.81941 21.5646 1.95897 21.5291 2.08264 21.4601L9 17.6166L15.9174 21.4601C16.041 21.5291 16.1806 21.5646 16.3222 21.5629C16.4638 21.5613 16.6025 21.5227 16.7246 21.4509C16.8466 21.3792 16.9478 21.2767 17.018 21.1537C17.0883 21.0308 17.1252 20.8916 17.125 20.75V2.0625C17.1246 1.63165 16.9532 1.21858 16.6486 0.913921C16.3439 0.609267 15.9308 0.437925 15.5 0.4375Z" fill="#FFCC00"/>
    </svg>
    </div>
    <div class="addBook" v-else v-on:click="addBook(getBookSaveData(book))">
      <svg width="18" height="22" viewBox="0 0 18 22" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.3125 20.75L8.99925 16.6875L1.6875 20.75V2.0625C1.6875 1.84701 1.7731 1.64035 1.92548 1.48798C2.07785 1.3356 2.28451 1.25 2.5 1.25H15.5C15.7155 1.25 15.9222 1.3356 16.0745 1.48798C16.2269 1.64035 16.3125 1.84701 16.3125 2.0625V20.75Z" stroke="#FFCC00" stroke-width="1.625" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
      <div class="book_page_img_container"><img class="book_page_img" v-bind:src=book.preview></div>
      <div class="book_page_authors">
        {{formateAuthors(book.authors)}}
        </div>
      <h4 class="book_page_title">{{book.title}}</h4>
      <p class="book_page_expert" v-if="userBooksDict[book.GoogleId]">
            <span v-if="userBooksDict[book.GoogleId].marked">Подтвердил <span class="book_page_expert_label">{{userBooksDict[book.GoogleId].expert}}</span>
            <svg width="13" height="12" viewBox="0 0 13 12" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.625 3.37524L5.375 8.62501L2.75 6.00024" stroke="#835ED2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            </span>
            <span class="book_page_send_button" v-else-if="!checkSend" v-on:click="showExpertMenu(book.GoogleId)">
             На подтверждение
            </span>
      </p>
      <div class="toogle_sections_container">
          <p>Описание</p>
          <p class="book_page_description">{{book.description}}</p>
          <p><a target="_blank" v-bind:href=createPreviewLink(book.GoogleId)>Ссылка на книгу</a></p>
        </div>
      <div v-if="popup_is_active" class="alert d-flex align-items-center" role="alert">
        <transition name="fade">
          <p>{{popup_msg}}</p>
        </transition>
      </div>
      <div class="select_expert_container" v-if="show_expert_container">
        <div class="select_expert_container_form">
          <h2 class="select_expert_container_form_label">Выберите эксперта</h2>
          <select class="form-select" aria-label="Default select example" v-model="selectedExpert">
            <option  v-for="expert in experts" :key="expert.id" :value="expert.username">{{expert.first_name}} {{expert.last_name}} - {{expert.profile}}</option>
          </select>
          <span class="select_expert_container_form_button" v-on:click="checkKnowledge(selectedExpert, book.GoogleId)">Отправить</span>
        </div>
      </div>
  </div>
</template>

<script>
import bookService from '@/services/bookService.js'
import userService from '@/services/userService.js'

export default {
  name: 'BookPage',
  props: {
    book: Object,
    isInUserBooks: Boolean
  },
  data () {
    return {
      added: false,
      popup_is_active: false,
      popup_msg: '',
      userBooksDict: {},
      show_expert_container: false,
      experts: [],
      selectedExpert: '',
      checkSend: false
    }
  },
  mounted () {
    this.getUserBooks()
  },
  methods: {
    getExperts () {
      bookService.getExperts()
        .then((res) => {
          this.experts = res.data.experts
        })
    },
    getBookById (id) {
      return this.userBooksDict[id]
    },
    getUserBooks: async function () {
      userService.getUserBooks(this.$store.state.user.username)
        .then((resp) => {
          resp.books.forEach(element => {
            console.log(element.GoogleId)
            this.userBooksDict[element.GoogleId] = element
          })
        })
    },
    isEmpty (obj) {
      try {
        return Object.keys(obj).length === 0
      } catch (err) {
        console.log(err)
        return false
      }
    },
    showExpertMenu (bookId) {
      this.show_expert_container = true
      this.getExperts()
    },
    hideExpertMenu () {
      this.show_expert_container = false
    },
    checkKnowledge (expert, bookId) {
      bookService.addMarkRequest(this.$store.state.user.username, bookId, expert)
        .then((res) => {
          this.popup_message('ОТПРАВЛЕНО')
          this.checkSend = true
        })
        .catch(() => {
          this.popup_message('Ошибка, вопторите позже')
        })
      this.hideExpertMenu()
    },
    formateAuthors (authors) {
      if (authors) {
        return authors.toString().replaceAll('[', '').replaceAll(']', '').replaceAll('\'', '')
      } else {
        return ''
      }
    },
    createPreviewLink (id) {
      return 'https://books.google.ru/books?id=' + id
    },
    emitHideBookPage () {
      this.$emit('hideBookPage')
    },
    popup_message (msg) {
      this.popup_msg = msg
      this.popup_is_active = true
      this.delay(2000).then(() => { this.popup_is_active = false })
    },
    addBook (data) {
      const username = this.$store.state.user.username
      bookService.addBook(username, data).then((result) => {
        if (result.status === 200) {
          this.popup_message('Добавлено')
          this.added = true
        } else {
          this.popup_message('Ошибка, повторите попытку позже')
          console.log(result)
        }
      })
    },
    getBookSaveData (book) {
      // ISBN
      const ISBN = this.getISBN(book.industryIdentifiers)

      // etag
      console.log(book)
      console.log(book.preview)
      const GoogleId = this.getUrlVars(book.preview).id
      // title
      const title = book.title

      const description = book.description
      const authors = book.authors
      const preview = book.imageLink
      console.log(GoogleId, ISBN, title)

      return { GoogleId: GoogleId, ISBN: ISBN, title: title, preview: preview, description: description, authors: authors }
    },
    getISBN (arr) {
      try {
        if (arr[0].identifier) {
          return arr[0].identifier
        }
      } catch (e) {
        return ''
      }
    },
    getUrlVars (location) {
      var vars = {}
      location.replace(/[?&]+([^=&]+)=([^&]*)/gi,
        function (m, key, value) {
          vars[key] = value
        })
      return vars
    },
    delay (time) {
      return new Promise(resolve => setTimeout(resolve, time))
    }
  }
}
</script>
<style scoped>
.book_page {
  top: 0;
  bottom:0;
  position:fixed;
  overflow-y:scroll;
  overflow-x:hidden;
  background-color: #fff;
  z-index: 100;
  padding-bottom: 100px;
}
.book_page_back {
  position: absolute;
  top: 27px;
  left: 21px;
}
.book_page_img_container {
  margin-top: 60px;
  max-height: 225px;
  width: 100vw;
}
.book_page_img {
  max-width:100%;
  max-height:100%;
  object-fit: contain;
}
.addBook {
  position: absolute;
  top: 27px;
  right: 21px;
}
.alert {
  position: absolute;
  bottom: 10px;
  left: 10px;
  right: 10px;
  background-color: #ffffff;
  color: #835ED2;
  border: 2px solid #835ed23a;
  border-radius: 30px;
}
.alert p{
  width: 100%;
  margin: 0;
  text-align: center;
}
.fade-enter-active, .fade-leave-active {
  transition-property: opacity, left, top, height;
  transition-duration: 3s, 5s, 3s, 5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active до версии 2.1.8 */ {
  opacity: 0;
}
.book_page_authors {
  font-weight: 400;
  font-size: 12px;
  line-height: 16px;
  align-items: center;
  text-align: center;
  letter-spacing: 0.4px;
  color: rgba(60, 60, 67, 0.6);
  margin-top: 18px;
  margin-bottom: 7px;
}
.book_page_title {
  font-weight: 500;
  font-size: 16px;
  line-height: 20px;
  align-items: center;
  text-align: center;
  letter-spacing: 0.44px;
  margin-left: 48px;
  margin-right: 48px;

  color: #000000;
}
.toogle_sections_container {
  border-top: 1px solid #E5E5EA;;
}
.book_page_description {
  font-weight: 400;
font-size: 14px;
line-height: 20px;
/* or 143% */

display: flex;
align-items: center;
letter-spacing: 0.25px;

/* Label color | Light/Secondary 60% */

color: rgba(60, 60, 67, 0.6);
text-align: left;
margin: 25px 19px;
}

.book_page a {
  color: #835ED2;
  text-decoration: none;
}
.book_page_expert {
  font-size: 12px;
  font-weight: 400;
  line-height: 16px;
  letter-spacing: 0.4px;
  color: rgba(60, 60, 67, 0.3);
}
.book_page_expert_label {
  color: #835ED2;
}

.book_page_expert svg {
  position: relative;
  left: -2px;
  top: -1px;
}
.book_page_send_button {
  position: fixed;
  padding: 19px 60px;
  width: 90vw;
  height: 54px;
  left: 5vw;
  bottom: 34px;
  background: #835ED2;
box-shadow: 0px 24px 32px rgba(131, 94, 210, 0.24);
border-radius: 10px;

font-weight: 500;
font-size: 14px;
line-height: 16px;
letter-spacing: 0.75px;
text-transform: uppercase;
text-align: center;
color: #F2F2F7;
}
.select_expert_container {
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
.select_expert_container_form {
  min-width: 100px;
  min-height: 100px;
  background: #fff;
  padding: 16px 12px;
  border-radius: 10px;
}
.select_expert_container_form_button {
  padding: 6px 10px;
width: 86px;
height: 28px;

background: #835ED2;
border-radius: 6px;
font-size: 10px;
line-height: 16px;
/* identical to box height, or 160% */

display: flex;
align-items: center;
letter-spacing: 0.4px;

/* System/White */

color: #FFFFFF;
text-align: center;
display: flex;
justify-content: center;
margin-top: 20px;
margin: 20px auto 0px auto;
}
.select_expert_container_form_label {
  font-size: 16px;
line-height: 24px;
/* identical to box height, or 150% */

display: flex;
align-items: center;
letter-spacing: 0.44px;

color: #000000;
}
</style>
