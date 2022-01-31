<template>
<div class="container-fluid">
    <div class="row mt-3" style="text-align: left;">
        <div class="col-xl-3 col-md-6 mb-4">
            <div class="card border-left-primary shadow h-100 py-2" style="border-left: 8px solid rgb(28, 28, 28);">
                <div class="card-body">
                    <h5 class="card-title text-dark"><b>Spreading Factor</b></h5>
                    <div class="row">
                        <div class="col">
                            <p class="fs-2">{{ dashboard_data.last_sf_reading }}</p>
                        </div>
                        <div class="col pe-3 ms-5 text-muted">
                            <font-awesome-icon :icon="['fas', 'wave-square']" size="3x"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-3 col-md-6 mb-4">
            <div class="card border-left-primary shadow h-100 py-2" style="border-left: 8px solid rgba(23, 86, 2, 0.749);">
                <div class="card-body">
                    <h5 class="card-title text-success"><b>Battery Voltage</b></h5>
                    <div class="row">
                        <div class="col">
                            <p class="fs-2">{{ dashboard_data.last_battery_reading }} V</p>
                        </div>
                        <div class="col pe-3 ms-5 text-muted">
                            <font-awesome-icon :icon="['fas', 'battery-full']" size="3x"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-3 col-md-6 mb-4">
            <div class="card border-left-primary shadow h-100 py-2" style="border-left: 8px solid rgb(29, 77, 223);">
                <div class="card-body">
                    <h5 class="card-title text-primary"><b>Consumed Airtime</b></h5>
                    <div class="row">
                        <div class="col">
                            <p class="fs-2">{{ dashboard_data.consumed_airtime_sum }} s</p>
                        </div>
                        <div class="col mt-3 pe-3">
                            <input type="range" :value="dashboard_data.consumed_airtime_sum" max="20" disabled>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-3 col-md-6 mb-4">
            <div class="card border-left-primary shadow h-100 py-2" style="border-left: 8px solid rgba(87, 87, 87, 0.297);">
                <div class="card-body">
                    <h5 class="card-title text-muted"><b>Scheduled Downlinks</b></h5>
                    
                    <div class="row">
                        <div class="col">
                            <p class="fs-3"><i>Coming..</i></p>
                        </div>
                        <div class="col pe-3 ms-5 text-muted">
                            <font-awesome-icon :icon="['fas', 'chevron-down']" size="3x"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="row mt-2">
        <div class="col-xl-6 col-lg-12 mt-2">
            <div class="card border-left-primary shadow h-100 py-2">
                <div class="card-body">
                    <h5 class="card-title text-primary"><b>Spreading Factor Count</b></h5>
                    <div class="">
                        <donut_chart
                            :labels='["SF07", "SF08", "SF09", "SF10", "SF11", "SF12"]'
                            :sf_counts="dashboard_data.sf_counts"
                        ></donut_chart>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-6 col-lg-12 mt-2">
            <div class="card border-left-primary shadow h-100 py-2">
                <div class="card-body">
                    <h5 class="card-title text-primary"><b><i>Gateways used (coming..)</i></b></h5>
                    <div class="">
                        <donut_chart
                            :labels='["GW1", "GW2", "GW3", "GW4", "GW5"]'
                            :sf_counts='[24, 34, 2, 12, 1]'
                        ></donut_chart>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script setup>
/* eslint-disable */
import axios from "axios"

import { inject, onMounted, reactive } from "vue";
import router from "@/router";
import { useRoute } from "vue-router";

import donut_chart from "@/components/data_presentation/donut_chart.vue"


let dashboard_data = reactive({
    uplinks: [],
    last_battery_reading: null,
    last_sf_reading: null,
    consumed_airtime_sum: null,
    sf_counts: [],
})

const route = useRoute()

onMounted(() => {
    get_uplinks();
})

function get_uplinks() {
    axios
        .get("/api/v1/roomsensoruplinks/" + route.params.device_id + "/")
        .then((resp) => {
            console.log(resp.data);
            let uplinks_data = resp.data.uplinks_data

            dashboard_data.uplinks = uplinks_data;
            dashboard_data.last_battery_reading = resp.data.last_battery_reading.toFixed(2);
            dashboard_data.last_sf_reading = resp.data.last_sf_reading;

            dashboard_data.consumed_airtime_sum = uplinks_data.map(uplink => uplink.consumed_airtime).reduce((a, b) => a + b, 0).toFixed(3);
            dashboard_data.sf_counts = [
                uplinks_data.filter(uplink => uplink.spreading_factor == 7).length,
                uplinks_data.filter(uplink => uplink.spreading_factor == 8).length,
                uplinks_data.filter(uplink => uplink.spreading_factor == 9).length,
                uplinks_data.filter(uplink => uplink.spreading_factor == 10).length,
                uplinks_data.filter(uplink => uplink.spreading_factor == 11).length,
                uplinks_data.filter(uplink => uplink.spreading_factor == 12).length,
            ]
            console.log(dashboard_data.sf_counts);
        })
}
</script>