<template>
<div class="container-fluid">
    <div class="row mt-5 mb-5 d-flex justify-content-center align-items-center">
        <h2 class="fw-bold justify-content-center" style="color: #074879;">Car Location</h2>
    </div>

    <div class="row mt-3" style="text-align: left; height: 50vh; width: 100%;">
        <div class="container">
            <l-map
                v-model="map_data.zoom"
                v-model:zoom="map_data.zoom"
                :center="[map_data.latitude, map_data.longitude]"
            >
                <l-tile-layer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                ></l-tile-layer>


                <l-marker :lat-lng="[map_data.latitude, map_data.longitude]">
                    <l-tooltip>
                        Your car [{{ props.data_list[0].time }}]
                    </l-tooltip>
                </l-marker>
            </l-map>
        </div>
    </div>
</div>
</template>


<script setup>
import {
    LMap,
    LTileLayer,
    LMarker,
    LTooltip,
} from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";

import { reactive } from "vue";


const props = defineProps({
    data_list: Array,
})

console.log(props.data_list);

const map_data = reactive({
    zoom: 18,
    latitude: props.data_list[0].latitude,
    longitude: props.data_list[0].longitude,
})
</script>