<template>
  <div class="spec">
    <div class="spec-header">
      <svg @click="closeSpecForm" width="12" height="22" viewBox="0 0 12 22" fill="none"
        xmlns="http://www.w3.org/2000/svg">
        <path d="M11 21L1 11L11 1" stroke="#835ED2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
      </svg>
      <div class="spec__title">Добавить специализацию</div>
      <!-- <div class="spec__subtitle" v-on:click="sendForm">Готово</div> -->
      <div class="spec__subtitle"></div>
    </div>
    <div v-if="popup_is_active" class="alert d-flex align-items-center popup" role="alert">
      <transition name="fade">
        <p>{{ popup_msg }}</p>
      </transition>
    </div>
    <form class="form" @submit.prevent="sendForm">
      <fieldset class="form-fieldset">
        <!-- <input class="form__input" v-model="title" placeholder="Автоматизация ИС" type="text" name="name" id="name"> -->
        <input :class="{'input-error': v$.title.$errors.length && title.length}" class="form__input" required v-model="title" type="text" placeholder="Название" />
        <label for="name" class="form__label-small">
          Название
        </label>
      </fieldset>
      <fieldset class="form-fieldset">
        <label class="form__label" for="description">
          Краткое описание
        </label>
        <textarea v-model="description" :class="{'input-error': v$.description.$errors.length && description.length}" class="form__input" required placeholder="Описание"
          name="description" id="description" rows="3" cols="30"></textarea>
      </fieldset>
      <fieldset class="form-fieldset">
        <label class="form__label">
          Выберите достижения для этой специальности
        </label>
        <div class="form__select">
          <div @click="isSelectOpen = !isSelectOpen" class="form__select-visible">
            <div class="selected">
              {{ selected.length ? selected.map(item => item.title).join(', ') : '' }}
            </div>
            <span>
              <svg :class="{ open: isSelectOpen }" width="20" height="20" viewBox="0 0 20 20" fill="none"
                xmlns="http://www.w3.org/2000/svg">
                <path d="M16.25 7.5L10 13.75L3.75 7.5" stroke="#B195EB" stroke-width="2" stroke-linecap="round"
                  stroke-linejoin="round" />
              </svg>
            </span>
          </div>
          <ul class="form__select-items" :class="{ 'form__select_hidden': !isSelectOpen }">
            <li class="form__select__item" :class="{ 'form__select__item_selected': selected.includes(option) }"
              @click="selectItem(option)" v-for="option in options" :key="option.id">
              {{ option.title }}
            </li>
          </ul>
        </div>
        <div @click.stop="isSelectOpen = false" v-if="isSelectOpen" class="form__select-container"></div>
        <button @click="$emit('switch-to-achievement-form')" type="button" class="form__btn">
          Добавить достижение
          <span>
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M3.125 10H16.875" stroke="#835ED2" stroke-width="1.5" stroke-linecap="round"
                stroke-linejoin="round" />
              <path d="M10 3.125V16.875" stroke="#835ED2" stroke-width="1.5" stroke-linecap="round"
                stroke-linejoin="round" />
            </svg>
          </span>
        </button>
      </fieldset>
      <button class="form__btn_submit" type="submit">Добавить</button>
    </form>
  </div>
</template>

<script>
import bookService from '@/services/bookService.js'
import useVuelidate from '@vuelidate/core'
import { required } from '@vuelidate/validators'

export default {
  data () {
    return {
      popup_is_active: false,
      popup_msg: '',
      title: '',
      description: '',
      isSelectOpen: false,
      selected: [],
      options: [
        { id: 1, title: 'Убийца крок' },
        { id: 2, title: 'Первопроходец' },
        { id: 3, title: 'Второпроходец' }
      ]
    }
  },
  validations () {
    return {
      title: { required },
      options: { required },
      description: { required },
      selected: { required }
    }
  },
  setup () {
    return {
      v$: useVuelidate()
    }
  },
  mounted () {
    this.loadOptions()
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
    async sendForm () {
      const isFormCorrect = await this.v$.$validate()

      console.log('sendForm', isFormCorrect)

      if (!isFormCorrect) return

      bookService.addProfile(
        {
          title: this.title,
          description: this.description,
          achievements: this.selected
        })
        .then((res) => {
          console.log('sendForm', res)
          if (res.data.status === 'exists') {
            this.popup_message('Уже существует')
          } else if (res.data.status === 'done') {
            this.popup_message('Добавлено')
          } else {
            console.log(res)
            this.popup_message('Ошибка')
          }
        })
        .catch((err) => {
          console.log(err)
          this.popup_message('Ошибка')
        })
    },
    loadOptions () {
      bookService.getAllAchievements(this.$store.state.user.username)
        .then((res) => {
          this.options = res.data
        })
    },
    closeSpecForm () {
      this.$emit('close-spec-form')
    },
    selectItem (selected) {
      if (this.selected.includes(selected)) {
        this.selected.splice(this.selected.indexOf(selected), 1)
      } else {
        this.selected.push(selected)
      }
      this.isSelectOpen = false
    }
  }
}
</script>

<style lang="scss" scoped>
.spec {
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
  }

  &__subtitle {
    color: #835ED2;
    cursor: pointer;
  }
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
    font-size: .875rem;
    line-height: 20px;
    letter-spacing: 0.25px;
    color: rgba(60, 60, 67, 0.6);

    &-small {
      color: rgba(60, 60, 67, 0.6);
      font-size: .75rem;
      line-height: 16px;
      letter-spacing: 0.4px;
      text-align: start;
    }
  }

  &__btn {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 2px dashed #DACAFC;
    border-radius: 6px;
    padding: 12px;
    font-size: 1rem;
    color: #9788B8;
    width: 100%;
    background-color: #fff;

  }

  &__btn_submit {
    display: flex;
    justify-content: center;
    align-items: center;
    border: 2px solid #FF2D55;
    padding: 16px;
    font-size: 1rem;
    color: #F2F2F7;
    width: 100%;
    background-color: #FF2D55;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 500;
    line-height: 16px;
    letter-spacing: 0.75px;
    text-transform: uppercase;
    box-shadow: 0px 24px 32px rgba(255, 45, 85, 0.24);
    border-radius: 10px;

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
  }

  &__select {
    position: relative;
    width: 100%;
    background: #FAF7FF;
    border: 0.5px solid #DACAFC;
    border-radius: 6px;
    padding: 12px;
    margin: 8px 0 18px;

    &-visible {
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
    }

    &_hidden {
      display: none;
    }

    &-container {
      position: absolute;
      left: 0;
      right: 0;
      bottom: 0;
      top: 0;
    }

    & .selected {
      color: #000;
      font-size: 1rem;
    }

    &-items {
      padding: 0;
      margin: 0;
      margin-top: 7px;
      list-style: none;
      position: absolute;
      left: -1px;
      right: -0.5px;
      z-index: 2;
      background-color: #fcfafa;
      border-radius: 0 0 6px 6px;
      border-bottom: 0.5px solid #DACAFC;
      border-left: 0.5px solid #DACAFC;
      border-right: 0.5px solid #DACAFC;
    }

    &__item {
      text-align: left;
      cursor: pointer;
      padding: 8px 12px;

      &:hover {
        background-color: #EBE8E8;
      }

      &_selected {
        background-color: #BDBBBB;
        opacity: .7;

        &:hover {
          background-color: #BDBBBB;
        }
      }
    }
  }
}

.open {
  transform: rotate(180deg);
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
</style>
