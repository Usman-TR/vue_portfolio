<template>
  <div class="spec">
    <div class="spec-header">
      <svg @click="closeSpecForm" width="12" height="22" viewBox="0 0 12 22" fill="none"
        xmlns="http://www.w3.org/2000/svg">
        <path d="M11 21L1 11L11 1" stroke="#835ED2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
      </svg>
      <div class="spec__title">Добавить специализацию</div>
      <div class="spec__subtitle">Готово</div>
    </div>
    <form class="form" action="#">
      <fieldset class="form-fieldset">
        <input class="form__input" placeholder="Автоматизация ИС" type="text" name="name" id="name">
        <label for="name" class="form__label-small">
          Название
        </label>
      </fieldset>
      <fieldset class="form-fieldset">
        <label class="form__label" for="description">
          Краткое описание
        </label>
        <textarea class="form__input" placeholder="Надпись более длинная по содержанию, чем обычная короткая запись"
          name="description" id="description" rows="3" cols="30"></textarea>
      </fieldset>
      <fieldset class="form-fieldset">
        <label class="form__label">
          Выберите достижения для этой специальности
        </label>
        <div class="form__select">
          <div @click="isSelectOpen = !isSelectOpen" class="form__select-visible">
            <div class="selected">{{ selected }}</div>
            <span>
              <svg :class="{ open: isSelectOpen }" width="20" height="20" viewBox="0 0 20 20" fill="none"
                xmlns="http://www.w3.org/2000/svg">
                <path d="M16.25 7.5L10 13.75L3.75 7.5" stroke="#B195EB" stroke-width="2" stroke-linecap="round"
                  stroke-linejoin="round" />
              </svg>
            </span>
          </div>
          <ul class="form__select-items" :class="{ 'form__select_hidden': !isSelectOpen }">
            <li class="form__select__item" @click="selectItem(option)" v-for="option in options" :key="option">{{ option
            }}</li>
          </ul>
        </div>
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
    </form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isSelectOpen: false,
      selected: 'Убийца строк',
      options: ['Убийца крок', 'Первопроходец', 'Второпроходец', 'Чел ты..']
    }
  },
  methods: {
    closeSpecForm () {
      this.$emit('close-spec-form')
    },
    selectItem (selected) {
      this.selected = selected
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

    & .selected {
      color: #000;
      font-size: 1rem;
    }

    &-items {
      padding: 0;
      margin: 0;
      list-style: none;
      position: absolute;
      left: 0;
      right: 0;
      z-index: 2;
      background-color: #FAF7FF;
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
        background-color: #d7c3fa;
      }
    }
  }
}

.open {
  transform: rotate(180deg);
}
</style>
