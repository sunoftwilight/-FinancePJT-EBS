import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

import ProfileView from '@/views/ProfileView.vue'
import RecommendView from '@//views/RecommendView.vue'

import ExchangeView from '@/views/ExchangeView.vue'

import AroundBankView from '@/views/AroundBankView.vue'

import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import UpdateView from '@/views/UpdateView.vue'

import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'

// import FinCompareView from '@/views/FinCompareView.vue'
import Deposit from '@/components/FinView/Deposit.vue'
import Saving from '@/components/FinView/Saving.vue'
import DepositDetail from '@/components/FinView/DepositDetail.vue'
import SavingDetail from '@/components/FinView/SavingDetail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
  // ==================================================
    {
      path: '/finCompare/deposit',
      name: 'depositCompare',
      component: Deposit,
    },
    {
      path: '/finCompare/saving',
      name: 'savingCompare',
      component: Saving,
    },
    {
      path: '/finCompare/deposit/:id',
      name: 'depositDetail',
      component: DepositDetail
    },
    {
      path: '/finCompare/saving/:id/:rsrv_type',
      name: 'savingDetail',
      component: SavingDetail
    },
  // ==================================================
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
    },
    {
      path: '/recommend',
      name: 'recommend',
      component: RecommendView,
    },
  // ==================================================
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView,
    },
  // ==================================================
    {
      path: '/around_bank',
      name: 'aroundbank',
      component: AroundBankView,
    },
  // ==================================================
    {
      path: '/articles',
      name: 'articles',
      component: ArticleView,
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/articles_update/:id',
      name: 'UpdateView',
      component: UpdateView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
  // ==================================================
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
  ]
})

import { useCounterStore } from '@/stores/counter'

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name === 'CreateView' && !store.isLogin) {
    window.alert('로그인이 필요합니다')
    return { name: 'LogInView' }
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인했습니다')
    return { name: 'ArticleView' }
  }
})

export default router
