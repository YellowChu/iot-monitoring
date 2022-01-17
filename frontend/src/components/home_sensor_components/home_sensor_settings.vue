<template>
<div>
    <div class="home-sensor-command">
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
                    <button type="submit" class="btn btn-primary">Save</button>
                </div>
            </form>
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
import axios from "axios";

import { defineProps, inject, ref } from "vue";
import { useRoute } from "vue-router";

const update_room_sensor = inject("update_room_sensor");

const props = defineProps({
    sensor_name: String,
    sensor_description: String,
})

let name = ref(props.sensor_name);
let description = ref(props.sensor_description);

const route = useRoute()

function save_changes() {
    let data = {
        device_name: name.value,
        device_description: description.value,
    }
    axios
        .patch("/api/v1/roomsensor/" + route.params.device_id + "/", data)
        .then(() => {
            update_room_sensor();
        })
        .catch((err) => {
            alert(err);
        })

    console.log("form submitted");
}
</script>