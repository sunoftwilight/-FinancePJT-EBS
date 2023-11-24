import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useFinanceStore = defineStore('finance', () => {
  const API_URL = 'http://127.0.0.1:8000'

  const finances = ref([])

  const getFinances = function () {
    axios({
      method: 'get',
      url: `${API_URL}/products/get_data/`
    })
    .then(res => {
      finances.value = res.data
      // console.log(res.data)
    })
    .catch(err => console.log(err))
  }



  return { API_URL, finances, getFinances }

}, { persist : true })
