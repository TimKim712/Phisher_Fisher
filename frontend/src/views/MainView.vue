<template>
  <div class="main">
    <section
      class="relative text-center min-h-40 bg-cover bg-center bg-no-repeat flex items-center justify-center"
      style="
        background-image: url('https://media.giphy.com/media/PTBVMsYIOB0SBP4MVe/giphy.gif');
      "
    >
      <h1 class="relative text-4xl text-center font-extrabold text-white z-10">
        Phisher Fisher
      </h1>
    </section>
    <div class="min-h-screen flex items-start justify-center">
      <Phisher />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Phisher from "../components/Phisher.vue";
export default {
  name: "HomeView",
  components: {
    Phisher,
  },
};
</script>
