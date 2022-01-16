<template>
<div class="home_sensor_list">
    <h2>List of Sensors</h2>

    <div>
        <ul>
            <li v-for="sensor in sensors_list.sensors" :key="sensor.pk" @click="change_displayed_device(sensor.pk)">{{ sensor.device_id }}</li>
        </ul>
    </div>
    <div v-if="displayed_device_id">
        <router-link :to="{ name: 'home_sensor_detail', params: { device_id: displayed_device_id } }">| Data |</router-link>
        <router-link :to="{ name: 'home_sensor_command', params: { device_id: displayed_device_id } }">| Issue command |</router-link>
    </div>
    <div>
        <router-view></router-view>
    </div>
</div>
</template>

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
</script>