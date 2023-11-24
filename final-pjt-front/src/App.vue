<template>
  <header>
    <ul class="nav justify-content-between">
      <div class="d-flex nav-item ms-1">

        <li class="logo"><RouterLink class="nav-link lg-pd" :to="{ name: 'home' }"><img class="ms-1 me-2 my-logo" src="@/assets/images/logo.png" alt="logo"></RouterLink></li>
        <li class="nav-underline"><RouterLink class="nav-link" :to="{ name: 'depositCompare' }">상품</RouterLink></li>
        <li class="nav-underline"><RouterLink class="nav-link" :to="{ name: 'exchange'}">환율</RouterLink></li>
        <li class="nav-underline"><RouterLink class="nav-link" :to="{ name: 'aroundbank'}">주변 은행</RouterLink></li>
        <li class="nav-underline"><RouterLink class="nav-link" :to="{ name: 'articles'}">상품 후기</RouterLink></li>
      </div>

      <div class="d-flex me-2">

        <li class="nav-underline" v-if="store.isLogin"><RouterLink class="nav-link" :to="{ name: 'profile' }">내 정보</RouterLink></li>
        <li class="nav-underline" v-if="!store.isLogin"><RouterLink class="nav-link" :to="{ name: 'SignUpView' }">회원가입</RouterLink></li>
        <li class="nav-underline" v-if="!store.isLogin"><RouterLink class="nav-link" :to="{ name: 'LogInView' }">로그인</RouterLink></li>
        <li class="nav-underline" v-if="store.isLogin" @click="logOut"><span class="nav-link">로그아웃</span></li>
      </div>
    </ul>
  </header>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const store = useCounterStore()

const logOut = function () {
  store.logOut()
}

// onMounted(() => {
//   store.currentUser(store.currentUserName)
//   user.value = store.currentUserDetail
// })
</script>

<style scoped>
li {
  margin: 10px;
}

.logo {
  margin: 0;
  margin-left: 5px;
  padding: 0;
  margin-top: 8px;
}

.lg-pd {
  padding: 0;
}

.my-logo {
  max-height: 45px;
}
</style>
