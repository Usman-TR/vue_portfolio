<template>
  <div class="book_page">
    <div class="book_page_back" v-on:click="emitHideBookPage()">
      <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M19 26L9 16L19 6" stroke="#835ED2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
    <div class="addBook" v-on:click="addBook(getBookSaveData(book))">
      <svg width="18" height="22" viewBox="0 0 18 22" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.3125 20.75L8.99925 16.6875L1.6875 20.75V2.0625C1.6875 1.84701 1.7731 1.64035 1.92548 1.48798C2.07785 1.3356 2.28451 1.25 2.5 1.25H15.5C15.7155 1.25 15.9222 1.3356 16.0745 1.48798C16.2269 1.64035 16.3125 1.84701 16.3125 2.0625V20.75Z" stroke="#FFCC00" stroke-width="1.625" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
      <div class="book_page_img_container"><img class="book_page_img" v-bind:src=book.preview></div>
      <div class="book_page_authors">
        {{formateAuthors(book.authors)}}
        </div>
      <h4 class="book_page_title">{{book.title}}</h4>
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
  </div>
</template>

<script>
import bookService from '@/services/bookService.js'

export default {
  name: 'BookPage',
  props: {
    book: Object
  },
  data () {
    return {
      added: false,
      popup_is_active: false,
      popup_msg: ''

    }
  },
  methods: {
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
</style>
