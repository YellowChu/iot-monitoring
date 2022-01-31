<template>
<div class="room_sensor_view">
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand">
            <b>IoT Gardienne</b>
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="main-nav collapse navbar-collapse nav justify-content-center" id="navbarNavDropdown">
            <ul class="navbar-nav">
                <li class="nav-item text-white">
                        <router-link :to="{ name: 'room_sensor_view' }" class="nav-link active">Room Sensor</router-link>
                </li>
                <li class="nav-item text-white">
                        <router-link :to="{ name: 'about_view' }" class="nav-link">About</router-link>
                </li>
            </ul>
        </div>


        <div v-if="!user_state.is_authenticated" class="user-nav me-auto">
            <ul class="navbar-nav">
                <li class="nav-item text-white">
                    <router-link :to="{ name: 'user_login' }" class="nav-link"><font-awesome-icon :icon="['fas', 'sign-in-alt']"/> Login</router-link>
                </li>
            </ul>
        </div>
        <div v-else class="user-nav me-auto">
            <ul class="navbar-nav">
                <li class="nav-item text-white" style="cursor: pointer;">
                    <a @click="logout()"><font-awesome-icon :icon="['fas', 'sign-out-alt']"/> Logout</a>
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
    background: grey;
    border-radius: 0.5rem;
}
.router_view_container {
    margin-top: 5rem;
}

.nav-item {
    color: white;
}
.nav-item:hover {
    font-weight: bold;
}
</style>

<script setup>
import axios from "axios";

import { inject } from "vue";
import router from "@/router";


const user_state = inject("user_state");
const remove_token = inject("remove_token");


function logout() {
    axios
        .post("/auth-api/token/logout/", user_state.token)
        .then(() => {
            remove_token();
            router.push({ name: 'user_login' });
        })
}
</script>
