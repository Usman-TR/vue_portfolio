import { createStore } from 'vuex'
import userbooks from './modules/userbooks'
import userService from '../services/userService'
import createPersistedState from 'vuex-persistedstate'

export default createStore({
  plugins: [createPersistedState({
    storage: window.sessionStorage
  })],
  state: {
    user: { username: 'user', authentificated: false, is_expert: false },
    token: localStorage.getItem('token') || ''
  },
  mutations: {
    setUser (state, user) {
      state.user = Object.assign(state.user, user)
    },
    setToken (state, token) {
      state.token = token
    }
  },
  actions: {
    getUser ({ commit }) {
      userService.fetchUser(this.state.user.username)
        .then(user => {
          console.log('getUser in store')
          console.log(user)
          commit('setUser', user, { root: true })
        })
    },
    login ({ commit }, data) {
      userService.login(data)
        .then(result => {
          console.log('login in store')
          console.log(result)
          if (result.key.length > 1) {
            data.authentificated = true
            const authUser = { username: data.username, authentificated: true }
            commit('setToken', result.key, { root: true })
            commit('setUser', authUser, { root: true })
          }
        })
    },
    logout ({ commit }, data) {
      localStorage.clear()
      const emptyUser = { username: 'user', authentificated: false, is_expert: false }
      commit('setUser', emptyUser, { root: true })
    }
  },
  modules: {
    userbooks
  }
})
