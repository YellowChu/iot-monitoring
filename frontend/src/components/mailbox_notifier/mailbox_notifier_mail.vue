<template>
<div class="container-fluid">
    <div class="row mt-5 mb-5 d-flex justify-content-center align-items-center">
        <h2 class="fw-bold justify-content-center" style="color: #074879;">Mailbox state</h2>
    </div>

    <div v-if="err_msg" class="alert alert-danger" role="alert">
        {{ err_msg }}
    </div>

    <div class="row mt-3" style="text-align: left;">

        <div class="col-9 mb-4">
            <div class="card border-left-primary shadow h-100 py-2 w-50" :class="props.number_of_mails > 0 ? 'is-mail' : 'no-mail'">
                <div class="card-body">
                    <h5 class="card-title text-dark"><b>Number of Mails</b></h5>
                    <div class="row">
                        <div class="col">
                            <p class="fs-2">{{ props.number_of_mails }}</p>
                        </div>
                        <div class="col pe-3 ms-5 text-muted">
                            <font-awesome-icon  v-if="props.number_of_mails > 0" :icon="['fas', 'envelope-open']" size="3x"/>
                            <font-awesome-icon  v-else :icon="['fas', 'envelope']" size="3x"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    
        <div class="col-3 mb-4">
            <div
                v-if="user_state.is_authenticated"
                class="card-mails-read card border-left-primary shadow h-100 py-2 d-flex justify-content-center align-items-center"
                @mouseover="hover = true"
                @mouseleave="hover = false"
                @click="clear_mailbox()"
            >
                <div class="card-body">
                    <h5 class="card-title"><b>Clear mailbox</b></h5>
                    <div class="row">
                        <div class="col d-flex justify-content-center align-items-center">
                            <font-awesome-icon v-if="hover" :icon="['fas', 'folder-open']" size="3x"/>
                            <font-awesome-icon v-else :icon="['fas', 'folder']" size="3x"/>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else class="card border-left-primary shadow h-100 py-2 d-flex justify-content-center align-items-center">
                <div class="card-body">
                    <h5 class="card-title"><b>Clear mailbox</b></h5>
                    <unlogged_warning/>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<style scoped>
.is-mail {
    border-left: 8px solid rgba(23, 86, 2, 0.749);
}

.no-mail {
    border-left: 8px solid rgb(28, 28, 28);;
}

.card-mails-read:hover {
    color: #5b8698;
    cursor: pointer;
    transform: scale(1.05);
    box-shadow: 0 10px 20px rgba(0,0,0,.12), 0 4px 8px rgba(0,0,0,.06);
}
</style>

<script setup>
import axios from "axios";

import { defineProps, inject, ref } from "vue";
import { useRoute } from "vue-router";

import unlogged_warning from "@/components/user/unlogged_warning.vue";


const props = defineProps({
    number_of_mails: Number,
})

let hover = ref(false);
let err_msg = ref("");

const update_mailbox_notifier = inject("update_mailbox_notifier");
const user_state = inject("user_state");
const route = useRoute();


function clear_mailbox() {
    if (props.number_of_mails > 0) {
        axios
            .get("/sensor/clear_mailbox/" + route.params.device_id + "/")
            .then((resp) => {
                if (resp.data.status == "ok") {
                    update_mailbox_notifier();
                }
            })
            .catch((err) => {
                alert(err);
            })
    } else {
        err_msg.value = "Cannot clear empty mailbox."
    }
}
</script>