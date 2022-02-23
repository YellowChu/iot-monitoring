<template>
    <div v-if="props.car_tracker.id" class="row d-flex justify-content-center align-items-center mt-4" style="width: 100rem;">
        <div class="col-xl-8 col-md-6">
            <div class="card pt-2 pb-4" style="box-shadow: 0 10px 20px rgba(0,0,0,.12), 0 4px 8px rgba(0,0,0,.06);">
                <nav :class="{'navbar d-flex fixed-bottom navbar-expand justify-content-center' : mq.isPortrait }">
                    <ul :class="{ 'nav nav-tabs ps-4 fw-bold': mq.isLandscape, 'navbar-nav p-3': mq.isPortrait }">
                        <li class="nav-item  ms-5 me-5" :class="{ 'mb-0': mq.isLandscape }">
                            <router-link
                                :to="{ name: 'car_tracker_location', params: { device_id: props.car_tracker.id } }"
                                class="nav-link"
                                :class="{active: route.name==='car_tracker_location'}"
                            >
                                <font-awesome-icon :icon="['fas', 'map-marked']" :size="mq.isPortrait ? '4x' : '1x'"/>
                                <span v-if="mq.isLandscape"> Location</span>
                            </router-link>
                        </li>
                        <li class="nav-item  ms-5 me-5" :class="{ 'mb-0': mq.isLandscape }">
                            <router-link
                                :to="{ name: 'car_tracker_settings', params: { device_id: props.car_tracker.id } }"
                                class="nav-link"
                                :class="{active: route.name==='car_tracker_settings'}"
                            >
                                <font-awesome-icon :icon="['fas', 'wrench']" :size="mq.isPortrait ? '4x' : '1x'"/>
                                <span v-if="mq.isLandscape"> Settings</span>
                            </router-link>
                        </li>
                    </ul>
                </nav>
        
                <router-view
                    :data_list="fake"
                    :sensor_name="props.car_tracker.device_name"
                    :sensor_description="props.car_tracker .device_description"
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
    car_tracker: Object,
});

const fake = [
    {
        time: "20.2.2022 17:22",
        latitude: 49.219250,
        longitude: 16.523830,
    },
    {
        time: "20.2.2022 18:22",
        latitude: 49.419250,
        longitude: 16.723830,
    },
]
</script>