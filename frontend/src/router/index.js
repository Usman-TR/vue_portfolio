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
    component: () => import('../views/About.vue')
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/Profile.vue')
  },
  {
    path: '/expert',
    name: 'Expert',
    component: () => import('../views/Expert.vue')
  },
  {
    path: '/registration',
    name: 'Registration',
    component: () => import('../views/Registration.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/static',
    name: 'Static',
    component: () => import('../views/Static.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
