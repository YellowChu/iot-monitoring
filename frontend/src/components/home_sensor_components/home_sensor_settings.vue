<template>
<div>
    <div class="home-sensor-command">
        <div class="row">
            <div class="col">
                <form class="sensor-form">
                    <div class="mb-3">
                        <label for="exampleFormControlSelect1">Name</label>
                        <input type="text" class="form-control" v-model="sensor_name">
                    </div>
                    <div class="mb-3">
                        <label for="exampleColorInput" class="form-label">Description</label>
                        <textarea class="form-control" rows="3" v-model="sensor_description"></textarea>
                    </div>
                    <div class="mb-3">
                        <button class="btn btn-primary">Save</button>
                    </div>
                </form>
            </div>
            <div class="col">
                <div class="jumbotron jumbotron-fluid bg-light">
                    <div class="container">
                        <h4 class="display-4">Fluid jumbotron</h4>
                        <p class="lead">This is a modified jumbotron that occupies the entire horizontal space of its parent.</p>
                    </div>
                </div>
            </div>
        </div>  
    </div>
</div>
</template>

<style>
.home-sensor-command {
    margin-top: 1rem;
}
.sensor-form {
  text-align: left;

}
</style>

<script setup>
import axios from "axios"

import { onMounted, ref, watch } from "vue";
import { useRoute } from "vue-router";


const route = useRoute()
let sensor_name = ref("");
let sensor_description = ref("");

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
            console.log("?", response)
            sensor_name.value = response.data.sensor_name;
            sensor_description.value = response.data.sensor_description;
        })
}
</script>