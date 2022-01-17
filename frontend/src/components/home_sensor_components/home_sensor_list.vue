<template>
<div>
    <div class="container d-flex justify-content-center">
        <div class="row">
            <div v-for="sensor in sensors_list.sensors" :key="sensor.pk"
            class="col-auto mb-3"
            style="cursor: pointer"
            @click="change_displayed_device(sensor.pk)"
            >
                <div class="sensor-card card" :class="{ 'selected-card': is_selected(sensor.pk) }" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">{{ sensor.device_name || sensor.device_id }}</h5>
                        <p v-if="sensor.device_description" class="card-text">{{ sensor.device_description.slice(0, 30) + "..." }}</p>
                        <p v-else class="card-text"><i>Missing sensor description.</i></p>
                    </div>
                </div>
            </div>
            <div class="row">
                <ul v-if="displayed_device_id" class="nav nav-tabs">
                    <li class="nav-item">
                        <router-link :to="{ name: 'home_sensor_detail', params: { device_id: displayed_device_id } }" class="nav-link" :class="{active: route.name==='home_sensor_detail'}">Data</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'home_sensor_command', params: { device_id: displayed_device_id } }" class="nav-link" :class="{active: route.name==='home_sensor_command'}">Issue command</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'home_sensor_settings', params: { device_id: displayed_device_id } }" class="nav-link" :class="{active: route.name==='home_sensor_settings'}">Settings</router-link>
                    </li>
                </ul>
                <router-view></router-view>
            </div>
        </div>
    </div>
</div>
</template>

<style scoped>
.sensor-card:hover {
    cursor: pointer;
    transform: scale(1.05);
    box-shadow: 0 10px 20px rgba(0,0,0,.12), 0 4px 8px rgba(0,0,0,.06);
}

.nav-container {
    width: 1000px;
}

.selected-card {
    transform: scale(1.05);
    box-shadow: 0 10px 20px rgba(0,0,0,.12), 0 4px 8px rgba(0,0,0,.06);
    color: white;
    background: rgb(57, 57, 57);
}
</style>

<script setup>
import axios from "axios"

import { onMounted, reactive, ref } from "vue";
import router from "@/router";
import { useRoute } from "vue-router";


const route = useRoute()

let sensors_list = reactive({sensors: []})
let displayed_device_id = ref(null);

onMounted(() => {
    console.log(route.params);
    if (route.params.device_id) {
        displayed_device_id.value = route.params.device_id;
    }
    axios
        .get("/api/sensor/room_sensor_list/")
        .then((response) => {
            sensors_list.sensors = response.data.room_sensors;
            console.log(sensors_list);
        })
})

function change_displayed_device(device_pk) {
    if (displayed_device_id.value == device_pk) {
        displayed_device_id.value = null;
        router.push({ name: 'home_sensor_list' });
    } else {
        displayed_device_id.value = device_pk;
        router.push({ name: 'home_sensor_detail', params: { device_id: device_pk } });
    }
}
function is_selected(device_pk) {
    if (displayed_device_id.value == device_pk) {
        return true
    } else {
        return false
    }
}
</script>