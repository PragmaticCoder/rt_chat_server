import Vue from 'vue'
import App from '@/App.vue'

import store from '@/store'
import router from '@/router'

import VueChatScroll from 'vue-chat-scroll'
import BootstrapVue from 'bootstrap-vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(VueChatScroll)

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')