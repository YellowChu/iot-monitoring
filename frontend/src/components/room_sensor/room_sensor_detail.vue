<template>
    <div v-if="props.room_sensor.id" class="row d-flex justify-content-center align-items-center mt-4" style="width: 100rem;">
        <div class="col-xl-12 col-md-6">
            <div class="card pt-2 pb-4" style="box-shadow: 0 10px 20px rgba(0,0,0,.12), 0 4px 8px rgba(0,0,0,.06);">
                <nav :class="{'navbar d-flex fixed-bottom navbar-expand justify-content-center' : mq.isPortrait }">
                    <ul :class="{ 'nav nav-tabs ps-4 fw-bold': mq.isLandscape, 'navbar-nav p-3': mq.isPortrait }">
                        <li class="nav-item  ms-5 me-5" :class="{ 'mb-0': mq.isLandscape }">
                            <router-link
                                :to="{ name: 'room_sensor_dashboard', params: { device_id: props.room_sensor.id } }"
                                class="nav-link"
                                :class="{active: route.name==='room_sensor_dashboard'}"
                            >
                                <font-awesome-icon :icon="['fas', 'digital-tachograph']" :size="mq.isPortrait ? '4x' : '1x'"/>
                                <span v-if="mq.isLandscape"> Dashboard</span>
                            </router-link>
                        </li>
                        <li class="nav-item  ms-5 me-5" :class="{ 'mb-0': mq.isLandscape }">
                            <router-link
                                :to="{ name: 'room_sensor_data', params: { device_id: props.room_sensor.id } }"
                                class="nav-link"
                                :class="{active: route.name==='room_sensor_data'}"
                            >
                                <font-awesome-icon :icon="['fas', 'chart-line']" :size="mq.isPortrait ? '4x' : '1x'"/>
                                <span v-if="mq.isLandscape"> Data</span>
                            </router-link>
                        </li>
                        <li class="nav-item  ms-5 me-5" :class="{ 'mb-0': mq.isLandscape }">
                            <router-link
                                :to="{ name: 'room_sensor_downlink', params: { device_id: props.room_sensor.id } }"
                                class="nav-link"
                                :class="{active: route.name==='room_sensor_downlink'}"
                            >
                                <font-awesome-icon :icon="['fas', 'caret-square-down']" :size="mq.isPortrait ? '4x' : '1x'"/>
                                <span v-if="mq.isLandscape"> Schedule downlink</span>
                            </router-link>
                        </li>
                        <li class="nav-item  ms-5 me-5" :class="{ 'mb-0': mq.isLandscape }">
                            <router-link
                                :to="{ name: 'room_sensor_settings', params: { device_id: props.room_sensor.id } }"
                                class="nav-link"
                                :class="{active: route.name==='room_sensor_settings'}"
                            >
                                <font-awesome-icon :icon="['fas', 'wrench']" :size="mq.isPortrait ? '4x' : '1x'"/>
                                <span v-if="mq.isLandscape"> Settings</span>
                            </router-link>
                        </li>
                    </ul>
                </nav>
        
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

<style scoped>
.navbar {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
    background: linear-gradient(#9198e5, #c191e5);
}

.nav-link-bot {
    color: white;
}
.active {
    color: #e66465;
}
</style>

<script setup>
import { useRoute } from "vue-router";
import { useMq } from "vue3-mq";


const route = useRoute()
const mq = useMq();

const props = defineProps({
    room_sensor: Object,
})
</script>