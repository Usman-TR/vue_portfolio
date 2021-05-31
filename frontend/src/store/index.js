import { createStore } from 'vuex'
import userbooks from './modules/userbooks'
import userService from '../services/userService'

export default createStore({
  state: {
    user: { username: 'admin' }
  },
  mutations: {
    setUser (state, user) {
      state.user = user
      console.log(state.user)
    }
  },
  actions: {
    getUser ({ commit }) {
      userService.fetchUser(this.state.user.username)
        .then(user => {
          commit('setUser', user)
        })
    }
  },
  modules: {
    userbooks
  }
})
