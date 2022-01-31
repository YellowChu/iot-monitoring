<template>
    <div v-if="props.room_sensor.id" class="row">
        <ul class="nav nav-tabs">
            <li class="nav-item">
                <router-link
                    :to="{ name: 'room_sensor_data', params: { device_id: props.room_sensor.id } }"
                    class="nav-link"
                    :class="{active: route.name==='room_sensor_data'}"
                >
                    Data
                </router-link>
            </li>
            <li class="nav-item">
                <router-link
                    :to="{ name: 'room_sensor_downlink', params: { device_id: props.room_sensor.id } }"
                    class="nav-link"
                    :class="{active: route.name==='room_sensor_downlink'}"
                >
                    Schedule downlink
                </router-link>
            </li>
            <li class="nav-item">
                <router-link
                    :to="{ name: 'room_sensor_settings', params: { device_id: props.room_sensor.id } }"
                    class="nav-link"
                    :class="{active: route.name==='room_sensor_settings'}"
                >
                    Settings
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
</template>

<style scoped>
.home-sensor-detail {
    margin-top: 1rem;
}
</style>

<script setup>
import { defineProps } from "vue";
import { useRoute } from "vue-router";


const route = useRoute()

const props = defineProps({
    room_sensor: Object,
})
</script>