<template>
<div id = "app">
<MainView/>
</div>
</template>

<script>
import MainView from "./views/MainView.vue";
export default {
  name: "App",
  components: {
    MainView,
  },
};
</script>


<!--Convert this to Tailwind later-->
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-width: 25vh;
}
</style>
