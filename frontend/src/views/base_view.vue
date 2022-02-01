<template>
<div class="room_sensor_view">
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark p-4">
        <div class="navbr-brand ps-5">
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

    <div class="router_view_container" style="margin-top: 9rem; margin-bottom: 20rem;">
        <router-view></router-view>
    </div>

    <footer class="fixed-bottom">
        <div class="waves-bg-1">
            <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
                <path d="M0,0V5.63C149.93,59,314.09,71.32,475.83,42.57c43-7.64,84.23-20.12,127.61-26.46,59-8.63,112.48,12.24,165.56,35.4C827.93,77.22,886,95.24,951.2,90c86.53-7,172.46-45.71,248.8-84.81V0Z" class="shape-fill"></path>
                <defs>
                    <linearGradient id="wave-gradient-1">
                        <stop offset="5%" stop-color="#324d76" />
                        <stop offset="95%" stop-color="#537fc1" />
                    </linearGradient>
                </defs>
            </svg>
        </div>
        <div class="waves-bg-2">
            <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
                <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
                <defs>
                    <linearGradient id="wave-gradient-2">
                        <stop offset="5%" stop-color="#791e6a80" />
                        <stop offset="95%" stop-color="#A2268E" />
                    </linearGradient>
                </defs>
            </svg>
        </div>
    </footer>
</div>
</template>

<style scoped>
.waves-bg-1 {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    overflow: hidden;
    line-height: 0;
    transform: rotate(180deg);
}

.waves-bg-1 svg {
    position: relative;
    display: block;
    width: calc(126% + 1.3px);
    height: 332px;
}

.waves-bg-1 .shape-fill {
    fill: url("#wave-gradient-1");
}

.waves-bg-2 {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    overflow: hidden;
    line-height: 0;
    transform: rotate(180deg);
}

.waves-bg-2 svg {
    position: relative;
    display: block;
    width: calc(137% + 1.3px);
    height: 186px;
}

.waves-bg-2 .shape-fill {
    fill: url("#wave-gradient-2");
}

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
