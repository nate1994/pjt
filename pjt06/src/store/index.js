import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieList :[]
  },
  mutations: {
    CREATE_LIST(state, movie){
      state.movieList.push(movie)
    }
  },
  actions: {
    createList({commit}, movie){
      commit('CREATE_LIST', movie)
    }
  },
  modules: {
  }
})
