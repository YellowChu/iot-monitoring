<template>
<div class="container-fluid">
    <div class="row mt-5 mb-5 d-flex justify-content-center align-items-center">
        <h2 class="fw-bold justify-content-center" style="color: #074879;">Gathered data</h2>
    </div>
    <div id="accordion" style="margin-top: 1rem; text-align: left">
        <div class="card">
            <div class="card-header" data-bs-toggle="collapse" href="#data_settings_collapse" style="cursor: pointer;">
                <a class="btn">
                    <font-awesome-icon :icon="['fas', 'sliders-h']"/>
                    Additional options
                </a>
            </div>
            <div id="data_settings_collapse" class="collapse" data-bs-parent="#accordion">
                <div class="card-body">
                    <room_sensor_configure_data
                        :current_n="props.displayed_uplinks_count"
                        :max_n="props.uplinks_count"
                        :display_temp="props.display_temperature"
                        :display_pres="props.display_pressure"
                    ></room_sensor_configure_data>
                </div>
            </div>
        </div>
    </div>

    <div v-if="props.display_temperature" class="row mt-3" style="margin-top: 2rem;">
        <div class="col-xl-8 col-lg-12 mt-2" style="margin-top: 1rem;">
            <div class="card border-left-primary shadow">
                <div class="card-body">
                    <h5 class="card-title"><b>Temperature Readings</b></h5>
                    <line_chart
                        :xaxis="props.data_list.map(obj => obj.time)"
                        :yaxis="props.data_list.map(obj => obj.temperature)"
                        color="#700000"
                        series_name="Temperature [°C]"
                    ></line_chart>
                </div>
            </div>
        </div>

        <div class="col-xl-4 col-lg-12 mt-2">
            <div class="card border-left-primary shadow">
                <div class="card-body">
                    <div class="tableFixHead">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th scope="col" class="bg-dark text-white"></th>
                                    <th scope="col" class="bg-dark text-white">Time</th>
                                    <th scope="col" class="bg-dark text-white">Temperature [°C]</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(data, idx) in props.data_list" :key="data.time + idx">
                                    <th scope="row">{{ idx }}</th>
                                    <td>{{ parse_date(data.time) }}</td>
                                    <td>{{ data.temperature.toFixed(2) }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div v-if="props.display_pressure" class="row mt-5">
        <div class="col-xl-8 col-lg-12 mt-2" style="margin-top: 1rem;">
            <div class="card border-left-primary shadow">
                <div class="card-body">
                    <h5 class="card-title"><b>Pressure Readings</b></h5>
                    <line_chart
                        :xaxis="props.data_list.map(obj => obj.time)"
                        :yaxis="props.data_list.map(obj => obj.pressure / 1000)"
                        color="#002D62"
                        series_name="Pressure [kPa]"
                    ></line_chart>  
                </div>
            </div>
        </div>

        <div class="col-xl-4 col-lg-12 mt-2">
            <div class="card border-left-primary shadow">
                <div class="card-body">
                    <div class="tableFixHead">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th scope="col" class="bg-dark text-white"></th>
                                    <th scope="col" class="bg-dark text-white">Time</th>
                                    <th scope="col" class="bg-dark text-white">Pressure [kPa]</th>
                                </tr>
                            </thead>    
                            <tbody>
                                <tr v-for="(data, idx) in props.data_list" :key="data.time + idx">
                                    <th scope="row">{{ idx }}</th>
                                    <td>{{ parse_date(data.time) }}</td>
                                    <td>{{ (data.pressure / 1000).toFixed(2) }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<style scoped>
.home-sensor-data {
    margin-top: 1rem;
}

.tableFixHead { 
    overflow: auto;
    height: 41rem;
}
.tableFixHead thead th {
    position: sticky;
    top: 0;
    z-index: 1;
}

table::-webkit-scrollbar {
    width: 0.4rem;
}

table::-webkit-scrollbar-track {
    background: #1e1e24;
}

table::-webkit-scrollbar-thumb {
    background: #b2b2bc;
}

table  { 
    border-collapse: collapse;
    width: 100%;
}
th, td { padding: 8px 16px; }
th     { background:#eee; }
</style>

<script setup>
import moment from "moment";

import { inject, defineProps } from "vue";

import line_chart from "@/components/data_presentation/line_chart.vue";
import room_sensor_configure_data from "@/components/room_sensor/room_sensor_configure_data.vue";


// init
const props = defineProps({
    data_list: Array,
    uplinks_count: Number,
    displayed_uplinks_count: Number,
    display_temperature: Boolean,
    display_pressure: Boolean,
})

const update_room_sensor = inject("update_room_sensor");


// websocket listen
const sensor_socket = new WebSocket(
    (window.location.protocol === "https:" ? "wss" : "ws")
    + "://"
    + window.location.host
    + "/ws/sensor/"
);

sensor_socket.onmessage = function(e) {
    const msg = JSON.parse(e.data);
    if (msg.message == "New uplink") {
        update_room_sensor();
    }
    console.log(msg.message);
}

sensor_socket.onclose = function() {
    console.error("Socket closed for some reason");
}


// methods
function parse_date(date_str) {
    let date = new Date(Date.parse(date_str));
    // return date.toUTCString()
    return moment(date).format("DD.MM.YYYY HH:mm");
}
</script>