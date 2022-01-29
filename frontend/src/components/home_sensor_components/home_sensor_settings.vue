<template>
<div class="home-sensor-settings" style="margin-top: 1rem;">
    <div class="row">
        <form class="sensor-form" @submit.prevent="save_changes()">
            <div class="mb-3">
                <label class="form-label">Name</label>
                <input type="text" class="form-control" v-model="name">
            </div>
            <div class="mb-3">
                <label class="form-label">Description</label>
                <textarea class="form-control" rows="3" v-model="description"></textarea>
            </div>
            <div class="mb-3">
                <div class="btn-group" role="group" aria-label="Basic example">
                    <button type="submit" class="btn btn-primary" :class="{ disabled: !data.enable_save }">Save Changes</button>
                    <button class="btn btn-danger" @click="data.show_delete_modal=true">Delete Sensor</button>
                </div>
            </div>
        </form>
    </div>

    <modal_window 
        :show_modal="data.show_delete_modal"
        @close="data.show_delete_modal=false"
    >
        <template v-slot:header>
            <h4 class="modal-title" id="myModalLabel">Do you really want to delete this sensor?</h4>
        </template>

        <template v-slot:body>
            <div v-if="data.form_err_msg" class="alert alert-danger" role="alert">
                {{ data.form_err_msg }}
            </div>
            <div class="mb-3">
                <label class="form-label"><b>Device name:</b> {{ props.sensor_name }}</label>
            </div>
        </template>

        <template v-slot:footer>
            <button class="btn btn-danger" @click="delete_room_sensor()">Delete</button>
        </template>
    </modal_window>
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
import axios from "axios";

import { defineProps, inject, reactive, ref, watch } from "vue";
import router from "@/router";
import { useRoute } from "vue-router";

import modal_window from "@/components/ui/modal_window.vue";


const props = defineProps({
    sensor_name: String,
    sensor_description: String,
})

let name = ref(props.sensor_name);
let description = ref(props.sensor_description);

let data = reactive({
    // patch sensor data
    enable_save: false,
    // delete sensor data
    form_err_msg: "",
    show_delete_modal: false,
})

const update_room_sensor = inject("update_room_sensor");
const route = useRoute()


watch([name, description], () => {
    data.enable_save = true;
})


function save_changes() {
    let request_data = {
        device_name: name.value,
        device_description: description.value,
    };
    axios
        .patch("/api/v1/roomsensor/" + route.params.device_id + "/", request_data)
        .then(() => {
            data.enable_save = false;
            update_room_sensor();
        })
        .catch((err) => {
            alert(err);
        })
}

function delete_room_sensor() {
    axios
        .delete("/api/v1/roomsensor/" + route.params.device_id + "/")
        .then(() => {
            data.show_delete_modal = false;
            update_room_sensor();
            router.push({ name: 'home_sensor_list' });
        })
        .catch((err) => {
            alert(err);
        })
}
</script>