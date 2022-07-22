<template>
  <div>
    <div class="achievement">
      <div class="achievement-header">
        <svg @click="closeAchievementForm" width="12" height="22" viewBox="0 0 12 22" fill="none"
          xmlns="http://www.w3.org/2000/svg">
          <path d="M11 21L1 11L11 1" stroke="#835ED2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
        <div class="achievement-header__title">Добавить достижения</div>
        <div class="achievement-header__subtitle">Готово</div>
      </div>
      <form class="form">
        <fieldset class="form-fieldset">
          <input class="form__input" placeholder="Убийца строк" type="text" name="" id="">
          <label class="form__label-small">
            Название
          </label>
        </fieldset>
        <fieldset class="form-fieldset">
          <label class="form__label" for="description">
            Краткое описание
          </label>
          <textarea class="form__input"
            placeholder="Введите краткое описание достижения, напимер, за какие успехи оно дается" name="description"
            id="description" rows="3" cols="30"></textarea>
        </fieldset>
        <fieldset class="form-fieldset">
          <span class="form__label">
            Иконка
          </span>
          <input type="file" @change="setFilename" name="" id="upload-file" required>
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
          <span class="form__label-small">Файл должен быть формата JPEG или PNG и весом не более <em>50Мб</em>
          </span>
        </fieldset>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      filename: null
    }
  },
  methods: {
    closeAchievementForm () {
      this.$emit('close-achievement-form')
    },
    setFilename (e) {
      const filelist = [...e.target.files]
      console.log(filelist)
      this.filename = filelist.pop().name
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
      cursor: pointer;
    }
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
}

input[type=file] {
  display: none;
}

textarea {
  resize: none;
}
</style>
