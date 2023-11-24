<template>
  <div>
    <!-- <h3></h3> -->
    <!-- <hr> -->
    <div class="d-flex">
      <h5 class="mx-3 fw-bold">#</h5>
      <p class="me-3">|</p>
      <p class="text-center fw-bold" style="width: 10rem;">제목</p>
      <p class="mx-3 text-center">내용</p>
    </div>
    <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/ArticleView/ArticleListItem.vue'

const store = useCounterStore()
</script>
