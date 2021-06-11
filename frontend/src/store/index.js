import { createStore } from 'vuex'
import userbooks from './modules/userbooks'
import userService from '../services/userService'
import createPersistedState from 'vuex-persistedstate'

export default createStore({
  plugins: [createPersistedState({
    storage: window.sessionStorage
  })],
  state: {
    user: { username: 'admin' }
  },
  mutations: {
    setUser (state, user) {
      state.user = user
    }
  },
  actions: {
    getUser ({ commit }) {
      userService.fetchUser(this.state.user.username)
        .then(user => {
          console.log(user)
          commit('setUser', user, { root: true })
        })
    }
  },
  modules: {
    userbooks
  }
})
