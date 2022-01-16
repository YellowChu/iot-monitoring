<template>
<div class="home_sensor_detail">
    <h3>Data</h3>

    <ul>
        <li v-for="data in sensor_data.data_list" :key="data.time">{{ data }}</li>
    </ul>
</div>
</template>

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
</script>