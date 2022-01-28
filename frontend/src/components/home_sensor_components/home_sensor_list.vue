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

            <div class="col-auto mb-3" style="cursor: pointer; margin-top: 1rem;" data-bs-toggle="modal" data-bs-target="#add_sensor">
                <div class="add-sensor card text-white bg-muted">
                    <div class="card-body-center">
                        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
                            <path 
                                d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"
                            />
                        </svg>
                    </div>
                </div>
            </div>

            <div v-if="data.displayed_device">
                <home_sensor_detail :room_sensor="data.displayed_device"></home_sensor_detail>
            </div>
        </div>
    </div>

    <div class="modal fade" id="add_sensor" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title" id="myModalLabel">Add Room Sensor</h4>
                </div>
                <div class="modal-body">
                    <form id="create_room_sensor_form" class="sensor-form" @submit.prevent="create_room_sensor()">
                        <div v-if="data.form_err_msg" class="alert alert-danger" role="alert">
                            {{ data.form_err_msg }}
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Device ID*</label>
                            <input type="text" class="form-control" v-model="data.device_id">
                            <small class="text-muted">Must correspond with device id registered to The Things Network</small>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Device Name</label>
                            <input type="text" class="form-control" v-model="data.device_name">
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Description</label>
                            <textarea class="form-control" rows="3" v-model="data.device_description"></textarea>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="submit" form="create_room_sensor_form" class="btn btn-success">Add</button>
               </div>
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

.add-sensor {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 3rem;
    width: 3rem;
    background: gray;
}
.add-sensor:hover {
    cursor: pointer;
    transform: scale(1.05);
    box-shadow: 0 10px 20px rgba(0,0,0,.12), 0 4px 8px rgba(0,0,0,.06);
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
    device_id: "",
    device_name: "",
    device_description: "",
    form_err_msg: "",
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

function create_room_sensor() {
    let request_data = {
        device_id: data.device_id,
        device_name: data.device_name,
        device_description: data.device_description,
    };
    axios  
        .post("/api/v1/roomsensor/", request_data)
        .then(() => {
            get_room_sensor();
        })
        .catch((err) => {
            alert(err);
            console.log(err.response);
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