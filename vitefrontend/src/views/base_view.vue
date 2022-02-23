<template>
<div class="room_sensor_view">
    <main_navbar></main_navbar>

    <div class="router_view_container" style="margin-top: 9rem;">
        <router-view></router-view>
    </div>
</div>
</template>


<script setup>
import main_navbar from "@/components/ui/main_navbar.vue";
</script>
