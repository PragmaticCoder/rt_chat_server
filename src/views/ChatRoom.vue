<template>
  <div class="card mt-3">
    <div class="card-body">
      <div class="card-title">
        <h3>Chat Group</h3>
        <hr />
      </div>
      <div class="card-body">
        <div class="messages"></div>
      </div>
    </div>
    <div class="card-footer">
      <form @submit.prevent="sendMessage">
        <div class="form-group pb-3">
          <label for="message">Message:</label>
          <input type="text" v-model="message" class="form-control" />
        </div>
        <button type="submit" class="btn btn-success">Send</button>
      </form>
    </div>
  </div>
</template>

<script>
import CreateMessage from "@/components/CreateMessage";
// import moment from "moment";

export default {
  name: "ChatRoom",
  props: ["name"],
  components: {
    CreateMessage
  },
  data() {
    return {
      user: "",
      message: "",
      messages: [],
      socket: {}
    };
  },
  mounted() {
    const loc = window.location;
    const webSocketPath = "ws://" + loc.host + "/chat/";
    this.socket = new WebSocket(webSocketPath);

    this.socket.onmessage = e => {
      console.log("data:", e.data);
      var msgData = JSON.parse(e.data);
      console.log(msgData);
    };

    this.socket.onopen = e => {
      console.log("open:", e);

      this.message = "";

      var jsonData = JSON.stringify({
        msg: this.message,
        username: "alvi"
      });

      this.socket.send(jsonData);
    };

    this.socket.onerror = function(e) {
      console.log("error:", e);
    };

    this.socket.onclose = function(e) {
      console.log("closed:", e);
    };

    if (this.socket.readyState === WebSocket.OPEN) {
      console.log("socket.readyState == WebSocket.OPEN");
    } else if (this.socket.readyState === WebSocket.CONNECTING) {
      console.log("Connecting");
    }
  },
  methods: {
    sendMessage(e) {
      e.preventDefault();
      var jsonData = JSON.stringify({
        msg: this.message,
        username: "alvi"
      });

      this.socket.send(jsonData);
      this.messages.push(this.message);

      e.target.reset();
    }
  }
};
</script>
