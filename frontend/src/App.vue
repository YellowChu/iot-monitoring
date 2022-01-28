<template>
<div class="base">
    <HomeSensorView></HomeSensorView>
</div>
</template>

<style scoped>
@font-face {
    font-family: "main_font";
    src: url("./assets/Viga-Regular.ttf") format("truetype");
}

.base {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-family: Helvetica;
    color: #2c3e50;
}

</style>

<script setup>
// sans-serif


import HomeSensorView from "@/views/home_sensor_views/home_sensor_base_view.vue"
</script>