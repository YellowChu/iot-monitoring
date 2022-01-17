<template>
<div class="row home-sensor-detail">
    <table class="table">
        <thead>
            <tr>
                <th scope="col"></th>
                <th scope="col">Time</th>
                <th scope="col">Temperature [°C]</th>
                <th scope="col">Pressure [kPa]</th>
                <th scope="col">Battery [V]</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(data, idx) in sensor_data.data_list" :key="data.time + idx">
                <th scope="row">{{ idx }}</th>
                <td>{{ parse_date(data.time) }}</td>
                <td>{{ parse_temp(data.temperature) }}</td>
                <td>{{ parse_pres(data.pressure) }}</td>
                <td>{{ parse_batt(data.battery) }}</td>
            </tr>
        </tbody>
    </table>
</div>
</template>

<style scoped>
.home-sensor-detail {
    margin-top: 1rem;
}
</style>

<script setup>
import axios from "axios"

import { onMounted, reactive, watch } from "vue";
import { useRoute } from "vue-router";


const route = useRoute()
let sensor_data = reactive({data_list: []});

onMounted(() => {
    get_device_data(route.params.device_id);
})
watch(
    () => route.params.device_id,
    async new_device_id => {
        await get_device_data(new_device_id);
    }
)

async function get_device_data(device_id) {
    axios
        .get("/api/sensor/room_sensor_data/" + device_id + "/")
        .then((response) => {
            sensor_data.data_list = response.data.sensor_data_list;
        })
}

function parse_date(date_str) {
    let date = new Date(Date.parse(date_str));
    return date.toUTCString()
}
function parse_temp(temp) {
    return temp.toFixed(2)
}
function parse_pres(pres) {
    return (pres / 1000).toFixed(2)
}
function parse_batt(batt) {
    return batt.toFixed(2)
}
</script>