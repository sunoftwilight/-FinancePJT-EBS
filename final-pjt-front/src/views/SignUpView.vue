<template>
  <MainCarousel />

  <div class="d-flex justify-content-center">
    <!-- 로그인 폼 -->
    <div class="container mt-5 me-1" id="container" style="width: 37rem;">
      <h1 id="loginBoxTitle" class="d-inline-block">WELCOME,<br> Please SingUp and JOIN US!</h1>
      <br>

      <div id="loginBox">
        <form @submit.prevent="signUp">

          <div class="input-form-box">
            <span>ID </span>
            <input type="text" v-model.trim="username" class="form-control" ><br>
          </div>

          <div class="input-form-box">
            <span>PW </span>
            <input type="password" v-model.trim="password1" class="form-control" ><br>
          </div>

          <div class="input-form-box">
            <span>PW 확인 </span>
            <input type="password" v-model.trim="password2" class="form-control" ><br>
          </div>

          <div class="input-form-box">
            <span>닉네임 </span>
            <input type="text" v-model.trim="nickname" class="form-control" ><br>
          </div>

          <div class="input-form-box">
            <span>E-mail </span>
            <input type="email" v-model.trim="email" class="form-control" ><br>
          </div>

          <div class="input-form-box">
            <span>나이 </span>
            <input type="number" v-model.trim="age" class="form-control" ><br>
          </div>

          <div class="input-form-box">
            <span>보유 자산 </span>
            <input type="number" v-model.trim="money" class="form-control" ><br>
          </div>

          <div class="input-form-box">
            <span>연 수익 </span>
            <input type="number" v-model.trim="salary" class="form-control" ><br>
          </div>

          <div class="button-login-box">
            <input type="submit" class="btn btn-primary btn-xs" style="width:100%">
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import MainCarousel from '@/components/MainCarousel.vue'

const store = useCounterStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const email = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    email: email.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
    interest:'여행',
  }
  store.signUp(payload)
  // .then(
  //   store.currentUser(payload.username)
  // )
}
</script>

<style>

#container {
  margin-left: 10%;
  /* display: flex; */
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: 100%;
}

#loginBox {
  width: 500px;
  text-align: center;
  background-color: #ffffff;
}

.input-form-box {
  border: 0px solid #ff0000;
  display: flex;
  margin-bottom: 5px;
}

.input-form-box > span {
  display: block;
  text-align: left;
  padding-top: 5px;
  min-width: 70px;
  margin-right: 10px;
}

.button-login-box {
  margin: 10px 0;
}

#loginBoxTitle {
  color:#000000;
  font-weight: bold;
  font-size: 32px;
  text-transform: uppercase;
  padding: 5px;
  margin-bottom: 20px;
  background: linear-gradient(to right, #270a09, #8ca6ce);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>
