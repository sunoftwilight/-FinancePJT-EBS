<template>
  <div class="container mt-3 ms-3" v-if="recomProducts">
    <h1 class="mb-4">Fit한 상품</h1>
    <!-- {{ recomProducts }} -->
    <div v-if="recomProducts.forRich.length" class="d-flex card border-0 shadow mt-2" style="width: 30rem;">
      <div v-for="prdt in recomProducts.forRich" class="p-3">
        <div v-if="prdt !=='자린고비가 될 시간이에요'">
          <h4 class="my-2 text-primary">{{ prdt.recommend.fin_prdt_nm }}</h4>
          <h5 class="mt-4 ms-1">은행 명</h5>
          <p class="ms-2 pt-2">{{ prdt.recommend.kor_co_nm }}</p>
          <hr>
          <h5 class="ms-1">가입 대상</h5>
          <p class="ms-2 pt-2">{{ prdt.recommend.join_member }}</p>
          <hr>
          <h5 class="ms-1">금리 옵션</h5>
          <div v-for="optn in prdt.recommend.depositoptions_set">
            <p class="ms-2 pt-2">{{ optn.intr_rate_type_nm }} &nbsp; &nbsp; {{ optn.save_trm }}개월 &nbsp; &nbsp; {{ optn.intr_rate }} %</p>
          </div>
        </div>
        <div v-else class="text-center">적합한 상품이 없습니다</div>
      </div>
    </div>
    <div v-else-if="recomProducts.forPoor.length">
      <div v-for="prdt in recomProducts.forPoor">
        <div v-if="prdt !=='형편에 맞는 상품이 없어요...'">
          <div v-for="recomoptn in prdt.recommend" class="d-flex card border-0 shadow mt-2 p-3" style="width: 30rem;">

            <h4 class="my-2 text-primary">{{ recomoptn[0].fin_prdt_nm }}</h4>
            <h5 class="mt-4 ms-1">은행 명</h5>
            <p class="ms-2 pt-2">{{  recomoptn[0].kor_co_nm }}</p>
            <hr>
            <h5 class="ms-1">가입 대상</h5>
            <p class="ms-2 pt-2">{{ recomoptn[0].join_member }}</p>
            <hr>
            <h5 class="ms-1 pb-2">금리 옵션</h5>
            <div v-for="optn in recomoptn[0].savingoptions_set">
              <p class="ms-2 pt-2">{{ optn.intr_rate_type_nm }} &nbsp; &nbsp; {{ optn.save_trm }}개월 &nbsp; &nbsp; {{ optn.intr_rate }} %</p>
            </div>
          </div>
        </div>
        <div v-else class="text-center">적합한 상품이 없습니다</div>
      </div>
    </div>
    <div v-else>
      <p>적합한 상품이 없습니다</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from  'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const store = useCounterStore()
const recomProducts = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/products/recommend/products/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
  })
  .then(res => {
    recomProducts.value = res.data
    console.log(recomProducts.value)
  })
  .catch(err => console.log(err))
})
</script>

<style scoped>

</style>