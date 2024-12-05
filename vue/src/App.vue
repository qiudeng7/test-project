<script setup lang="ts">
import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios'

function click() {
  axios({
    method: 'get',
    url: "/api/tianshu/hello/",
  }).then((response) => {
    console.log(response.data);
  });
}

</script>

<template>
  <div>
    <a href="https://vite.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/image.png" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <el-button type="danger" plain2 :onclick="click">Danger</el-button>
  <HelloWorld msg="Vite + Vue" />

</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}

.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
