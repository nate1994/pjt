import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'
import MyMovieList from '../views/MyMovieList'
import Random from '../views/Random'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/random',
    name: 'Random',
    component: Random
  },
  {
    path: '/mymovieList',
    name: 'MyMovieList',
    component: MyMovieList
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
