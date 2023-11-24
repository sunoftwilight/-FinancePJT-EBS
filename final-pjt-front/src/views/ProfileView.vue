<template>
  <div class="container ms-3 mt-4">
    <div class="d-flex justify-content-between">
      <h1 id="username" class="fw-bold text-primary" style="width: 15rem;">{{ user.username }}</h1>
      <RouterLink :to="{ name: 'recommend'} " class="btn mybtn" style="height: 40px;"> Fit한 상품 찾기 </RouterLink>
    </div>
    <div class="mt-4">
      <h5 class="ms-2 m-3">닉네임</h5>
      <p class="ms-3">{{ user.nickname }}</p>
      <hr>
      <h5 class="ms-2 m-3">나이</h5>
      <p class="ms-3">{{ user.age }}</p>
      <hr>
      <h5 class="ms-2 m-3">보유 자산</h5>
      <p class="ms-3">{{ user.money }}</p>
      <hr>
      <h5 class="ms-2 m-3">연봉</h5>
      <p class="ms-3">{{ user.salary }}</p>
      <hr>
      <h5 class="ms-2 m-3">가입 상품</h5>
      <p v-if="user.financial_products">{{ user.financial_products }}</p>
      <p v-else class="text-secondary ms-3">가입한 상품이 존재하지 않습니다</p>
      <hr>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import { RouterLink } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const user = store.currentUserDetail

// onMounted(() => {
//   console.log(store.isLogin)
//   if (store.isLogin) {
//     store.currentUser(store.currentUserName)
//     user.value = store.currentUserDetail
//     console.log(user.value)
//   }
// })
</script>

<style scoped>
#username {
  background: linear-gradient(to right, rgb(221, 142, 255), #4e95ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.mybtn {
  background-color: rgb(197, 122, 255);
  color: white;
  text-shadow: 1px 1px rgb(94, 125, 193);
}
</style>