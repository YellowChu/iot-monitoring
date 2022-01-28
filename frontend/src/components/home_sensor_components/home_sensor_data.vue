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
                <div class="tableFixHead">
                    <thead>
                        <tr>
                            <th scope="col">i</th>
                            <th scope="col">Time</th>
                            <th scope="col">Temperature [°C]</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(data, idx) in props.data_list" :key="data.time + idx">
                            <th scope="row">{{ idx }}</th>
                            <td>{{ parse_date(data.time) }}</td>
                            <td>{{ data.temperature.toFixed(2) }}</td>
                        </tr>
                    </tbody>
                </div>
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
                <div class="tableFixHead">
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
                            <td>{{ data.pressure.toFixed(2) }}</td>
                        </tr>
                    </tbody>
                </div>
            </table>
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
    height: 500;
}
.tableFixHead thead th {
    position: sticky;
    top: 0;
    z-index: 1;
}

table  { 
    border-collapse: collapse;
    width: 100%;
}
th, td { padding: 8px 16px; }
th     { background:#eee; }
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