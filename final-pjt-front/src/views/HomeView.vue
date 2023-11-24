<template>
  <!-- 캐러셀 -->
  <MainCarousel />
  <div>

    <!-- 바로가기 카드 -->
    <div class="d-flex justify-content-center" style="height: 26em;">
      <!-- 바로가기1. 예금 상품비교 -->
      <div @click="goDeposit" class="d-flex card border-0 shadow m-3" style="width: 18rem;">

        <img src="@/assets/images/home_cd_deposit.png" style="width: 70%; height: 12rem;" class="mx-auto card-img-top mt-1" alt="예금상품">
        <div class="card-body mt-3 mx-2">
          <h5 class="card-title">예금 상품</h5>
          <p class="card-text text-secondary" style="height: 5rem;">
            가장 확실한 선택.<br>다양한 선택 폭, 마음에 드는 상품 찾기
          </p>

          <!-- <div class="btn-position">
            <RouterLink :to="{ name: 'depositCompare'}" class="btn mybtn">바로가기</RouterLink>
          </div> -->

        </div>
      </div>

      <!-- 바로가기2. 적금 상품비교 -->
      <div @click="goSaving" class="card border-0 shadow m-3" style="width: 18rem;">
        <img src="@/assets/images/home_cd_saving.png" style="width: 70%; height: 12rem;" class="mx-auto card-img-top mt-2" alt="적금상품">
        <div class="card-body mt-3 mx-2">
          <h5 class="card-title">적금 상품</h5>
          <p class="card-text text-secondary" style="height: 5rem;">
            더욱 실속 있는 선택.<br>효율적으로, 그리고 간편하게 상품 찾기
          </p>

          <!-- <div class="btn-position">
            <RouterLink :to="{ name: 'savingCompare'}" class="btn mybtn">바로가기</RouterLink>
          </div> -->

        </div>
      </div>

      <!-- 바로가기3. 환율 계산기 -->
      <div @click="goExchange" class="card border-0 shadow m-3" style="width: 18rem;">
        <img src="@/assets/images/home_cd_exchange.png" style="width: 70%; height: 12rem;" class="pt-2 mx-auto card-img-top mt-2" alt="환율">
        <div class="card-body mt-3 mx-2">
          <h5 class="card-title">오늘의 환율</h5>
          <p class="card-text text-secondary" style="height: 5rem;">
            계속되는 변화.<br> 변화를 확인하는 가장 빠른 방법
          </p>
          <!-- <div class="btn-position">
            <RouterLink :to="{ name: 'exchange'}" class="btn mybtn">바로가기</RouterLink>
          </div> -->

        </div>
      </div>

      <!-- 바로가기4. 주변 은행 검색하기 -->
      <div @click="goABank" class="card border-0 shadow m-3" style="width: 18rem;">
        <img src="@/assets/images/home_cd_bank.png" style="width: 70%; height: 12rem;" class="mx-auto card-img-top mt-2" alt="주변 은행">
        <div class="card-body mt-3 mx-2">
          <h5 class="card-title">내 주변 은행</h5>
          <p class="card-text text-secondary" style="height: 5rem;">
            앉은 그 자리에서.<br>모든 은행, 모든 지점을 한 눈에
          </p>

          <!-- <div class="btn-position">
            <RouterLink :to="{ name: 'aroundbank'}" class="btn mybtn">바로가기</RouterLink>
          </div> -->

        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import MainCarousel from '@/components/MainCarousel.vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const goDeposit = function () {
  router.push({name: 'depositCompare'})
}

const goSaving = function () {
  router.push({name: 'savingCompare'})
}

const goExchange = function () {
  router.push({name: 'exchange'})
}

const goABank = function () {
  router.push({name: 'aroundbank'})
}
</script>

<style scoped>
.carousel-inner > .carousel-item > img {
    top: 0;
    left: 0;
    /* min-width: 100%; */
    max-height: 400px;
    width: auto;
    object-fit: cover;
}

.sd-txt { 
  text-shadow: 2px 2px 2px rgb(63, 63, 63); 
}

.mybtn {
  background-color: rgb(97, 147, 255);
  color: white;
  text-shadow: 1px 1px rgb(146, 176, 241);
}

.btn-position {
  text-align: right;
}
</style>