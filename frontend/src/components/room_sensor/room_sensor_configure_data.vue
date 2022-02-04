<template>
<div class="p-2">
    <form @submit.prevent>
        <div class="input-group w-50 mb-2">
            <div class="input-group-prepend">
                <span class="input-group-text">Number of displayed uplinks: </span>
            </div>
            <input type="number" class="form-control" :max="props.max_n" v-model="n">
        </div>
        <input type="range" id="range_slider" class="w-100" min="0" :max="props.max_n" v-model="n">

        <div class="form-check mt-4">
            <label class="form-check-label" for="show_temp_checkbox">Show temperature readings</label>
            <input class="form-check-input" type="checkbox" id="show_temp_checkbox" v-model="show_temp">
        </div>
        <div class="form-check mt-2 mb-2">
            <label class="form-check-label" for="show_pres_checkbox">Show pressure readings</label>
            <input class="form-check-input" type="checkbox" id="show_pres_checkbox" v-model="show_pres">
        </div>

        <div v-if="user_state.is_authenticated" class="d-flex flex-row-reverse bd-highlight">
            <div class="btn-group" role="group">
                <button class="btn btn-primary" @click="show_export_modal=true"><font-awesome-icon :icon="['fas', 'download']"/> Export options</button>
                <button type="submit" class="btn btn-success" @click="save_configuration()">Save configuration</button>
            </div>
        </div>
        <div v-else>
            <unlogged_warning/>
        </div>
    </form>

    <modal_window 
        :show_modal="show_export_modal"
        @close="show_export_modal=false; modal_err_msg='';"
    >
        <template v-slot:header>
            <h4 class="modal-title" id="myModalLabel">Export options</h4>
        </template>

        <template v-slot:body>
            <div v-if="modal_err_msg" class="alert alert-danger" role="alert">
                {{ modal_err_msg }}
            </div>
            <form @submit.prevent="uplinks_export()" id="uplinks_export_form">
                <div class="input-group">
                    <div class="input-group-prepend">
                        <span class="input-group-text">From: </span>
                    </div>
                    <input type="datetime-local" class="form-control" v-model="export_from">
                </div>

                <div class="input-group mt-2">
                    <div class="input-group-prepend" style="width: 4.25rem;">
                        <span class="input-group-text">To: </span>
                    </div>
                    <input type="datetime-local" class="form-control" v-model="export_to">
                </div>
                <small class="text-muted">Empty date will be converted to earliest/latest available date (not specifying neither date will export every uplink).</small>

                <div class="form-check mt-4">
                    <label class="form-check-label" for="export_temp_checkbox">Export temperature readings</label>
                    <input class="form-check-input" type="checkbox" id="export_temp_checkbox" v-model="export_temp">
                </div>
                <div class="form-check mt-2 mb-2">
                    <label class="form-check-label" for="export_pres_checkbox">Export pressure readings</label>
                    <input class="form-check-input" type="checkbox" id="export_pres_checkbox" v-model="export_pres">
                </div>
            </form>
        </template>

        <template v-slot:footer>
            <button type="submit" form="uplinks_export_form" class="btn btn-primary">Export</button>
        </template>
    </modal_window>
</div>
</template>

<script setup>
import axios from "axios";

import { defineProps, inject, ref, watch } from 'vue';
import { useRoute } from "vue-router";

import modal_window from "@/components/ui/modal_window.vue";
import unlogged_warning from "@/components/user/unlogged_warning.vue";


const props = defineProps({
    current_n: Number,
    max_n: Number,
    display_temp: Boolean,
    display_pres: Boolean,
})

// TODO: fix bug, range slider keeps resetting when moving through tabs
// display data options
let n = ref(props.current_n);
let show_temp = ref(props.display_temp);
let show_pres = ref(props.display_pres);
// export data
let modal_err_msg = ref("");
let show_export_modal = ref(false);
let export_from = ref("");
let export_to = ref("");
let export_temp = ref(false);
let export_pres = ref(false);

const update_room_sensor = inject("update_room_sensor");
const user_state = inject("user_state");
const route = useRoute()


watch(() => [props.current_n, props.display_temp, props.display_pressure], () => {
    update_form();
})


function update_form() {
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

function uplinks_export() {
    let request_data = {
        export_from: export_from.value,
        export_to: export_to.value,
        export_temp: export_temp.value,
        export_pres: export_pres.value,
    };
    axios
        .get("/sensor/export_uplinks/" + route.params.device_id + "/", {params: request_data})
        .then((resp) => {
            if (resp.data.status == "req_nok") {
                modal_err_msg.value = "You need to export at least one field.";
            } else {
                let content_disposition = resp.headers["content-disposition"];
                let file_name;
                if (content_disposition) {
                    file_name = content_disposition.split("filename=")[1].replace(/['"]+/g, "");
                } else {
                    file_name = "room_sensor_export.csv"
                }
    
                const anchor = document.createElement("a");
                anchor.href = "data:text/csv;charset=utf-8," + encodeURIComponent(resp.data);
                anchor.target = "_blank";
                anchor.download = file_name;
                anchor.click();
            }
        })
        .catch((err) => {
            alert(err);
        })
}
</script>