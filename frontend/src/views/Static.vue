<template>
  <div class="static">
    <h5 class="static__title">Статистика</h5>
    <ul>
      <StaticItem
        v-for="item in staticItems"
        :staticItem="item"
        :key="item.id"
      />
    </ul>
  </div>
</template>

<script>
import StaticItem from '../components/StaticItem.vue'
export default {
  components: { StaticItem },
  data () {
    return {
      staticItems: [
        {
          id: 1,
          title: 'Информационные технологии',
          status: 'Прочитано',
          progress: 25,
          pages: '54/300'
        },
        {
          id: 2,
          title: 'Машинное обучение',
          status: 'Читаю',
          progress: 48,
          pages: '222/224'
        },
        {
          id: 3,
          title: 'Промышленные технологии',
          status: 'Прочитано',
          progress: 100,
          pages: '59/152'
        },
        {
          id: 4,
          title: 'Информационные технологии',
          status: 'Прочитано',
          progress: 90,
          pages: '54/300'
        },
        {
          id: 5,
          title: 'Машинное обучение',
          status: 'Читаю',
          progress: 12,
          pages: '222/224'
        },
        {
          id: 6,
          title: 'Промышленные технологии',
          status: 'Прочитано',
          progress: 33,
          pages: '59/152'
        },
        {
          id: 51,
          title: 'Машинное обучение',
          status: 'Читаю',
          progress: 65,
          pages: '222/224'
        },
        {
          id: 62,
          title: 'Промышленные технологии',
          status: 'Прочитано',
          progress: 75,
          pages: '59/152'
        }
      ]
    }
  }
}
</script>

<style scoped>
ul {
  padding: 0;
}

.static {
  padding: 1rem;
}

.static__title {
  text-align: start;
  font-size: 24px;
  line-height: 28px;
  font-weight: 400;
  margin-bottom: 1rem;
}

.btn {
  color: #835ed2;
}
</style>
