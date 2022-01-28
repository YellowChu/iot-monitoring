<template>
    <div v-if="props.room_sensor.id" class="row">
        <ul class="nav nav-tabs">
            <li class="nav-item">
                <router-link
                    :to="{ name: 'home_sensor_data', params: { device_id: room_sensor.id } }"
                    class="nav-link"
                    :class="{active: route.name==='home_sensor_data'}"
                >
                    Data
                </router-link>
            </li>
            <li class="nav-item">
                <router-link
                    :to="{ name: 'home_sensor_command', params: { device_id: room_sensor.id } }"
                    class="nav-link"
                    :class="{active: route.name==='home_sensor_command'}"
                >
                    Issue command
                </router-link>
            </li>
            <li class="nav-item">
                <router-link
                    :to="{ name: 'home_sensor_settings', params: { device_id: room_sensor.id } }"
                    class="nav-link"
                    :class="{active: route.name==='home_sensor_settings'}"
                >
                    Settings
                </router-link>
            </li>
        </ul>

        <router-view
            :data_list="room_sensor.sensor_data_list"
            :sensor_name="room_sensor.device_name"
            :sensor_description="room_sensor.device_description"
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
import { defineProps, toRefs } from "vue";
import { useRoute } from "vue-router";


const route = useRoute()

const props = defineProps({
    room_sensor: Object,
})

const { room_sensor } = toRefs(props);
</script>