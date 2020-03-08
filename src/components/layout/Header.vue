<template>
  <header class="header">
    <h1>Sask Confessions Chat</h1>
    <div id="nav">
      <router-link to="/chatroom">Chat Room</router-link> |
      <router-link to="/todo">To Do App</router-link> |
      <router-link to="/messages">Message</router-link>
    </div>
  </header>
</template>

<script>
export default {
  name: "Header"
};
</script>

<style scoped>
.header {
  background: #333;
  color: #fff;
  text-align: center;
  padding: 10px;
  text-decoration: none;
}

.header a {
  color: #fff;
  padding-right: 5px;
}
</style>
