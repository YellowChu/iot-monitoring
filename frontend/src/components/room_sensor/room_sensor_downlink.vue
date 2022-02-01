<template>
<div>
    <div class="container-fluid">
        <div v-if="downlink_successfull" class="alert alert-success" role="alert">
            Downlink schedules successfully.
        </div>
        <div class="row mt-2">
            <div class="col-xl-6 col-lg-12 mt-2">
                <form class="sensor-form" id="downlink_form" @submit.prevent>
                    <div class="mb-3">
                        <label>Spreading factor</label>

                        <div class="input-group" style="margin-top:1rem;">
                            <select class="form-control" v-model="spreading_factor">
                                <option>Unchanged</option>
                                <option>SF7</option>
                                <option>SF8</option>
                                <option>SF9</option>
                                <option>SF10</option>
                                <option>SF11</option>
                                <option>SF12</option>
                            </select>
                            <div class="input-group-prepend">
                                <span class="input-group-text" id="">Uplink interval: {{ sleep_time }} minutes</span>
                            </div>
                        </div>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">LED color</label>
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <div class="input-group-text" style="height: 3rem; cursor: pointer" @click="enable_color_change = !enable_color_change">
                                    <input type="checkbox" style="cursor: pointer" :checked="enable_color_change">
                                    <small style="margin-left: 0.5rem;">Change color</small>
                                </div>
                            </div>
                            <input
                                type="color"
                                class="form-control"
                                title="Choose your color"
                                v-model="color"
                                style="height: 3rem;"
                                :disabled="!enable_color_change"
                            >
                        </div>
                    </div>
                    <div v-if="user_state.is_authenticated" class="d-flex flex-row-reverse bd-highlight mb-3">
                        <button class="btn btn-primary" :disabled="!enable_downlink" @click="show_downlink_modal=true">Schedule downlink</button>
                    </div>
                    <div v-else>
                        <unlogged_warning/>
                    </div>
                </form>
            </div>
            <div class="col-xl-6 col-lg-12 mt-2">
                <div class="jumbotron jumbotron-fluid bg-light">
                    <div class="container">
                        <h4 class="display-6">Description</h4>
                        <p class="description">
                            You are able to issue downlink to the lora end node. The available commands are chaning spreding factor and
                            changing led color.
                        </p>
                        <p class="description">
                            The spreading factor (SF) impacts the communication performance of LoRa, which uses an SF between 7 and 12. 
                            A larger SF increases the time on air, which increases energy consumption, reduces the data rate, and 
                            improves communication range.
                        </p>
                        <p class="description">
                            Therefore, as the spreading factor increases the time interval between uplinks increases as well.
                        </p>
                    </div>
                </div>
            </div>
        </div>  
    </div>

    <modal_window 
        :show_modal="show_downlink_modal"
        @close="show_downlink_modal=false"
    >
        <template v-slot:header>
            <h4 class="modal-title" id="myModalLabel">Do you really want to schedule downlink?</h4>
        </template>

        <template v-slot:body>
            <div v-if="modal_err_msg" class="alert alert-danger" role="alert">
                {{ modal_err_msg }}
            </div>
            <div class="mb-3">
                <label class="form-label"><b>Spreading factor:</b> {{ spreading_factor }}</label><br/>
                <label class="form-label"><b>Uplink interval:</b> {{ sleep_time }} minutes</label><br/>
                <label v-if="enable_color_change" class="form-label"><b>Color:</b> <span :style="{color: color}">&#9632;</span></label>
                <label v-else class="form-label"><b>Color:</b> Unchanged</label>
            </div>
        </template>

        <template v-slot:footer>
            <button class="btn btn-primary" type="submit" form="downlink_form" @click="schedule_downlink()">Schedule downlink</button>
        </template>
    </modal_window>
</div>
</template>

<style scoped>
.home-sensor-downlink {
    margin-top: 1rem;
}
.sensor-form {
    text-align: left;
}
.description {
    text-align: left;
}
</style>

<script setup>
import axios from "axios";

import { inject, ref, watch } from 'vue';

import modal_window from "@/components/ui/modal_window.vue";
import unlogged_warning from "@/components/user/unlogged_warning.vue";


let spreading_factor = ref("Unchanged");
let sleep_time = ref("unknown");
let enable_color_change = ref(false);
let color = ref("#444444");

let enable_downlink = ref(false);
let show_downlink_modal = ref(false);
let modal_err_msg = ref("");
let downlink_successfull = ref(false);

const user_state = inject("user_state");

const sf_sleep = {
    "Unchanged": "unknown",
    "SF7": 5,
    "SF8": 10,
    "SF9": 15,
    "SF10": 30,
    "SF11": 60,
    "SF12": 90,
}


watch(enable_color_change, (enabled) => {
    if (enabled) {
        color.value = "#006400";
    } else {
        color.value = "#444444";
    }
    check_form();
})

watch(spreading_factor, (sf) => {
    sleep_time.value = sf_sleep[sf];
    check_form();
})


function schedule_downlink() {
    let request_data = {
        spreading_factor: spreading_factor.value,
        color_code: enable_color_change.value ? color.value.substring(1).toUpperCase() : "Unchanged",
    };
    axios
        .get("/sensor/schedule_downlink/", {params: request_data})
        .then((resp) => {
            if (resp.data.status == "ok") {
                show_downlink_modal.value = false;
                downlink_successfull.value = true;
            } else {
                modal_err_msg.value = "Could not schedule downlink. Some problems with The Things Network.";
            }
        })
        .catch((err) => {
            alert(err);
        })
}

function check_form() {
    if (spreading_factor.value == "Unchanged" && !enable_color_change.value) {
        enable_downlink.value = false;
    } else {
        enable_downlink.value = true;
    }
}
</script>