import Vue from 'vue'
import Router from 'vue-router'
import Messages from '@/views/Messages'
import TodoApp from '@/views/TodoApp'
import ChatRoom from '@/views/ChatRoom.vue'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'chatroom',
            component: ChatRoom
        },
        {
            path: '/messages',
            name: 'messages',
            component: Messages
        },
        {
            path: '/todo',
            name: 'todo',
            component: TodoApp
        }
    ]
})
