<template>
  <div class="d-flex justify-content-between ms-3">
    <div class="d-flex">
      <h5 class="me-3 fw-bold">{{ article.id }}</h5>
      <p class="me-3">|</p>
      <p class="fw-bold text-center" style="width: 10rem;">{{ article.title }}</p>
      <p class="mx-3">{{ article.content }}</p>
    </div>
    <div>
      <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}" class="btn mybtn pt-1" style="height: 2rem;">
        Detail
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>

<style scoped>
.mybtn {
  background-color: rgb(66, 121, 239);
  color: white;
  text-shadow: 1px 1px rgb(94, 125, 193);
}
</style>