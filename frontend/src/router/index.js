import { createRouter, createWebHistory } from 'vue-router'
import index from '../views/Index.vue'

const routes = [
  {
    path: '/',
    name: 'Index',
    component: index
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import(/* webpackChunkName: "about" */ '../views/Profile.vue')
  },
  {
    path: '/expert',
    name: 'Expert',
    component: () => import(/* webpackChunkName: "about" */ '../views/Expert.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
