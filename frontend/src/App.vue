<template>
<div class="base">
    <HomeSensorView></HomeSensorView>
</div>
</template>

<style>
@font-face {
    font-family: "main_font";
    src: url("./assets/Viga-Regular.ttf") format("truetype");
}

.base {
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Helvetica;
    text-align: center;
    color: #2c3e50;
}

</style>

<script setup>
// sans-serif


import HomeSensorView from "@/views/home_sensor_views/home_sensor_base_view.vue"
</script>