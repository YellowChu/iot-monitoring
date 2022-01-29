<template>
<div class="home_sensor_view">
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand">
            <b>IoT Gardienne</b>
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="main-nav collapse navbar-collapse nav justify-content-center" id="navbarNavDropdown">
            <ul class="navbar-nav">
                <li class="nav-item">
                        <router-link :to="{ name: 'home_sensor_list' }" class="nav-link active">Room Sensor</router-link>
                </li>
                <li class="nav-item">
                        <router-link :to="{ name: 'home_sensor_about' }" class="nav-link">About</router-link>
                </li>
            </ul>
        </div>
    </nav>

    <div class="router_view_container">
        <router-view></router-view>
    </div>
</div>
</template>

<style scoped>
.navbar-brand {
    margin-left: 1rem;
}
.main-nav {
    margin-left: -10rem;
}
.nav-item {
    margin: 0rem 2rem 0rem 2rem;
}
.router-link-active {
    font-weight: bold;
}
.router_view_container {
    margin-top: 5rem;
}
</style>

<script>

</script>
