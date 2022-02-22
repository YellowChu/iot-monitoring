<template>
<nav class="navbar fixed-top navbar-expand-lg navbar-dark p-4">
    <div class="navbar-brand ps-5">
        <router-link :to="{ name: 'homepage_view' }" class="nav-link fw-bold text-white" style="font-size: 32px">IoT Gardienne</router-link>
    </div>

    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <li class="nav-item main-nav-item">
                    <router-link :to="{ name: 'room_sensor_view' }" class="nav-link fw-bold text-white">Room Sensor</router-link>
            </li>
            <li class="nav-item main-nav-item">
                    <router-link :to="{ name: 'mailbox_notifier_view' }" class="nav-link fw-bold text-white">Mailbox Notifier</router-link>
            </li>
            <li class="nav-item main-nav-item">
                    <router-link :to="{ name: 'car_tracker_view' }" class="nav-link fw-bold text-white">Car Tracker</router-link>
            </li>

            <li v-if="!user_state.is_authenticated" class="nav-item">
                <router-link :to="{ name: 'user_login' }" class="nav-link login-link text-white fw-bold">Sign In</router-link>
            </li>
            <li v-else class="nav-item" style="cursor: pointer;">
                <button type="button" class="btn btn-secondary fw-bold" @click="logout()">
                    <a>Sign Out</a>
                </button>
            </li>
        </ul>
    </div>
</nav>
</template>

<style scoped>
.navbar {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
    background: linear-gradient(#e66465, #9198e5);
}
.nav-item {
    margin: 0.5rem 2rem 0.5rem 2rem;
}
.router-link-active {
    border-bottom: 4px solid rgb(255, 255, 255);
}
.nav-link:hover:not(.active) {
    transition: 0.3s;
    border-bottom: 2px solid rgb(255, 255, 255);
}
.login-link {
    border: 3px solid rgb(255, 255, 255);
    border-radius: 4px;
}
.login-link:hover {
    background: gray;
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
