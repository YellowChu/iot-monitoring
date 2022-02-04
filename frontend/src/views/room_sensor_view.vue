<template>
<div class="container d-flex justify-content-center">
    <transition name="slide-up" mode="out-in">
    <div :key="Object.keys(data.displayed_device).length">
        <div v-if="Object.keys(data.displayed_device).length === 0" class="vertical-center">
            <div class="container">
                <div class="row">
                    <div class="col card-group pt-3 pb-3">
                        <div class="d-flex flex-column justify-content-center align-items-center ms-2" style="width: 3rem">
                            <font-awesome-icon v-if="data.start - 3 >= 0" :icon="['fas', 'chevron-left']" size="2x" @click="prev_cards()" style="cursor:pointer"/>
                        </div>
                        <transition :name="data.transition_name" mode="out-in">
                            <div class="d-flex" :key="data.start">
                                <div v-for="sensor in data.device_list.slice(data.start, data.end)" :key="sensor.id"
                                    class="col-auto"
                                    style="cursor: pointer"
                                    @click="change_displayed_device(sensor)"
                                >
                                    <div class="sensor-card card ms-2 me-2" :class="{ 'selected-card': data.displayed_device.id == sensor.id }" style="width: 18rem; height: 15rem;">
                                        <div class="card-body d-flex flex-column justify-content-center align-items-center">
                                            <h5 class="card-title fw-bold">{{ sensor.device_name || sensor.device_id }}</h5>
                                            <p v-if="sensor.device_description" class="card-text mt-4">{{ sensor.device_description }}</p>
                                            <p v-else class="card-text"><i>Missing sensor description.</i></p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </transition>
                        <div class="d-flex flex-column justify-content-center align-items-center me-2" style="width: 3rem">
                            <font-awesome-icon v-if="data.start + 3 < data.device_list.length" :icon="['fas', 'chevron-right']" size="2x" @click="next_cards()" style="cursor:pointer"/>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col d-flex flex-column justify-content-center align-items-center">
                        <div class="add-sensor card text-white" @click="data.show_create_modal=true">
                            <div class="card-body-center">
                                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
                                    <path 
                                        d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"
                                    />
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <teleport to="body">
                <wave_footer
                    :bool_trigger="Object.keys(data.displayed_device).length == 0"
                ></wave_footer>
            </teleport>
        </div>
        <div v-if="Object.keys(data.displayed_device).length != 0">
            <div class="card-group d-flex justify-content-center align-items-center pt-3 pb-3">
                <div class="d-flex flex-column justify-content-center align-items-center ms-2" style="width: 3rem">
                    <font-awesome-icon v-if="data.start - 3 >= 0" :icon="['fas', 'chevron-left']" size="2x" @click="prev_cards()" style="cursor:pointer"/>
                </div>
                <transition :name="data.transition_name" mode="out-in">
                    <div class="d-flex" :key="data.start">
                        <div v-for="sensor in data.device_list.slice(data.start, data.end)" :key="sensor.id"
                            class="col-auto"
                            style="cursor: pointer"
                            @click="change_displayed_device(sensor)"
                        >
                            <div class="sensor-card card ms-2 me-2" :class="{ 'selected-card': data.displayed_device.id == sensor.id }" style="width: 18rem;">
                                <div class="card-body">
                                    <h5 class="card-title">{{ sensor.device_name || sensor.device_id }}</h5>
                                    <p v-if="sensor.device_description" class="card-text">{{ sensor.device_description.slice(0, 30) + "..." }}</p>
                                    <p v-else class="card-text"><i>Missing sensor description.</i></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </transition>
                <div class="d-flex flex-column justify-content-center align-items-center me-2" style="width: 3rem">
                    <font-awesome-icon v-if="data.start + 3 < data.device_list.length" :icon="['fas', 'chevron-right']" size="2x" @click="next_cards()" style="cursor:pointer"/>
                </div>
            </div>

            <room_sensor_detail :room_sensor="data.displayed_device"></room_sensor_detail>
        </div>
    </div>
    </transition>

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
.vertical-center {
    min-height: 100%;
    min-height: 60vh;

    display: flex;
    align-items: center;
}
.sensor-card {
    border-left: 8px solid #9198e5;
}
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
    border-left: none;
    background: linear-gradient(#e66465, #9198e5);
}

.add-sensor {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 3rem;
    width: 3rem;
    background: linear-gradient(#e66465, #9198e5);
}
.add-sensor:hover {
    cursor: pointer;
    transform: scale(1.05);
    box-shadow: 0 10px 20px rgba(0,0,0,.12), 0 4px 8px rgba(0,0,0,.06);
}

.slide-right-enter-active,
.slide-right-leave-active {
    transition: all 0.3s;
}
.slide-right-leave-to {
    opacity: 0;
    transform: translateX(15px);
}
.slide-right-enter-from {
    opacity: 0;
    transform: translateX(-15px);
}

.slide-left-enter-active,
.slide-left-leave-active {
    transition: all 0.3s;
}
.slide-left-leave-to {
    opacity: 0;
    transform: translateX(-15px);
}
.slide-left-enter-from {
    opacity: 0;
    transform: translateX(+15px);
}

.slide-up-enter-active,
.slide-up-leave-active {
    transition: all 0.3s;
}
.slide-up-leave-to {
    opacity: 0;
    transform: translateY(-30px);
}
.slide-up-enter-from {
    opacity: 0;
    transform: translateY(-30px);
}
</style>

<script setup>
import axios from "axios";

import { onMounted, provide, reactive, watch } from "vue";
import router from "@/router";
import { useRoute } from "vue-router";

import room_sensor_detail from "@/components/room_sensor/room_sensor_detail.vue";
import modal_window from "@/components/ui/modal_window.vue";
import wave_footer from "@/components/ui/wave_footer.vue";


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
    // slider data
    start: 0,
    end: 3,
    transition_name: "slide-left",
    cards: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
})

const route = useRoute()

provide("update_room_sensor", get_room_sensor);


watch(() => [data.device_id, data.device_name, data.device_name], () => {
    data.enable_create = true;
})

watch(() => route.params.device_id, () => {
    if (!route.params.device_id) {
        data.displayed_device = {};
    }
})

onMounted(() => {
    get_room_sensor();
})

function get_room_sensor() {
    axios
        .get("/api/v1/roomsensor/")
        .then((resp) => {
            data.device_list = resp.data;

            if (route.params.device_id && route.params.device_id != "undefined") {
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
        router.push({ name: 'room_sensor_dashboard', params: { device_id: device.id } });
    }
}

function next_cards() {
    data.transition_name = "slide-left";
    data.start += 3;
    data.end += 3;
}

function prev_cards() {
    data.transition_name = "slide-right";
    data.start -= 3;
    data.end -= 3;
}
</script>