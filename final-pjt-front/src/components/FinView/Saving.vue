<template>
  <div class="container mx-3 mt-3">
    <h1 class="mb-4">적금 상품</h1>
    <p class="text-secondary mb-4">더욱 실속 있는 선택. 효율적으로, 그리고 간편하게 상품 찾기</p>
    <br>
    <div class="d-flex justify-content-between">
      <select v-model="selectedBanks" class="input-form-box fw-bold">
        <option v-for="bank in allBanks" :key="bank.id" :value="bank.id">{{ bank.kor_co_nm }}</option>
      </select>
      <div>
        <RouterLink :to="{ name: 'depositCompare' } " class="btn mybtn pt-1 me-3" style="height: 35px;">예금 상품</RouterLink>
        <RouterLink :to="{ name: 'savingCompare' } " class="btn mybtn pt-1" style="height: 35px;">적금 상품</RouterLink>
      </div>
    </div>
    <br>
    <table class="list-group">
      <thead>
        <tr class="text-center list-group-item tb-header">
          <th>은행 명</th>
          <th>상품 명</th>
          <th>적립 유형</th>
          <th>저축 금리 6개월</th>
          <th>저축 금리 12개월</th>
          <th>저축 금리 24개월</th>
          <th>저축 금리 36개월</th>
        </tr>
      </thead>
      <p></p>
      <tbody>
        <tr v-for="saving in filteredSavings" :key="saving.fin_co_no" class="list-group-item py-3">
          <td>{{ saving.kor_co_nm }}</td>
          <td>
            <RouterLink id="togo" :to="{ 
              name: 'savingDetail',
              params: {
                'id': saving.id,
                'rsrv_type': getFirstOptionType(saving)
              }, 
            }"
            class="ps-3"
          >{{ saving.fin_prdt_nm }}</RouterLink>
          </td>

          <td class="text-center">{{ getOptionTypeName(saving, getFirstOptionType(saving)) }}</td>
          <td class="text-center">{{ getInterestRate(saving, getFirstOptionType(saving), 6) }}</td>
          <td class="text-center">{{ getInterestRate(saving, getFirstOptionType(saving), 12) }}</td>
          <td class="text-center">{{ getInterestRate(saving, getFirstOptionType(saving), 24) }}</td>
          <td class="text-center">{{ getInterestRate(saving, getFirstOptionType(saving), 36) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { onMounted, computed, ref, watch } from 'vue'
import { useFinanceStore } from '@/stores/finance.js'
import { RouterLink } from 'vue-router'

const store = useFinanceStore()
const ALL_BANKS_OPTION_ID = 'allBanks';
const selectedBanks = ref([ALL_BANKS_OPTION_ID]);

const allBanks = computed(() => {
  if (!store.finances || !store.finances.savings) {
    return [];
  }

  const uniqueBanks = store.finances.savings.reduce((acc, saving) => {
    if (!acc.some(item => item.id === saving.fin_co_no)) {
      acc.push({ id: saving.fin_co_no, kor_co_nm: saving.kor_co_nm });
    }
    return acc;
  }, []);

  return [{ id: ALL_BANKS_OPTION_ID, kor_co_nm: '전체 조회' }, ...uniqueBanks];
});

const filteredSavings = computed(() => {
  if (!store.finances || !store.finances.savings) {
    return [];
  }

  const uniqueSavings = selectedBanks.value.includes(ALL_BANKS_OPTION_ID)
    ? store.finances.savings
    : store.finances.savings.filter(saving => selectedBanks.value.includes(saving.fin_co_no));

  return uniqueSavings;
});

const getOptionTypeName = (saving, type) => {
  const option = saving.savingoptions_set.find(item => item.rsrv_type === type);
  return option ? option.rsrv_type_nm : '-';
};

const getInterestRate = (saving, type, term) => {
  const option = saving.savingoptions_set.find(item => item.save_trm === term && item.rsrv_type === type);
  return option ? (option.intr_rate || '-') : '-';
};

const getFirstOptionType = (saving) => {
  return saving.savingoptions_set.length > 0 ? saving.savingoptions_set[0].rsrv_type : '-';
};

onMounted(() => {
  store.getFinances()
})

watch(selectedBanks, (newSelectedBanks) => {
  console.log('Selected Banks Changed:', newSelectedBanks);
});
</script>

<style scoped>
#togo {
  text-decoration: none;
}

.tb-header {
  background-color: rgb(168, 195, 255);
  border: 1px solid rgb(168, 195, 255);
  padding-top: 15px;
  padding-bottom: 15px;
  color: white;
  text-shadow: 1px 1px rgb(37, 87, 195);
}

.select-container {
  margin-bottom: 10px;
}

.select-bar {
  margin-right: 10px; /* 적절한 간격 조절 */
}

th, td {
  width: 15rem;
}

.input-form-box {
  border: 1px solid #007bff;
  border-radius: 10px 10px 10px 10px;
  display: flex;
  margin-bottom: 5px;
}

.input-form-box > option {
  display: block;
  text-align: left;
  padding-top: 5px;
  min-width: 70px;
  margin-right: 10px;
}

.mybtn {
  background-color: rgb(89, 139, 248);
  color: white;
  text-shadow: 1px 1px rgb(146, 176, 241);
}
</style>