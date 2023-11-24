<template>
  <!-- 캐러셀 -->
  <div id="carouselExampleCaptions" class="carousel slide h-50" data-bs-ride="carousel" data-bs-interval="3000">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
    </div>
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="@/assets/images/home_cs1.jpg" class="d-block w-100" alt="...">
        <div class="sd-txt carousel-caption d-none d-md-block">
          <h4>쉽고 빠르게, 하지만 강력하게</h4>
          <p>Effortlessly swift, yet undeniably impactful.</p>
        </div>
      </div>
      <div class="carousel-item">
        <img src="@/assets/images/home_cs2.jpg" class="d-block w-100" alt="...">
        <div class="sd-txt carousel-caption d-none d-md-block">
          <h4>취향 분석, 더 적합한 상품</h4>
          <p>Preference analysis for a more fitting selection of products.</p>
        </div>
      </div>
      <div class="carousel-item">
        <img src="@/assets/images/home_cs3.jpg" class="d-block w-100" alt="...">
        <div class="sd-txt carousel-caption d-none d-md-block">
          <h4>더 나은 삶을 위한 든든한 서비스</h4>
          <p>Robust services for a better quality of life.</p>
        </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>

</template>

<script setup>

</script>

<style scoped>
.carousel-inner > .carousel-item > img {
    top: 0;
    left: 0;
    /* min-width: 100%; */
    max-height: 400px;
    width: auto;
    object-fit: cover;
}

.sd-txt { 
  text-shadow: 2px 2px 2px rgb(63, 63, 63); 
}
</style>