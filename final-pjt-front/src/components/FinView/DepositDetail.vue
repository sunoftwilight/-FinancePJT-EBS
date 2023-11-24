<template>
  <div class="container mx-2 mt-3">
    
    <div class="mx-2 mt-3">
      <div class="d-flex justify-content-between">
        <h2>{{ product.fin_prdt_nm }}</h2>
        <RouterLink :to="{ name: 'depositCompare'}" class="btn mybtn pt-1 me-3" style="height: 35px;">목록</RouterLink>
      </div>
      <hr>

      <h4 class="ms-1">은행 명</h4>
      <p class="my-4 ms-2">{{ product.kor_co_nm }}</p>
      <hr>

      <h4 class="ms-1">가입 방법</h4>
      <p class="my-4 ms-2">{{ product.join_way }}</p>
      <hr>

      <h4 class="ms-1">가입 대상</h4>
      <p class="my-4 ms-2">{{ product.join_member }}</p>
      <hr>

      <h4 class="ms-1">우대 금리 조건</h4>
      <p class="my-4 ms-2">{{ product.spcl_cnd }}</p>
      <hr>

      <h4 class="ms-1">만기 후</h4>
      <p class="my-4 ms-2" style="width: 60rem;">{{ product.mtrt_int }}</p>
      <hr>

      <h4 class="ms-1">유의 사항</h4>
      <p class="my-4 ms-2" style="width: 60rem;">{{ product.etc_note }}</p>
      <hr>

      <h4 class="ms-1">이자율 적용 방법</h4>
      <div class="ms-2">
        <p class="my-4 text-primary fw-bold">{{ product.depositoptions_set[0].intr_rate_type_nm }}</p>
        <div v-for="(option, index) in product.depositoptions_set" :key="index">
          <p><span class="ms-1 text-primary opacity-75">{{ option.save_trm }}개월</span> &nbsp; {{ option.intr_rate }} %</p>
          <p></p>
        </div>
      </div>
      <hr>
      
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { useFinanceStore } from '@/stores/finance.js'

const store = useFinanceStore()
const route = useRoute()
const userId = route.params.id

const product = store.finances.deposits.find((product) => product.id == userId)
</script>

<style scoped>
.mybtn {
  background-color: rgb(89, 139, 248);
  color: white;
  text-shadow: 1px 1px rgb(146, 176, 241);
}
</style>