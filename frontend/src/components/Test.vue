<template>
    <div class="Test">
        <h1>Room sensors</h1>
        <div v-for="room_sensor in room_sensors" :key="room_sensor.pk">
            <span @click="show_data(room_sensor.pk)">{{ room_sensor.device_id }}</span>
        </div>

        <ul v-if="sensor_data.length">
            <li v-for="(data, idx) in sensor_data" :key="data.time + idx">{{ data.time }}</li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "Test",
    data() {
        return {
            room_sensors: [],
            sensor_data: [],
        }
    },
    mounted() {
        let vm = this;
        axios
            .get("/api/sensor/room_sensor_list/")
            .then(response => {
                console.log(response);
                vm.room_sensors = response.data.room_sensors;
            })
    },
    methods: {
        async show_data(id) {
            let vm = this;
            axios
                .get("/api/sensor/room_sensor_data/" + id +"/")
                .then(response => {
                    console.log(response);
                    vm.sensor_data = response.data.sensor_data_list;
                    console.log(vm.sensor_data);
                })
            
        }
    }
}
</script>
