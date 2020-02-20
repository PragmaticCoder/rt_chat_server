import Vue from 'vue'
import Router from 'vue-router'
import Messages from '@/components/Messages'
import Home from '@/views/Home.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component:Home
    },
    {
      path: '/messages',
      name: 'messages',
      component: Messages
    }
  ]
})
