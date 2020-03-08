<template>
  <div>
    <b-nav tabs align="center" danger>
      <b-navbar toggleable="lg" type="dark" variant="warning">
        <b-nav-item to="/chatroom">Chat Room</b-nav-item>
        <b-nav-item to="/todo">To Do App</b-nav-item>
        <b-nav-item to="/messages">Message</b-nav-item>
      </b-navbar>
    </b-nav>
  </div>
</template>

<script>
export default {
  name: "Header"
};
</script>
