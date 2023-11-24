<template>
  <div class="container mt-3 ms-3">
    <h1 class="mb-4">상품 후기 수정</h1>
    <form @submit.prevent="updateArticle">
      <div class="mb-4">
        <input type="submit" class="btn mybtn">
      </div>
      <div class="input-form-box">
        <span class="ms-1">제목</span>
        <input type="text" v-model.trim="title" class="form-control" style="width: 30rem;"><br>
      </div>
      <div class="input-form-box">
        <span class="ms-1">내용</span>
        <textarea type="text" v-model.trim="content" class="form-control" style="width: 30rem; height: 20rem;"></textarea><br>
      </div>
    </form>
  </div>


  <!-- 
      <div class="container mt-3 ms-3">
    <h1 class="mb-4">상품 후기 작성</h1>
    <form @submit.prevent="createArticle">
      <div class="mb-4">
        <input type="submit" class="btn mybtn">
      </div>
      <div class="input-form-box">
        <span class="ms-1">제목</span><br>
        <input type="text" v-model.trim="title" class="form-control" style="width: 30rem;">
      </div>
      <div class="input-form-box">
        <span class="ms-1">내용</span><br>
        <textarea v-model.trim="content" class="form-control" style="width: 30rem; height: 20rem;"></textarea>
      </div>
    </form>
  </div>
  -->
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
const title = ref('')
const content = ref('')

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      title.value = res.data.title
      content.value = res.data.content
    })
    .catch((err) => {
      console.log(err)
    })
})

const updateArticle = function () {
  axios({
    method: 'put',
    url: `${store.API_URL}/articles/${route.params.id}/`,
    data: {
      title: title.value,
      content: content.value,
    },
    // headers: {
    //   Authorization: `Token ${store.token}`
    // }
  })
    .then((res) => {
      // console.log(res.data)
      // article.value = res.data
      router.push({ name: 'DetailView', params: { id: route.params.id } })
    })
    .catch((err) => {
      console.log(err)
    })
  }
</script>

<style scoped>
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

.mybtn {
  background-color: rgb(66, 121, 239);
  color: white;
  text-shadow: 1px 1px rgb(94, 125, 193);
}
</style>