<template>
<div class="row align-items-center justify-content-center" style="margin-top: 25rem;">
    <div class="login-card card" style="width: 25rem;">
        <div class="card-body" style="text-align: left;">
            <div v-if="form_err_msg" class="alert alert-danger" role="alert">
                {{ form_err_msg }}
            </div>
            <form @submit.prevent="login_submit()">
                <div class="input-group mb-3">
                    <div class="input-group-prepend">
                        <span class="input-group-text" style="height: 3rem;"><font-awesome-icon :icon="['fas', 'user']"/></span>
                    </div>
                    <input type="text" class="form-control" placeholder="Username" v-model="username">
                </div>
                <div class="input-group mb-3">
                    <div class="input-group-prepend">
                        <span class="input-group-text" style="height: 3rem;"><font-awesome-icon :icon="['fas', 'lock']"/></span>
                    </div>
                    <input type="password" class="form-control" placeholder="Password" v-model="password">
                </div>

                <div class="d-flex flex-row-reverse bd-highlight">
                    <button type="submit" class="btn btn-primary">Login</button>
                </div>
            </form>
        </div>
    </div>
</div>
</template>

<style>
.login-card {
    box-shadow: 0 10px 20px rgba(0,0,0,.12), 0 4px 8px rgba(0,0,0,.06);
}
</style>

<script setup>
import axios from "axios";

import { inject, ref } from "vue";
import router from "@/router";


let username = ref("");
let password = ref("");
let form_err_msg = ref("");

const user_state_set_token = inject("set_token");


function login_submit() {
    let request_data = {
        username: username.value,
        password: password.value,
    }

    axios
        .post("/auth-api/token/login", request_data)
        .then((resp) => {
            const token = resp.data.auth_token;
            user_state_set_token(token);

            axios.defaults.headers.common["Authorization"] = "Token " + token;
            localStorage.setItem("token", token);

            router.go(-1);
        })
        .catch((err) => {
            if (err.response.status == 400) {
                form_err_msg.value = "Wrong username or password."
            } else {
                alert(err);
            }
        })
}
</script>