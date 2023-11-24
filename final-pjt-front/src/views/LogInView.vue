<template>
  <MainCarousel />

  <div class="d-flex justify-content-center">
    <!-- 로그인 폼 -->
    <div class="container mt-5 me-1" id="container" style="width: 37rem;">
      <h1 id="loginBoxTitle" class="d-inline-block">WELCOME BACK,<br> Please LogIn !</h1>
      <br>
  
      <div id="loginBox">
        <form @submit.prevent="logIn">
    
          <div class="input-form-box">
            <span>ID </span>
            <input type="text" v-model.trim="username" class="form-control" ><br>
          </div>
    
          <div class="input-form-box">
            <span>PW </span>
            <input type="password" v-model.trim="password" class="form-control" ><br>
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
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
  store.currentUser(payload.username)
}

</script>

<style scoped>
img {
  margin-left: 0;
  padding-left: 0;
}

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
  min-width: 65px;
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
