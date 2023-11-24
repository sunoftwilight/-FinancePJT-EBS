<template>
  <div class="container mt-3 ms-3" v-if="article">
    <h1 class="mb-3">{{ article.title }}</h1>
      <!-- <span>작성자 : {{ user.username }}  </span> -->
    <div class="text-secondary opacity-75">
      <span class="me-3 ms-2">작성 날짜 &nbsp; {{ article.created_at.slice(0, 10) }}</span>
      <span class="me-3 ms-2">수정 날짜 &nbsp; {{ article.updated_at.slice(0, 10) }}</span>
    </div>
    <div class="d-flex">
      <p class="my-3 ms-3 pt-5" style="height: 10rem;">{{ article.content }}</p>
    </div>

    <div class="d-flex">
      <div class="me-2">
        <RouterLink :to="{ name: 'articles' }" class="btn mybtn">목록</RouterLink>
      </div>

      <div v-if="store.isLogin" class="me-2">
        <div v-if="user.id === article.user">
          <RouterLink 
            :to="{ name: 'UpdateView', params: { id: article.id }} "
            class="btn mybtn" 
          >
            수정
          </RouterLink>
        </div>
      </div>
      
      <div v-if="store.isLogin" class="me-2">
        <button @click="deleteArticle" v-if="user.id === article.user"
          class="btn mybtn"
        >삭제</button>
      </div>
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
const article = ref(null)
const user = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/${route.params.id}/`
  })
    .then((res) => {
      console.log(res.data)
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  
  if (store.isLogin) {
    // console.log(store.currentUserName)
    store.currentUser(store.currentUserName)
    user.value = store.currentUserDetail
  }
})

const deleteArticle = function () {
  axios({
    method: 'delete',
    url: `${store.API_URL}/articles/${route.params.id}/`
  })
    .then((res) => {
      router.push({ name: 'articles'})
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style scoped>
/* .mybtn {
  background-color: rgb(89, 139, 248);
  color: white;
  text-shadow: 1px 1px rgb(146, 176, 241);
} */
.mybtn {
  background-color: rgb(66, 121, 239);
  color: white;
  text-shadow: 1px 1px rgb(94, 125, 193);
}
</style>
