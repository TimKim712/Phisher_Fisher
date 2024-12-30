<template>
  <div class="phisher_detector flex flex-col items-center space-y-3 mt-20">
    <input
      type="text"
      v-model="userMessage"
      placeholder="Enter suspected message"
      class="p-1 border rounded w-64"
    />
    <button @click="sendReq" class="p-2 bg-teal-950 text-white rounded">
      Check
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userMessage: "",
    };
  },
  methods: {
    sendReq() {
      fetch("http://127.0.0.1:5000/test", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: this.userMessage,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
