<template>
<div class="row home-sensor-data" style="text-align: left">
    <div class="row" style="margin-top: 1rem;">
        <h4>Temperature readings</h4>
        <div class="col-8" style="margin-top: 1rem;">
            <line_chart
                :xaxis="props.data_list.map(obj => obj.time)"
                :yaxis="props.data_list.map(obj => obj.temperature)"
                color="#700000"
            ></line_chart>
        </div>
        <div class="col">
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col"></th>
                        <th scope="col">Time</th>
                        <th scope="col">Temperature [°C]</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(data, idx) in props.data_list" :key="data.time + idx">
                        <th scope="row">{{ idx }}</th>
                        <td>{{ parse_date(data.time) }}</td>
                        <td>{{ parse_temp(data.temperature) }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="row" style="margin-top: 2rem;">
        <h4>Pressure readings</h4>
        <div class="col-8" style="margin-top: 1rem;">
            <line_chart
                :xaxis="props.data_list.map(obj => obj.time)"
                :yaxis="props.data_list.map(obj => obj.pressure)"
                color="#002D62"
            ></line_chart>
        </div>
        <div class="col">
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col"></th>
                        <th scope="col">Time</th>
                        <th scope="col">Pressure [kPa]</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(data, idx) in props.data_list" :key="data.time + idx">
                        <th scope="row">{{ idx }}</th>
                        <td>{{ parse_date(data.time) }}</td>
                        <td>{{ parse_temp(data.pressure) }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>


    <!-- <table class="table">
        <thead>
            <tr>
                <th scope="col"></th>
                <th scope="col">Time</th>
                <th scope="col">Temperature [°C]</th>
                <th scope="col">Pressure [kPa]</th>
                <th scope="col">Battery [V]</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(data, idx) in props.data_list" :key="data.time + idx">
                <th scope="row">{{ idx }}</th>
                <td>{{ parse_date(data.time) }}</td>
                <td>{{ parse_temp(data.temperature) }}</td>
                <td>{{ parse_pres(data.pressure) }}</td>
                <td>{{ parse_batt(data.battery) }}</td>
            </tr>
        </tbody>
    </table> -->
</div>
</template>

<style scoped>
.home-sensor-data {
    margin-top: 1rem;
}
</style>

<script setup>
/* eslint-disable */
import { inject, defineProps } from "vue";

import moment from "moment";
import line_chart from "@/components/data_presentation/line_chart.vue";


// init
const props = defineProps({
    data_list: Array,
})

const update_room_sensor = inject("update_room_sensor");


// websocket listen
const sensor_socket = new WebSocket(
    "ws://"
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

function parse_temp(temp) {
    return temp.toFixed(2)
}

function parse_pres(pres) {
    return (pres / 1000).toFixed(2)
}

function parse_batt(batt) {
    return batt.toFixed(2)
}
</script>