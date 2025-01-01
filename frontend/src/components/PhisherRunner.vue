<template>
  <div
    class="phisher_detector flex flex-col items-center space-x-3 space-y-3 mt-20"
  >
    <input
      type="text"
      v-model="userMessage"
      placeholder="Enter suspected message"
      class="p-1 border rounded w-64"
    />
    <button @click="fetchResponse" class="p-2 bg-teal-950 text-white rounded">
      Check
    </button>

    <div class="response_display" v-if="showResults === true">
      <p class="modelResponse font-mono font-semibold">
        Model Response:
        <span
          :class="
            modelResponse === 'Phishing' ? 'text-red-700' : 'text-green-700'
          "
        >
          {{ modelResponse }}
        </span>
      </p>
      <p class = "modelConfidence font-mono font-semibold">Model Confidence: {{ modelConfidence }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showResults: false,
      userMessage: "",
      modelResponse: "",
      modelConfidence: "",
    };
  },
  methods: {
    async fetchResponse() {
      try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
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
            this.showResults = true;
            this.modelResponse = data.result;
            this.modelConfidence = data.confidence;
            console.log(data);
          });
      } catch (err) {
        console.error(err);
      }
    },
  },
};
</script>
