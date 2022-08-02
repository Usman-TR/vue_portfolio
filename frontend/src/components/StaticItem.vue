<template>
  <div class="static-item">
    <div class="static-item__title">{{ staticItem.title }}</div>
    <div class="static-item-content">
      <div class="progressbar">
        <div class="progressbar__graded" :style="{ width: gradedProgress }"></div>
        <div class="progressbar__ungraded" :style="{ width: ungradedProgress }"></div>
      </div>
      <div class="static-item__label">Прочитано
      </div>
      <div class="static-item__label">{{ `${staticItem.graded}/${staticItem.allPages}` }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    staticItem: {
      type: Object,
      required: true
    }
  },
  computed: {
    gradedProgress () {
      return ((this.staticItem.graded / this.staticItem.allPages) * 100) + '%'
    },
    ungradedProgress () {
      return ((this.staticItem.currentPage / this.staticItem.allPages) * 100) + '%'
    }
  }
}
</script>

<style scoped lang="scss">
.static-item {
  padding: 8px 15px 10px;
  border-radius: 8px;
  height: 80px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-bottom: 15px;
}

.static-item__title {
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0.25px;
  margin-right: auto;
}

.static-item-content {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.static-item__label {
  letter-spacing: 0.4px;
  font-size: 12px;
  line-height: 16px;
}

.progressbar {
  width: 100%;
  position: relative;
  height: 5px;
  border-radius: 12px;
  margin-bottom: 7px;
}

.progressbar__graded {
  position: absolute;
  height: 5px;
  left: 0;
  border-radius: 12px;
  z-index: 10;
}

.progressbar__ungraded {
  position: absolute;
  height: 5px;
  left: 0;
  border-radius: 12px;
  z-index: 5;
}

.static-item:nth-child(1n) {
  border: 1px solid #dacafc;
  background: #F5F0FF;

  & .static-item__title {
    color: #835ed2;
  }

  & .progressbar {
    background-color: #dacafc;

    &__graded {
      background-color: #835ed2;
    }
    &__ungraded {
      background-color: #835ed24e;

    }
  }

  & .static-item__label {
    color: #b195eb;
  }
}

.static-item:nth-child(2n) {
  background: #FFF4E6;
  border: 1px solid #F2DEC2;

  & .static-item__title {
    color: #FF9500;
  }

  & .progressbar {
    background-color: #F9DCB4;

    &__graded {
      background-color: #FF9500;
    }
    &__ungraded {
      background-color: #ff950057;
    }
  }

  & .static-item__label {
    color: #F4BE71;
  }
}

.static-item:nth-child(3n) {
  background: #E7FFED;
  border: 1px solid #5ECC8D;

  & .static-item__title {
    color: #219653;
  }

  & .progressbar {
    background-color: #AFF0C5;

    &__graded {
      background-color: #219653;
    }
    &__ungraded {
      background-color: #21965451;
    }
  }

  & .static-item__label {
    color: #5ECC8D;
  }
}
</style>
