import { createStore } from 'vuex'
import userbooks from './modules/userbooks'

export default createStore({
  state: {
    username: 'Admin',
    is_expert: true
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    userbooks
  }
})
