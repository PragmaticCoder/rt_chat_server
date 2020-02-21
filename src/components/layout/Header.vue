<template>
  <header class="header">
    <h1>Sask Confessions</h1>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/messages">Message</router-link> |
      <router-link to="/chat">Chat</router-link>
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
