import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/views/Login'
import Messages from '@/views/Messages'
import TodoApp from '@/views/TodoApp'
import ChatRoom from '@/views/ChatRoom'

Vue.use(Router);

export default new Router({
    routes: [{
            path: '/',
            name: 'login',
            component: Login
        },
        {
            path: '/chatroom',
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