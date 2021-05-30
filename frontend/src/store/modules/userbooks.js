import userService from '../../services/userService'

const state = {
  books: []
}

const getters = {
  books: state => {
    return state.books
  }
}

const actions = {
  getBooks ({ commit }) {
    userService.fetchBooks()
      .then(books => {
        commit('setbooks', books)
      })
  },
  addbook ({ commit }, book) {
    userService.postBook(book)
      .then(() => {
        commit('addbook', book)
      })
  },
  deletebook ({ commit }, msgId) {
    userService.deleteBook(msgId)
    commit('deletebook', msgId)
  }
}

const mutations = {
  setbooks (state, books) {
    state.books = books
  },
  addbook (state, book) {
    state.books.push(book)
  },
  deletebook (state, msgId) {
    state.books = state.books.filter(obj => obj.pk !== msgId)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
