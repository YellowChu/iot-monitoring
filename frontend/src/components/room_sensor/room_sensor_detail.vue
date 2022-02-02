<template>
    <div v-if="props.room_sensor.id" class="row d-flex justify-content-center align-items-center mt-4" style="width: 100rem;">
        <div class="col-xl-12 col-md-6">
            <div class="card pt-2 pb-4" style="box-shadow: 0 10px 20px rgba(0,0,0,.12), 0 4px 8px rgba(0,0,0,.06);">
                <ul class="nav nav-tabs ps-4 fw-bold">
                    <li class="nav-item mb-0">
                        <router-link
                            :to="{ name: 'room_sensor_dashboard', params: { device_id: props.room_sensor.id } }"
                            class="nav-link"
                            :class="{active: route.name==='room_sensor_dashboard'}"
                        >
                            <font-awesome-icon :icon="['fas', 'digital-tachograph']"/> Dashboard
                        </router-link>
                    </li>
                    <li class="nav-item mb-0">
                        <router-link
                            :to="{ name: 'room_sensor_data', params: { device_id: props.room_sensor.id } }"
                            class="nav-link"
                            :class="{active: route.name==='room_sensor_data'}"
                        >
                            <font-awesome-icon :icon="['fas', 'chart-line']"/> Data
                        </router-link>
                    </li>
                    <li class="nav-item mb-0">
                        <router-link
                            :to="{ name: 'room_sensor_downlink', params: { device_id: props.room_sensor.id } }"
                            class="nav-link"
                            :class="{active: route.name==='room_sensor_downlink'}"
                        >
                            <font-awesome-icon :icon="['fas', 'caret-square-down']"/> Schedule downlink
                        </router-link>
                    </li>
                    <li class="nav-item mb-0">
                        <router-link
                            :to="{ name: 'room_sensor_settings', params: { device_id: props.room_sensor.id } }"
                            class="nav-link"
                            :class="{active: route.name==='room_sensor_settings'}"
                        >
                            <font-awesome-icon :icon="['fas', 'wrench']"/> Settings
                        </router-link>
                    </li>
                </ul>
        
                <router-view
                    :data_list="props.room_sensor.sensor_data_list"
                    :uplinks_count="props.room_sensor.uplinks_count"
                    :displayed_uplinks_count="props.room_sensor.displayed_uplinks_count"
                    :display_temperature="props.room_sensor.display_temperature"
                    :display_pressure="props.room_sensor.display_pressure"
                    :sensor_name="props.room_sensor.device_name"
                    :sensor_description="props.room_sensor.device_description"
                >
                </router-view>
            </div>
        </div>
    </div>
</template>


<script setup>
import { defineProps } from "vue";
import { useRoute } from "vue-router";


const route = useRoute()

const props = defineProps({
    room_sensor: Object,
})
</script>