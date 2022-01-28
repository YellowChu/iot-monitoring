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
                    <button type="submit" class="btn btn-primary">Save Changes</button>
                    <button class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#delete_sensor">Delete Sensor</button>
                </div>
            </div>
        </form>
    </div>

    <div class="modal fade" id="delete_sensor" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title" id="myModalLabel">Do you really want to delete this sensor?</h4>
                </div>
                <div class="modal-footer">
                    <button class="btn btn-danger" @click="delete_room_sensor()">Delete</button>
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
/* eslint-disable */
import axios from "axios";

import { defineProps, inject, ref } from "vue";
import router from "@/router";
import { useRoute } from "vue-router";


const props = defineProps({
    sensor_name: String,
    sensor_description: String,
})

let name = ref(props.sensor_name);
let description = ref(props.sensor_description);

const update_room_sensor = inject("update_room_sensor");
const route = useRoute()


function save_changes() {
    let data = {
        device_name: name.value,
        device_description: description.value,
    };
    axios
        .patch("/api/v1/roomsensor/" + route.params.device_id + "/", data)
        .then(() => {
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
            router.push({ name: 'home_sensor_list' });
        })
        .catch((err) => {
            alert(err);
        })
}
</script>