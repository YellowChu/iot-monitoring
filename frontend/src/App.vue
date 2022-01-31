<template>
<div class="base">
    <base_view></base_view>
</div>
</template>

<style>
::-webkit-scrollbar {
    width: 0.4rem;
}

::-webkit-scrollbar-track {
    background: #1e1e24;
}

::-webkit-scrollbar-thumb {
    background: #b2b2bc;
}

@font-face {
    font-family: "main_font";
    src: url("./assets/Viga-Regular.ttf") format("truetype");
}

.base {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-family: Helvetica;
    color: #2c3e50;
}
</style>

<script setup>
import axios from "axios";

import base_view from "@/views/base_view.vue"
import { provide, reactive, readonly } from "vue";

// user auth storage
// TODO: move somewhere else
// TODO: when opening site check if token is working if not remove it
let user_state = reactive({
    token: "",
    is_authenticated: false,
})


initialize_user();
const token = user_state.token;

if (token) {
    axios.defaults.headers.common["Authorization"] = "Token " + token;
} else {
    axios.defaults.headers.common["Authorization"] = "";
}

function initialize_user() {
    if (localStorage.getItem("token")) {
        user_state.token = localStorage.getItem("token");
        user_state.is_authenticated = true;
    } else {
        user_state.token = "";
        user_state.is_authenticated = false;
    }
}

function set_token(token) {
    user_state.token = token;
    user_state.is_authenticated = true;
}

function remove_token() {
    user_state.token = "";
    user_state.is_authenticated = false;

    localStorage.removeItem("token");
    axios.defaults.headers.common["Authorization"] = "";
}

provide("user_state", readonly(user_state));
provide("initialize_user", initialize_user);
provide("set_token", set_token);
provide("remove_token", remove_token);
</script>