import { createStore } from 'vuex'
import userbooks from './modules/userbooks'
import api from '../services/api'
import userService from '../services/userService'
// import bookService from '../services/bookService'
import createPersistedState from 'vuex-persistedstate'

export default createStore({
  plugins: [createPersistedState({
    storage: window.sessionStorage
  })],
  state: {
    user: { username: 'user', authentificated: false, expert: false },
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
      console.log('setUser in store', user)
      state.user = Object.assign(state.user, user)
    },
    setToken (state, token) {
      state.token = token
    },
    authStatusLoading (state) {
      console.log('auth_status = loading')
      state.authStatus = 'loading'
    },
    authStatusSuccess (state) {
      console.log('auth_status = success')
      state.authStatus = 'success'
    },
    authStatusError (state) {
      console.log('auth_status = error')
      state.authStatus = 'error'
    },
    setAuthStatusDefault (state) {
      state.authStatus = 'default'
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
      // this.dispatch('userbooks/getBooks')
    },
    login ({ commit }, data) {
      commit('authStatusLoading', { root: true })
      userService.login(data)
        .then(result => {
          console.log('login in store', result)
          if (result.key.length > 1) {
            api.defaults.headers.common.token = result.key
            data.authentificated = true
            const authUser = { username: data.username, authentificated: true }
            // login form data console.log(data)

            commit('setToken', result.key, { root: true })
            commit('setUser', authUser, { root: true })
            commit('authStatusSuccess', { root: true })
            this.dispatch('getUser')
          } else {
            console.log('login in store key len <= 1')
            commit('authStatusError')
          }
        })
        .catch(() => {
          commit('authStatusError')
        }
        )
    },
    logout ({ commit }, data) {
      localStorage.clear()
      const emptyUser = { username: 'user', authentificated: false, expert: false }
      commit('setUser', emptyUser, { root: true })
    },
    resetAuthStatus ({ commit }) {
      commit('setAuthStatusDefault')
    }
  },
  modules: {
    userbooks
  }
})
