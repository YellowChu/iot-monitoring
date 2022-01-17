<template>
<div class="row home-sensor-data">
    <table class="table">
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
    </table>

    <line_chart></line_chart>
</div>
</template>

<style scoped>
.home-sensor-data {
    margin-top: 1rem;
}
</style>

<script setup>
import { defineProps } from "vue";

import line_chart from "@/components/data_presentation/line_chart.vue"

const props = defineProps({
    data_list: Array,
})

function parse_date(date_str) {
    let date = new Date(Date.parse(date_str));
    return date.toUTCString()
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