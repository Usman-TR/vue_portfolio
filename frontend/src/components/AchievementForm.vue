<template>
  <div>
    <div class="achievement">
      <div class="achievement-header">
        <svg @click="closeAchievementForm" width="12" height="22" viewBox="0 0 12 22" fill="none"
          xmlns="http://www.w3.org/2000/svg">
          <path d="M11 21L1 11L11 1" stroke="#835ED2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
        <div class="achievement-header__title">Добавить достижения</div>
        <!-- <div class="achievement-header__subtitle" v-on:click="sendData()">Готово</div> -->
        <div class="achievement-header__subtitle"></div>
      </div>
      <div v-if="popup_is_active" class="alert d-flex align-items-center popup" role="alert">
      <transition name="fade">
        <p>{{ popup_msg }}</p>
      </transition>
      </div>
      <form class="form"  @submit.prevent="sendData">
        <button id="submit_button">Готово</button>
        <fieldset class="form-fieldset">
          <input class="form__input" required placeholder="Убийца строк" type="text" name="" id="" v-model="title">
          <label class="form__label-small">
            Название
          </label>
        </fieldset>
        <fieldset class="form-fieldset">
          <label class="form__label" for="description">
            Краткое описание
          </label>
          <textarea class="form__input" v-model="description" required
            placeholder="Введите краткое описание достижения, напимер, за какие успехи оно дается" name="description"
            id="description" rows="3" cols="30"></textarea>
        </fieldset>
        <fieldset class="form-fieldset">
          <span class="form__label">
            Иконка
          </span>
          <span class="alert_val" v-if="showFileMsg && !filename">Загрузите иконку</span>
          <img class="file-img" v-if="file" :src="fileObj" alt="no img">
          <input type="file" accept="image/png, image/jpeg" name="upload-file" @change="setFilename" id="upload-file">
          <label class="form__input-file" for="upload-file" v-if="filename">
            <span>
              <svg width="24" height="24" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M10.125 3.37524L4.875 8.62501L2.25 6.00024" stroke="#835ED2" stroke-linecap="round"
                  stroke-linejoin="round" />
              </svg>
            </span> {{ filename }}</label>
          <label v-else class="form__input-file" for="upload-file">
            <span><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 21.0004V6.75037" stroke="#835ED2" stroke-width="1.5" stroke-linecap="round"
                  stroke-linejoin="round" />
                <path d="M5.25 13.5004L12 6.75037L18.75 13.5004" stroke="#835ED2" stroke-width="1.5"
                  stroke-linecap="round" stroke-linejoin="round" />
                <path d="M3.75 3.75H20.25" stroke="#835ED2" stroke-width="1.5" stroke-linecap="round"
                  stroke-linejoin="round" />
              </svg></span>
            Загрузить фотографию
          </label>
          <span class="form__label-small">Файл должен быть формата JPEG или PNG и весом не более <em>5 Мб</em>
          </span>
        </fieldset>
        <fieldset class="form-fieldset">
          <label class="form__label" for="description">
            <span v-if="selectedBooks.length === 0" class="invalid">Выбранные Книги ({{selectedBooks.length}})</span>
            <span v-else>Выбранные Книги ({{selectedBooks.length}})</span>
            <span class="selectedlist_toogle" v-if="selectedBooks.length" v-on:click="show_full = !show_full">
              <span v-if="!show_full">Показать все</span>
              <span v-else>Показать меньше</span>
            </span>
          </label>
          <div class="form__list" v-if="show_full">
            <div class="form__list_item" v-for="book in selectedBooks" :key="book.id">
              <div class="form__list_image">
                <img v-if="book.imageLink" top v-bind:src="book.imageLink" class="img-fluid" />
                <img v-else src="../assets/default-book.png">
              </div>
              <div class="form__list_item_labels">
                <p class="form__list_item_labels_title"><a :href="book.previewLink" target="_blank">{{cutText(book.title, 40)}}</a></p>
                <p class="form__list_item_labels_authors" v-if="book.authors">
                  {{ cutText(book.authors.join(", "), 100) }}
                </p>
                <p class="form__list_item_labels_date">{{cutText(book.publishedDate)}}</p>
                <p class="form__list_item_labels_button" v-on:click="deleteBook(book)">Удалить</p>
              </div>
            </div>

          </div>

          <input class="form__input" v-model="searchSeq" @input="search_books({ text: searchSeq, page: searchPage })"
            placeholder="Введите название книги для поиска" name="search"
            id="search" rows="3" cols="30">

          <div class="form__list">
            <div class="form__list_item" v-for="book in searchedBooks" :key="book.id">
              <div class="form__list_image">
                <img v-if="book.imageLink" top v-bind:src="book.imageLink" class="img-fluid" />
                <img v-else src="../assets/default-book.png">
              </div>
              <div class="form__list_item_labels">
                <p class="form__list_item_labels_title"><a :href="book.previewLink" target="_blank">{{cutText(book.title, 40)}}</a></p>
                <p class="form__list_item_labels_authors" v-if="book.authors">
                  {{ cutText(book.authors.join(", "), 100) }}
                </p>
                <p class="form__list_item_labels_date">{{cutText(book.publishedDate)}}</p>
                <p class="form__list_item_labels_button" v-on:click="selectBook(book)">Добавить</p>
              </div>
            </div>
          </div>
        </fieldset>
      </form>
    </div>
  </div>
</template>

<script>
import bookService from '@/services/bookService.js'

export default {
  data () {
    return {
      show_full: false,
      title: '',
      description: '',
      popup_is_active: false,
      popup_msg: '',
      filename: '',
      file: null,
      fileObj: null,
      searchSeq: '',
      searchPage: 0,
      searchedBooks: [],
      selectedBooks: [],
      showFileMsg: false
    }
  },
  methods: {
    isAddButtonActive (book) {
      this.selectedBooks.forEach(element => {
        if ((element.title === book.title && element.publishedDate === book.publishedDate)) {
          return false
        }
      })
      return true
    },
    popup_message (msg) {
      this.popup_msg = msg
      this.popup_is_active = true
      this.delay(2000).then(() => { this.popup_is_active = false })
    },
    delay (time) {
      return new Promise(resolve => setTimeout(resolve, time))
    },
    deleteBook (book) {
      const filtered = []
      this.selectedBooks.forEach(element => {
        if (!(element.title === book.title && element.publishedDate === book.publishedDate)) {
          filtered.push(element)
        }
      })
      this.selectedBooks = filtered
    },
    selectBook (book) {
      try {
        if (!this.selectedBooks.includes(book)) {
          this.selectedBooks.push(book)

          const index = this.searchedBooks.indexOf(book)
          if (index > -1) { // only splice array when item is found
            this.searchedBooks.splice(index, 1) // 2nd parameter means remove one item only
          }
        }
      } catch (err) {
        console.log(err)
      }
    },
    getBookSaveData (book) {
      const ISBN = this.getISBN(book.industryIdentifiers)
      const GoogleId = this.getUrlVars(book.previewLink).id
      const title = book.title
      const description = book.description
      const authors = book.authors
      const preview = book.imageLink
      const language = book.language
      const publishedDate = book.publishedDate.slice(0, 4)
      const publisher = book.publisher
      return { GoogleId, ISBN, title, preview, description, authors, language, publishedDate, publisher }
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
    sendData () {
      console.log('sending achievements data')
      this.showFileMsg = true

      if (!this.filename) {
        this.popup_message('Загрузите изображение')
        return -1
      }

      if (!this.selectedBooks.length) {
        this.popup_message('Выберите книги')
        return -1
      }

      const saveBooksData = []

      this.selectedBooks.forEach(book => {
        saveBooksData.push(this.getBookSaveData(book))
      })

      bookService.addAchievement(
        {
          title: this.title,
          description: this.description,
          books: saveBooksData,
          file: this.file
        })
        .then((res) => {
          console.log('sendData', res)
          if (res.data.status === 'exists') {
            this.popup_message('Уже существует')
          } else if (res.data.status === 'done') {
            this.popup_message('Добавлено')
          } else {
            console.log(res)
            this.popup_message(res)
            this.popup_message('Ошибка')
          }
        })
        .catch((err) => {
          console.log(err)
          this.popup_message('Ошибка')
        })
    },
    cutText (str, len = 40) {
      if (String(str).length > len) {
        return str.slice(0, len) + '...'
      }
      return String(str).slice(0, len)
    },
    async search_books (obj) {
      const text = obj.text
      const url = 'https://www.googleapis.com/books/v1/volumes?q='
      const params = `&maxResults=25&startIndex=${obj.page * 15}`
      if (text) {
        const searchSeq = String(text).replaceAll('  ', ' ').replaceAll(' ', '+')
        const response = await fetch(url + searchSeq + params)
        if (response.ok) {
          const json = await response.json()
          const volume = json.items
          const exportBooks = bookService.parse_volume(volume)
          console.log('exportBooks', exportBooks.length, exportBooks)

          const filtered = []
          exportBooks.forEach(element => {
            const contains = this.selectedBooks.some(elem => {
              return JSON.stringify(element) === JSON.stringify(elem)
            })

            if (!contains) {
              filtered.push(element)
            }
          })
          this.searchedBooks = filtered
        } else {
          console.log(response)
        }
      }
    },
    closeAchievementForm () {
      this.$emit('close-achievement-form')
    },
    setFilename (e) {
      const filelist = [...e.target.files]
      this.file = filelist.pop()
      this.filename = this.file.name
      if (this.file) {
        const reader = new FileReader()
        reader.readAsDataURL(this.file)
        reader.onload = () => {
          this.fileObj = reader.result
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.achievement {
  padding: 30px 13px 0;
  width: 100%;

  &-header {
    display: flex;
    justify-content: space-between;
    letter-spacing: 0.44px;
    font-size: 1rem;
    align-items: center;

    & svg {
      cursor: pointer;
    }

    &__subtitle {
      color: #835ED2;
      // cursor: pointer;
      width: 70px;
    }
  }
}

.invalid {
  color: red;
}

.form {
  margin-top: 2rem;

  &-fieldset {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin: 24px 0;
  }

  &__label {
    display: flex;
    justify-content: space-between;
    font-size: .875rem;
    line-height: 20px;
    letter-spacing: 0.25px;
    color: rgba(60, 60, 67, 0.6);
    margin-bottom: 20px;

    &-small {
      color: rgba(60, 60, 67, 0.6);
      font-size: .75rem;
      line-height: 16px;
      letter-spacing: 0.4px;
      text-align: start;
    }
  }

  &__input {
    padding: 8px;
    font-size: 1rem;
    color: #9788B8;
    border: 0.5px solid #DACAFC;
    border-radius: 6px;
    background: #FAF7FF;
    width: 100%;
    margin: 8px 0;

    &:hover {
      border-color: #ae8cf7;
      background-color: #fff;
    }

    &::placeholder {
      color: #9788B8;
      opacity: 1;
    }

    &:focus {
      background-color: #fff;
      outline: 1px solid #835ED2;

      &::placeholder {
        color: #9788B8;
        opacity: .6;
      }
    }

    &-file {
      width: 100%;
      border: 1.5px solid #835ED2;
      border-radius: 6px;
      padding: 18px 0;
      color: #835ED2;
      font-size: 1rem;
      cursor: pointer;
      background-color: #fff;
      margin: 8px 0;

      &:hover {
        color: #fff;
        background-color: #835ED2;

        & svg path {
          stroke: #fff;
        }
      }
    }
  }

  &__list {
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
    align-items: center;
    gap: 12px;

    a {
      text-decoration: none;
      color: #000;
    }

    &_item {
      font-size: 14px !important;
      color: rgba(60, 60, 67, 0.6);;
      border: 0px solid #DACAFC;
      border-radius: 6px;
      box-shadow: 0px 4px 8px rgba(176, 65, 118, 0.26);
      height: 150px;

      margin-bottom: 12px;

      display: flex;
      justify-content: space-between;
      align-items: flex-start;

        &_labels{
          display: flex;
          flex-flow: column nowrap;
          justify-content: space-between;
          height: 150px;
          width: 200px;

          &_title {
            height: 40px;
            margin-bottom: 0;
            color: red !important;
          }

          &_authors {
            height: 30px;
            margin: 0;
            line-height: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
          }

          &_date {
            height: 20px;
            margin: 0;
          }

          &_button {
            margin: 0;
            padding: 6px 8px;
            border: 0.5px solid #DACAFC;
            border-radius: 6px;
            width: 120px;
            margin: 8px auto;
            user-select: none;

            &:hover, &:active {
              // border-color: #ae8cf7;
              color: #fff;
              background-color: #ae8cf7;
              cursor: pointer;
            }
          }
        }

        img {
          max-height: 150px;
          max-width: 100px;
        }

    }

    &_image{
        display: flex;
        justify-content: center;
        align-items: center;
      }

  }
}

input[type=file] {
  display: none;
}

.file-img {
  width: 100%;
  height: 100%;
  margin: 8px 0;
}

textarea {
  resize: none;
}

#submit_button {
  position: absolute;
  top: 30px;
  right: 20px;

  outline: none;
  border: none;
  color: #835ED2;
  background: #fff;

  &:hover, &:active {
    background: #ae8cf7;
    color: #fff;
    border-radius: 6px;
  }

}
.selectedlist_toogle {
  position: absolute;
  right: 20px;
  color: #835ED2;
}

.popup {
  border: 0.5px solid #FF2D55;
  background: #ff2d5390;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  position: fixed;
  top: 10vh;
  left: 4vw;
  width: 92vw;
}
.popup * {
  margin: 0;
  padding: 0;
}
.alert_val {
  color: #FF2D55;
}
</style>
