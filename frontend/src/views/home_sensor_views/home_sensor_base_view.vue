<template>
<div class="home_sensor_view">
    <h1>Home Sensor</h1>
    <div>
        <router-link :to="{ name: 'home_sensor_list' }">| List |</router-link>
        <router-link :to="{ name: 'home_sensor_about' }">| About |</router-link>
    </div>
    <div>
        <router-view></router-view>
    </div>
</div>
</template>

<script>

</script>
