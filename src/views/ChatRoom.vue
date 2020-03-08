<template>
  <b-container class="chat">
    <h2 class="text-primary text-center">Real-Time Chat</h2>
    <h5 class="text-secondary text-cen">Powered by Vue JS</h5>
    <div class="card-body">
      <!-- <p class="text-secondary nomessages" v-if="messages.length == 0">
        [No messages yet!]
      </p> -->
      <div class="messages" v-chat-scroll="{ always: false, smooth: true }">
        <div v-for="message in messages" :key="message.id">
          <span class="text-info">[{{ message.name }}]</span>
          <span>{{ message.message }}</span>
          <span class="text-secondary time">{{ message.timestamp }}</span>
        </div>
      </div>
    </div>
    <div class="create-action">
      <CreateMessage :name="name" />
    </div>
  </b-container>
</template>

<script>
import CreateMessage from "@/components/CreateMessage";
import moment from "moment";

export default {
  name: "ChatRoom",
  props: ["name"],
  components: {
    CreateMessage
  },
  data() {
    return {
      messages: []
    };
  },
//   created() {
      
//   }
};
</script>

<style scoped></style>
