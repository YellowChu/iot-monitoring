<template>
<div>
    <div class="container d-flex justify-content-center">
        <div class="row">
            <div v-for="sensor in data.device_list" :key="sensor.id"
            class="col-auto mb-3"
            style="cursor: pointer"
            @click="change_displayed_device(sensor)"
            >
                <div class="sensor-card card" :class="{ 'selected-card': is_selected(sensor.id) }" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">{{ sensor.device_name || sensor.device_id }}</h5>
                        <p v-if="sensor.device_description" class="card-text">{{ sensor.device_description.slice(0, 30) + "..." }}</p>
                        <p v-else class="card-text"><i>Missing sensor description.</i></p>
                    </div>
                </div>
            </div>

            <div v-if="data.displayed_device">
                <home_sensor_detail :room_sensor="data.displayed_device"></home_sensor_detail>
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

import { onMounted, provide, reactive } from "vue";
import router from "@/router";
import { useRoute } from "vue-router";

import home_sensor_detail from "@/components/home_sensor_components/home_sensor_detail.vue"


const route = useRoute()

let data = reactive({
    device_list: [],
    displayed_device: {},
})

provide("update_room_sensor", get_room_sensor);

onMounted(() => {
    get_room_sensor();
})

function get_room_sensor() {
    axios
        .get("/api/v1/roomsensor/")
        .then((response) => {
            console.log(response);
            data.device_list = response.data;

            if (route.params.device_id) {
                var found_sensor = data.device_list.filter(sensor => {
                    return sensor.id == route.params.device_id
                })
                data.displayed_device = found_sensor[0];
            }
        })
}

function change_displayed_device(device) {
    if (data.displayed_device.id == device.id) {
        data.displayed_device = {};
        router.push({ name: 'home_sensor_list' });
    } else {
        data.displayed_device = device;
        router.push({ name: 'home_sensor_data', params: { device_id: device.id } });
    }
}

function is_selected(device_pk) {
    if (data.displayed_device.id == device_pk) {
        return true
    } else {
        return false
    }
}
</script>