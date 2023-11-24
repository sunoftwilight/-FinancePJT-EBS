<template>
  <div class="container mt-5" style="width: 45rem;">
    <h1>오늘의 환율</h1>
    <br>
    <p class="text-secondary">계속되는 변화, 변화를 확인하는 가장 빠른 방법</p>
    <br>
    <!-- <div class="d-flex"> -->
    <select name="" id="exchangeresult" v-model="country" class="input-form-box text-primary fw-bold">
      <option v-for="exchangeList in exchangeLists" :value=exchangeList.cur_nm>{{ exchangeList.cur_nm }}</option>
    </select>
      <!-- <span class="text-secondary opacity-75"> &nbsp; &nbsp; &nbsp;(국가 / 화폐단위)</span>
    </div> -->
    <br>
    <!-- <div> -->
      <div class="input-form-box" style="height: 4rem;">
        <span class="pt-4" for="others">외국 통화 &nbsp; &nbsp; </span>
        <input id="others" type="number" placeholder="환전할 금액" class="form-control" v-model="won" @input="changeWon(country)"><br>
      </div>

      <div class="input-form-box" style="height: 4rem;">
        <span class="pt-4" for="won">국내 통화 &nbsp; &nbsp; </span>
        <input id="won" type="number" placeholder="환전 결과" class="form-control" v-model="result" @input="changeResult(country)">
      </div>
      <br>
      <p class="text-primary opacity-75">※ 1 단위 기준&nbsp;&nbsp;(단, '일본 엔화' 및 '인도네시아 루피아'는 100 단위)</p>
    <!-- </div> -->
  </div>
</template>

<script setup>
import { onMounted, computed, ref } from 'vue'
import { useCounterStore } from '@/stores/counter.js'

const store = useCounterStore()

onMounted(() => {
  store.getChange()
})

const exchangeLists = computed(() => {
  return store.saveExchange.filter((item) => {
    return item.cur_nm !== '한국 원'
  })
})

const country = ref('아랍에미리트 디르함')
const won = ref() 
const result = ref() 

const changeWon = function (country) {
  const temp = store.saveExchange.find((item) => {
    return item.cur_nm === country
  })
  const ttb = Number(temp.ttb.replace(',', ''))
  if (country === '일본 옌' || country === '인도네시아 루피아') {
    result.value = won.value * ttb / 100
  } else {
    result.value = won.value * ttb
  }
}

const changeResult = function (country) {
  const temp = store.saveExchange.find((item) => {
    return item.cur_nm === country
  })
  const tts = Number(temp.tts.replace(',', ''))
  if (country === "일본 옌" || country === '인도네시아 루피아') {
    won.value = result.value / tts * 100
  } else {
    won.value = result.value / tts
  }
}

// 한국 원 1,000원 단위로 콤마 추가하는 computed 
// 사용하려면 <input id="won" type="text" placeholder="환전결과" v-model="formattedResult"로 바꾸기>
// const formattedResult = computed(() => {
//   // Use a computed property to format the result with commas
//   return result.value?.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',') || '';
// });

</script>

<style scoped>
</style>