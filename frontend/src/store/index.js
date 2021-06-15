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
    token: localStorage.getItem('token') || '',
    authStatus: 'default'
  },
  getters: {
    user: state => state.user,
    token: state => state.token,
    isLoggedIn: state => !!state.token,
    authStatus: state => state.authStatus
  },
  mutations: {
    setUser (state, user) {
      state.user = Object.assign(state.user, user)
    },
    setToken (state, token) {
      state.token = token
    },
    authStatusLoading (state) {
      state.auth_status = 'loading'
    },
    authStatusSuccess (state) {
      state.auth_status = 'success'
    },
    authStatusError (state) {
      state.auth_status = 'error'
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
      commit('authStatusLoading', { root: true })
      userService.login(data)
        .then(result => {
          console.log('login in store')
          if (result.key.length > 1) {
            console.log('login in store key len > 1')
            data.authentificated = true
            const authUser = { username: data.username, authentificated: true }
            commit('setToken', result.key, { root: true })
            commit('setUser', authUser, { root: true })
            commit('authStatusSuccess', { root: true })
          } else {
            console.log('login in store key len <= 1')
            commit('authStatusError')
          }
        })
    },
    logout ({ commit }, data) {
      localStorage.clear()
      const emptyUser = { username: 'user', authentificated: false, is_expert: false }
      commit('setUser', emptyUser, { root: true })
    },
    register ({ commit }, data) {
      userService.register(data)
        .then(result => {
          console.log('register in store')
        })
    }
  },
  modules: {
    userbooks
  }
})
