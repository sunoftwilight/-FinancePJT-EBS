import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'

  const token = ref(null)
  const articles = ref([])
  const currentUserName = ref(null)
  const currentUserPk = ref(null)
  
// -----------------------------------------

  const saveExchange = ref([])

  function getChange() {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/currency/getexchange/'
    })
      .then((res) => {
        // console.log(res.data)
        saveExchange.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  // const sample = {
  //   name:'편수지',
  // }

// ---------------------------------------------
  // token값에 따라 isLogin 변경
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2, nickname, email, age, money, salary, interest } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, nickname, email, age, money, salary, interest
      }
    })
      .then((res) => {
        // console.log(res.data)   // res.data의 key에 token값 저장되어 있음
        // const password = password1
        // logIn({username, password})
        // console.log(res)
        router.push({name:'LogInView'})
        // return {name: 'LogInView'}
      })
      .catch((err) => {
        if (password1 !== password2) {
          window.alert('비밀번호가 서로 일치하지 않습니다.')
        }
        console.log(err)
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password,
      }
    })
      .then((res) => {
        // console.log(res)
        token.value = res.data.key
        currentUserName.value = username
        // currentUser(currentUserName.value)
        router.push({ name: 'home'})
      })
      .catch((err) => {
        window.alert('로그인 정보가 잘못되었습니다.')
        console.log(err)
      })
  }

  const currentUserDetail = ref(null)
  const currentUser = function (username) {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/users/${username}/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        // console.log(res)
        currentUserDetail.value = res.data.data
        currentUserPk.value = res.data.id
      })
      .catch((err) => {
        console.log(err)
      })
  }
    

  const logOut = function() {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then(res => {
        token.value = null
        currentUserPk.value = null
        currentUserDetail.value = null
        router.push({ name: 'home' })
      })
  }

//---------------------------------------------------------------
const recomProducts = ref(null)
const getRecoms = function () {
  axios({
    method: 'get',
    url: `${API_URL}/products/recommend/products/`,
    headers: {
      Authorization: `Token ${token.value}`
    },
  })
  .then(res => {
    console.log(res.data)
    recomProducts.value = res.data
    // return res.data
  })
  .catch(err => console.log(err))
}

const interProducts = ref(null)
const getInter = function (keyword) {
  axios({
    method: 'get',
    url: `${API_URL}/products/recommend/keyword/${keyword}`,
    headers: {
      Authorization: `Token ${token.value}`
    },
  })
  .then(res => {
    console.log(res.data)
    interProducts.value = res.data
  })
  .catch(err => console.log(err))
  
}
//---------------------------------------------------------------

  return {  saveExchange, getChange
  , articles, API_URL, getArticles, signUp, logIn, token, isLogin, logOut
  , currentUserName, currentUser, currentUserPk, currentUserDetail, 
  getRecoms, getInter }
}, { persist : true })

// dpPrdt, getDpPrdt, dpOptn, getDpOptn, svPrdt, getSvPrdt, svOptn, getSvOptn,
// currentUser, currentUserPk, currentUserDetail