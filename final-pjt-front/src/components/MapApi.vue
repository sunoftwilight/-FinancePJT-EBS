
<template>
  <div class="container ms-5 me-2 mt-3">
    <h2>주변 은행</h2>
    <br>
    <p class="text-secondary">앉은 그 자리에서. 모든 은행, 모든 지점을 한 눈에</p>

    <div class="d-flex">

      <div class="me-5 d-flex flex-column">
        <!-- 시/도 -->
        <div class="inputbox my-3">
          <label for="mainList" class="mb-1 text-primary">시/도</label><br>
          <select class="input-form-box"
            @change="selectedProvince"
            id="mainList"
            v-model="selectPro" style="width: 17rem;"
          >
            <option v-for="province in store.mainList" :key="province">
              {{ province }}
            </option>
          </select>
        </div>

        <!-- 시/군/구 -->
        <div class="inputbox mb-3">
          <label for="subList" class="mb-1 text-primary">시/군/구</label><br>
          <select class="input-form-box" @change="selectedCity" id="subList" v-model="selectCity" style="width: 17rem;">
            <option v-for="city in store.subList[selectPro]" :key="city">
              {{ city }}
            </option>
          </select>
        </div>

        <!-- 은행 -->
        <div class="inputbox mb-3">
          <label for="bankList" class="mb-1 text-primary">은행</label><br>

          <select class="input-form-box" @change="selectedBank" id="bankList" v-model="selectB" style="width: 17rem;">
            <option v-for="bank in store.bankList" :key="bank">
              {{ bank }}
            </option>
          </select>
        </div>

        <!-- 검색 -->
        <button class="btn mybtn my-3 align-self-end" @click="searchNow">검색</button>

        <!-- 검색 결과 -->
        <div class="mt-4 mb-3" style="width: 17rem;">
          <div v-if="bankMarkers.length > 0">
            <h6 class="fw-bold text-primary mb-3">
              {{ searchResultText }}
            </h6>
            <div class="list-group">
              <div
                class="list-group-item item"
                v-for="bankMarker in bankMarkers"
                :key="bankMarker.place_name"
              >
                {{ bankMarker.place_name }}
              </div>
            </div>
          </div>
          
          <!-- <div v-else class="my-3 fw-bold text-primary">
            <h6>옵션을 선택해주세요.</h6>
          </div> -->
        </div>
      </div>

      <!-- 지도 -->
      <div class="mt-4">
        <div class="map" id="map" style="width: 60rem; height: 500px"></div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useLocationStore } from "@/stores/Map.js";

const store = useLocationStore();

// 시도 / 시군구 / 은행 저장하는 변수
const selectPro = ref("");
const selectCity = ref("");
const selectB = ref("");

// 지도 저장
const map = ref(null);

// 은행 마커 저장
const bankMarkers = ref([]);

// 현재 열려있는 인포윈도우
let currentInfowindow = null;

// 드롭다운 선택
const selectedProvince = (event) => {
  selectPro.value = event.target.value;
};
const selectedCity = (event) => {
  selectCity.value = event.target.value;
};
const selectedBank = (event) => {
  selectB.value = event.target.value;
};

// 지도가 넘 느려서 비동기로 처리...( 흠 어려움 )
const loadMap = async () => {
  if (!window.kakao || !window.kakao.maps) {
    console.error("Kakao Maps API is not loaded.");
    return;
  }

  // 초기값은 우선... 싸피 구미캠 근처로...
  const mapContainer = document.getElementById("map");
  const mapOption = {
    center: new kakao.maps.LatLng(36.107071, 128.419289),
    level: 5,
  };

  // 지도 객체 생성
  map.value = new kakao.maps.Map(mapContainer, mapOption);
};

// PlaceAPI 은행 검색...
const placesSearchCB = async (data, status, pagination) => {
  if (status === kakao.maps.services.Status.OK) {
    // 이전 은행 목록과 마커 초기화
    clearMarkers();

    // LetLngBounds 이게 검색 결과의 경계 설정하는거...
    const bounds = new kakao.maps.LatLngBounds();

    for (let i = 0; i < data.length; i++) {
      // 마커 지도에 찍고 경계 만들긩
      displayMarker(data[i]);
      bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
    }

    // 모든 마커 포함하는 지도 짜잔!!!
    map.value.setBounds(bounds);

    // 전체 마커 분포?에 맞춰서 줌 얼추 맞추기... ( 실행되는건지 모르겠음 )
    map.value.setLevel(map.value.getLevel() - 1);

    // 은행 목록 업데이트
    updateBankList(data);
  } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
    console.warn("검색 결과가 없어요 !!");
    // 검색 결과 없는 경우 메세지 표시하기
  } else {
    console.error(`검색 실패 : ${status}`);
  }
};

// 은행 목록 업데이트 함수
function updateBankList(data) {
  // 새로운 은행 목록 추가하기
  for (const marker of data) {
    bankMarkers.value.push({
      marker: null,
      place_name: marker.place_name,
    });

    // 콘솔 확인용 (나중에 지우기)
    console.log("은행: ", marker.place_name);
  }
}

const searchResultText = ref("");

// 검색 버튼 클릭
const searchNow = () => {
  const ps = new kakao.maps.services.Places(map.value);
  // 검색 키워드 저장
  const keyword = `${selectPro.value} ${selectCity.value} ${selectB.value}`;

  if (
    selectPro.value !== "" &&
    selectCity.value !== "" &&
    selectB.value !== ""
  ) {
    // 이전 은행 목록과 마커 초기화
    clearMarkers();

    // 검색
    ps.keywordSearch(
      keyword,
      (data, status, pagination) => {
        // 검색 결과가 있는 경우에만 텍스트 업데이트
        if (status === kakao.maps.services.Status.OK) {
          searchResultText.value = "은행 목록";
        } else {
          searchResultText.value = "옵션을 선택해주세요";
        }

        placesSearchCB(data, status, pagination);
      },
      {
        useMapBounds: false,
      }
    );
  } else {
    alert("옵션을 선택해주세요");
  }
};

// 이전 마커 및 검색 결과 초기화 함수
const clearMarkers = () => {
  for (const marker of bankMarkers.value) {
    if (marker.marker) {
      marker.marker.setMap(null);
    }
  }
  bankMarkers.value = [];
};

// 지도에 마커 표시
function displayMarker(place) {
  const marker = new kakao.maps.Marker({
    map: map.value,
    position: new kakao.maps.LatLng(place.y, place.x),
  });

  // 마커 리스트 추가하기
  bankMarkers.value.push({
    marker: marker,
    place_name: place.place_name,
  });

  kakao.maps.event.addListener(marker, "click", function () {
    // 현재 열려있는 인포윈도우 닫기
    if (currentInfowindow) {
      currentInfowindow.close();
    }

    // 새로운 인포윈도우 열기
    const infowindow = new kakao.maps.InfoWindow({
      zIndex: 1,
      content: `<div style="padding:5px;font-size:12px;">${place.place_name}</div>`,
    });

    infowindow.open(map.value, marker);
    currentInfowindow = infowindow;
  });
}

// 컴포넌트가 마운트된 후 지도 로딩
onMounted(loadMap);
</script>

<style scoped>
.input-form-box {
  border: 1px solid rgb(133, 133, 133);
  border-radius: 10px 10px 10px 10px;
  display: flex;
  margin-bottom: 5px;
}

.mybtn {
  background-color: rgb(97, 147, 255);
  color: white;
  text-shadow: 1px 1px rgb(146, 176, 241);
}
</style>
