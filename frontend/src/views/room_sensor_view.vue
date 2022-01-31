<template>
<div>
    <div class="container d-flex justify-content-center">
        <div class="row">
            <div v-for="sensor in data.device_list" :key="sensor.id"
                class="col-auto mb-3"
                style="cursor: pointer"
                @click="change_displayed_device(sensor)"
            >
                <div class="sensor-card card" :class="{ 'selected-card': data.displayed_device.id == sensor.id }" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">{{ sensor.device_name || sensor.device_id }}</h5>
                        <p v-if="sensor.device_description" class="card-text">{{ sensor.device_description.slice(0, 30) + "..." }}</p>
                        <p v-else class="card-text"><i>Missing sensor description.</i></p>
                    </div>
                </div>
            </div>

            <div 
                class="col-auto mb-3"
                style="cursor: pointer; margin-top: 1rem;"
                @click="data.show_create_modal=true"
            >
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
                <room_sensor_detail :room_sensor="data.displayed_device"></room_sensor_detail>
            </div>
        </div>
    </div>

    <modal_window 
        :show_modal="data.show_create_modal"
        @close="data.show_create_modal=false; data.enable_create=false"
    >
        <template v-slot:header>
            <h4 class="modal-title" id="myModalLabel">Add Room Sensor</h4>
        </template>

        <template v-slot:body>
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
        </template>

        <template v-slot:footer>
            <button type="submit" form="create_room_sensor_form" class="btn btn-success"
                :class="{ disabled: !data.enable_create }"
            >
                Add
            </button>
        </template>
    </modal_window>
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

import { inject, onMounted, provide, reactive, watch } from "vue";
import router from "@/router";
import { useRoute } from "vue-router";

import room_sensor_detail from "@/components/room_sensor/room_sensor_detail.vue"
import modal_window from "@/components/ui/modal_window.vue";


let data = reactive({
    // device list data
    device_list: [],
    displayed_device: {},
    // create sensor form data
    device_id: "",
    device_name: "",
    device_description: "",
    form_err_msg: "",
    show_create_modal: false,
    enable_create: false,
})

const route = useRoute()
const remove_token = inject("remove_token");

provide("update_room_sensor", get_room_sensor);


watch(() => [data.device_id, data.device_name, data.device_name], () => {
    data.enable_create = true;
})


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
        .catch((err) => {
            if (err.response.data && err.response.status == 401) {
                remove_token();
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
            data.show_create_modal = false;
            data.device_id = "";
            data.device_name = "";
            data.device_description = "";
        })
        .catch((err) => {
            if (err.response.data) {
                if (err.response.data.device_id) {
                    data.form_err_msg = err.response.data.device_id[0].replace("This field", "device id");
                } else {
                    data.form_err_msg = err.response.data;
                }
            } else {
                alert(err);
            }
        })
}

function change_displayed_device(device) {
    if (data.displayed_device.id == device.id) {
        data.displayed_device = {};
        router.push({ name: 'room_sensor_view' });
    } else {
        data.displayed_device = device;
        router.push({ name: 'room_sensor_data', params: { device_id: device.id } });
    }
    console.log(data.displayed_device);
}
</script>