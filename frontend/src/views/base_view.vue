<template>
<div class="room_sensor_view">
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark p-0" style="height: 5rem;">
        <a class="navbar-brand">
            <!-- <img class="icon me-4" src="@/assets/logo.png" style="width: 230;"> -->
            <strong>IoT Gardienne</strong>
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
                <li class="nav-item">
                    <button type="button" class="btn btn-light btn-sm">
                        <router-link :to="{ name: 'user_login' }" class="nav-link text-dark"><font-awesome-icon :icon="['fas', 'sign-in-alt']"/> Login</router-link>
                    </button>
                </li>
            </ul>
        </div>
        <div v-else class="user-nav me-auto">
            <ul class="user-nav navbar-nav">
                <li class="nav-item text-white" style="cursor: pointer;">
                    <button type="button" class="btn btn-secondary" @click="logout()">
                        <a><font-awesome-icon :icon="['fas', 'sign-out-alt']"/> Logout</a>
                    </button>
                </li>
            </ul>
        </div>
    </nav>

    <div class="router_view_container" style="margin-top: 7rem;">
        <router-view></router-view>
    </div>
</div>
</template>

<style scoped>
.navbar {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
}
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
    background: rgb(206, 206, 206);
    border-radius: 0.25rem;
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
