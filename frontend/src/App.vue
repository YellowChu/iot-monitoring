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
    font-family: Helvetica;
    overflow: hidden;
}
</style>

<script setup>
import axios from "axios";

import base_view from "@/views/base_view.vue"
import { provide, reactive, readonly } from "vue";

// user auth storage
let user_state = reactive({
    token: "",
    is_authenticated: false,
})


initialize_user();
const token = user_state.token;

if (token) {
    axios.defaults.headers.common["Authorization"] = "Token " + token;
    validate_token();
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

function validate_token() {
    var request = new XMLHttpRequest();
    request.open("GET", "/token-auth/", false);
    request.setRequestHeader("Authorization", "Token " + token);
    request.send(null);

    if (request.status === 200) {
        if (JSON.parse(request.responseText).status != "ok") {
            remove_token();
        }
    }
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