<template>
<div class="container d-flex justify-content-center">
    <transition name="slide-up" mode="out-in">
    <div :key="Object.keys(list_data.displayed_device).length">
        <div v-if="Object.keys(list_data.displayed_device).length === 0" class="vertical-center">
            <div class="container">
                <div class="row">
                    <div class="col card-group pt-3 pb-3">
                        <div class="d-flex flex-column justify-content-center align-items-center ms-2" style="width: 3rem">
                            <font-awesome-icon v-if="slider_data.start - slider_data.step >= 0" :icon="['fas', 'chevron-left']" size="2x" @click="prev_cards()" style="cursor:pointer"/>
                        </div>

                        <transition :name="slider_data.transition_name" mode="out-in">
                            <div class="d-flex" :key="slider_data.start">
                                <div v-for="sensor in list_data.device_list.slice(slider_data.start, slider_data.end)" :key="sensor.id"
                                    class="col-auto"
                                    style="cursor: pointer"
                                    @click="change_displayed_device(sensor)"
                                >
                                    <div class="sensor-card card ms-2 me-2" :class="{ 'selected-card': list_data.displayed_device.id == sensor.id }" style="width: 18rem; height: 15rem;">
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
                            <font-awesome-icon v-if="slider_data.start + slider_data.step < list_data.device_list.length" :icon="['fas', 'chevron-right']" size="2x" @click="next_cards()" style="cursor:pointer"/>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col d-flex flex-column justify-content-center align-items-center">
                        <div class="add-sensor card text-white" @click="create_data.show_create_modal=true">
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
                    :bool_trigger="Object.keys(list_data.displayed_device).length == 0"
                ></wave_footer>
            </teleport>
        </div>

        <div v-if="Object.keys(list_data.displayed_device).length != 0">
            <div class="card-group d-flex justify-content-center align-items-center pt-3 pb-3">
                <div class="d-flex flex-column justify-content-center align-items-center ms-2" style="width: 3rem">
                    <font-awesome-icon v-if="slider_data.start - slider_data.step >= 0" :icon="['fas', 'chevron-left']" size="2x" @click="prev_cards()" style="cursor:pointer"/>
                </div>
                <transition :name="slider_data.transition_name" mode="out-in">
                    <div class="d-flex" :key="slider_data.start">
                        <div v-for="sensor in list_data.device_list.slice(slider_data.start, slider_data.end)" :key="sensor.id"
                            class="col-auto"
                            style="cursor: pointer"
                            @click="change_displayed_device(sensor)"
                        >
                            <div class="sensor-card card ms-2 me-2" :class="{ 'selected-card': list_data.displayed_device.id == sensor.id }" style="width: 18rem;">
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
                    <font-awesome-icon v-if="slider_data.start + slider_data.step < list_data.device_list.length" :icon="['fas', 'chevron-right']" size="2x" @click="next_cards()" style="cursor:pointer"/>
                </div>
            </div>

            <transition name="slide-right" mode="out-in">
                <div :key="list_data.displayed_device.id">
                    <mailbox_notifier_detail
                        :mailbox_notifier="list_data.displayed_device"
                    ></mailbox_notifier_detail>
                </div>
            </transition>
        </div>
    </div>
    </transition>

    <modal_window 
        :show_modal="create_data.show_create_modal"
        @close="create_data.show_create_modal=false; create_data.enable_create=false; create_data.form_err_msg='';"
    >
        <template v-slot:header>
            <h4 class="modal-title" id="myModalLabel">Add Mailbox Notifier</h4>
        </template>

        <template v-slot:body>
            <form id="create_room_sensor_form" class="sensor-form" @submit.prevent="create_mailbox_notifier()">
                <div v-if="create_data.form_err_msg" class="alert alert-danger" role="alert">
                    {{ create_data.form_err_msg }}
                </div>
                <div class="mb-3">
                    <label class="form-label">Device ID*</label>
                    <input type="text" class="form-control" v-model="create_data.device_id">
                    <small class="text-muted">Must correspond with device id registered to The Things Network</small>
                </div>
                <div class="mb-3">
                    <label class="form-label">Device Name</label>
                    <input type="text" class="form-control" v-model="create_data.device_name">
                </div>
                <div class="mb-3">
                    <label class="form-label">Description</label>
                    <textarea class="form-control" rows="3" v-model="create_data.device_description"></textarea>
                </div>
                <div class="mb-3">
                    <label class="form-check-label" for="notify_checkbox">Notify</label>
                    <input class="form-check-input ms-2" type="checkbox" id="notify_checkbox" v-model="create_data.should_notify">
                </div>
                <div v-if="create_data.should_notify" class="mb-3">
                    <label class="form-label">Emails</label>
                    <textarea class="form-control" rows="3" v-model="create_data.emails"></textarea>
                </div>
            </form>
        </template>

        <template v-slot:footer>
            <button type="submit" form="create_room_sensor_form" class="btn btn-success"
                :class="{ disabled: !create_data.enable_create }"
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
import { useMq } from "vue3-mq";

import mailbox_notifier_detail from "@/components/mailbox_notifier/mailbox_notifier_detail.vue";
import modal_window from "@/components/ui/modal_window.vue";
import wave_footer from "@/components/ui/wave_footer.vue";


const route = useRoute()
const mq = useMq();

onMounted(() => {
    if (mq.isPortrait) {
        slider_data.end = 1;
        slider_data.step = 1;
    }
    get_mailbox_notifier();
})

// DEVICE LIST
let list_data = reactive({
    device_list: [],
    displayed_device: {},
})

provide("update_mailbox_notifier", get_mailbox_notifier);


watch(() => route.params.device_id, () => {
    if (!route.params.device_id) {
        list_data.displayed_device = {};
    }
})

function get_mailbox_notifier() {
    axios
        .get("/api/v1/mailboxnotifier/")
        .then((resp) => {
            list_data.device_list = resp.data;

            if (route.params.device_id && route.params.device_id != "undefined") {
                var found_sensor = list_data.device_list.filter(sensor => {
                    return sensor.id == route.params.device_id
                })
                list_data.displayed_device = found_sensor[0];
            }
        })
}

function change_displayed_device(device) {
    if (list_data.displayed_device.id == device.id) {
        list_data.displayed_device = {};
        router.push({ name: 'mailbox_notifier_view' });
    } else {
        list_data.displayed_device = device;
        router.push({ name: 'mailbox_notifier_mail', params: { device_id: device.id } });
    }
}


// CREATE DEVICE
let create_data = reactive({
    show_create_model: false,
    enable_create: false,
    form_err_msg: "",
    
    device_id: "",
    device_name: "",
    device_description: "",
    should_notify: false,
    emails: "",
})


watch(() => create_data.device_id, () => {
    create_data.enable_create = true;
})

function create_mailbox_notifier() {
    let request_data = {
        device_id: create_data.device_id,
        device_name: create_data.device_name,
        device_description: create_data.device_description,
        should_notify: create_data.should_notify,
        emails: create_data.emails.length ? create_data.emails.split("\n").filter(n => n) : [],
    };
    axios  
        .post("/api/v1/mailboxnotifier/", request_data)
        .then(() => {
            get_mailbox_notifier();
            create_data.show_create_modal = false;
            create_data.device_id = "";
            create_data.device_name = "";
            create_data.device_description = "";
            create_data.should_notify = false;
            create_data.emails = [];
        })
        .catch((err) => {
            if (err.response.data) {
                if (err.response.data.device_id) {
                    create_data.form_err_msg = err.response.data.device_id[0].replace("This field", "device id");
                } else {
                    create_data.form_err_msg = err.response.data;
                }
            } else {
                alert(err);
            }
        })
}


// DEVICE SLIDER
let slider_data = reactive({
    start: 0,
    end: 3,
    step: 3,
    transition_name: "slide-left",
})


watch(() => mq.isLandscape, (isLandscape, wasLandscape) => {
    if (isLandscape && !wasLandscape) {
        slider_data.end += 2;
        slider_data.step += 2;
    } else if (!isLandscape && wasLandscape) {
        slider_data.end -= 2;
        slider_data.step -= 2;
    }
})

function next_cards() {
    slider_data.transition_name = "slide-left";
    slider_data.start += slider_data.step;
    slider_data.end += slider_data.step;
}

function prev_cards() {
    slider_data.transition_name = "slide-right";
    slider_data.start -= slider_data.step;
    slider_data.end -= slider_data.step;
}
</script>