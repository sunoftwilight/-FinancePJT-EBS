<template>
  <div class="container ms-3 mt-3">
    <h1>상품 후기</h1>
    <div class="mt-4 mb-4">
      <RouterLink :to="{ name: 'CreateView' }" class="btn mybtn pt-1"  style="height: 35px;">
        CREATE
      </RouterLink>
    </div>
    <div>
      <ArticleList />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink, useRouter } from 'vue-router'
import ArticleList from '@/components/ArticleView/ArticleList.vue'

const store = useCounterStore()
const router = useRouter()

onMounted(() => {
  store.getArticles()
})

</script>

<style scoped>
.mybtn {
  background-color: rgb(89, 139, 248);
  color: white;
  text-shadow: 1px 1px rgb(146, 176, 241);
}
</style>
