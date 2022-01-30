<template>
<div class="p-2">
    <form @submit.prevent="save_configuration()">
        <div class="input-group w-50 mb-2">
            <div class="input-group-prepend">
                <span class="input-group-text">Number of displayed uplinks: </span>
            </div>
            <input type="number" class="form-control" :max="props.max_n" v-model="n">
        </div>
        <input type="range" class="w-100" min="0" :max="props.max_n"  :value="n">

        <div class="form-check mt-4">
            <label class="form-check-label">Show temperature readings</label>
            <input class="form-check-input" type="checkbox" v-model="show_temp">
        </div>
        <div class="form-check mt-2 mb-2">
            <label class="form-check-label">Show pressure readings</label>
            <input class="form-check-input" type="checkbox" v-model="show_pres">
        </div>

        <div v-if="user_state.is_authenticated" class="d-flex flex-row-reverse bd-highlight">
            <button type="submit" class="btn btn-success">Save configuration</button>
        </div>
        <div v-else>
            <unlogged_warning/>
        </div>
    </form>
</div>
</template>

<script setup>
/* eslint-disable */
import axios from "axios";

import { defineProps, inject, ref, watch } from 'vue';
import { useRoute } from "vue-router";

import unlogged_warning from "@/components/user/unlogged_warning.vue";


const props = defineProps({
    current_n: Number,
    max_n: Number,
    display_temp: Boolean,
    display_pres: Boolean,
})

let n = ref(props.current_n);
let show_temp = ref(props.display_temp);
let show_pres = ref(props.display_pres);

const update_room_sensor = inject("update_room_sensor");
const user_state = inject("user_state");
const route = useRoute()


watch(() => [props.current_n, props.display_temp, props.display_pressure], () => {
    update_form();
})


function update_form() {
    console.log("wtf", props)
    n.value = props.current_n;
    show_temp.value = props.display_temp;
    show_pres.value = props.display_pres;
}

function save_configuration() {
    let request_data = {
        displayed_uplinks_number: n.value,
        display_temperature: show_temp.value,
        display_pressure: show_pres.value,
    };
    axios
        .patch("/api/v1/roomsensor/" + route.params.device_id + "/", request_data)
        .then(() => {
            update_room_sensor();
        })
        .catch((err) => {
            alert(err);
        })
}
</script>