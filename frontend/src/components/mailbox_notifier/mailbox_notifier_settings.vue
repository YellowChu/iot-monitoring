<template>
<div class="container-fluid">
    <div class="row mt-5 mb-5 d-flex justify-content-center align-items-center">
        <h2 class="fw-bold justify-content-center" style="color: #074879;">Settings</h2>
    </div>
    <div class="row">
        <form class="sensor-form" @submit.prevent>
            <div class="mb-3">
                <label class="form-label">Name</label>
                <input type="text" class="form-control" v-model="name">
            </div>
            <div class="mb-3">
                <label class="form-label">Description</label>
                <textarea class="form-control" rows="3" v-model="description"></textarea>
            </div>
            <div class="mb-3">
                <label class="form-check-label" for="notify_checkbox">Notify</label>
                <input class="form-check-input ms-2" type="checkbox" id="notify_checkbox" v-model="should_notify">
            </div>
            <div class="mb-3">
                <label class="form-label">Emails</label>
                <textarea class="form-control" rows="3" v-model="emails"></textarea>
            </div>

            <div class="mb-3">
                <div v-if="user_state.is_authenticated" class="d-flex flex-row-reverse bd-highlight mb-3">
                    <div class="btn-group" role="group">
                        <button type="submit" class="btn btn-success" :class="{ disabled: !data.enable_save }" @click="save_changes()">Save Changes</button>
                        <button class="btn btn-danger" @click="data.show_delete_modal=true">Delete Sensor</button>
                    </div>
                </div>
                <div v-else>
                    <unlogged_warning/>
                </div>
            </div>
        </form>
    </div>

    <modal_window 
        :show_modal="data.show_delete_modal"
        @close="data.show_delete_modal=false; data.form_err_msg='';"
    >
        <template v-slot:header>
            <h4 class="modal-title" id="myModalLabel">Do you really want to delete this sensor?</h4>
        </template>

        <template v-slot:body>
            <div v-if="data.form_err_msg" class="alert alert-danger" role="alert">
                {{ data.form_err_msg }}
            </div>
            <div class="mb-3">
                <label class="form-label"><b>Device name:</b> {{ props.sensor_name }}</label>
            </div>
        </template>

        <template v-slot:footer>
            <button class="btn btn-danger" @click="delete_room_sensor()">Delete</button>
        </template>
    </modal_window>
</div>
</template>

<style>
.home-sensor-command {
    margin-top: 1rem;
}
.sensor-form {
  text-align: left;

}
</style>

<script setup>
import axios from "axios";

import { defineProps, inject, reactive, ref, watch } from "vue";
import router from "@/router";
import { useRoute } from "vue-router";

import modal_window from "@/components/ui/modal_window.vue";
import unlogged_warning from "@/components/user/unlogged_warning.vue";


const props = defineProps({
    sensor_name: String,
    sensor_description: String,
    mn_should_notify: Boolean,
    mn_emails: Array,
})

let name = ref(props.sensor_name);
let description = ref(props.sensor_description);
let should_notify = ref(props.mn_should_notify);
let emails = ref(props.mn_emails.join("\r\n"));

let data = reactive({
    // patch sensor data
    enable_save: false,
    // delete sensor data
    form_err_msg: "",
    show_delete_modal: false,
})

const update_mailbox_notifier = inject("update_mailbox_notifier");
const user_state = inject("user_state");
const route = useRoute()


watch([name, description, should_notify, emails], () => {
    data.enable_save = true;
})


function save_changes() {
    let request_data = {
        device_name: name.value,
        device_description: description.value,
        should_notify: should_notify.value,
        emails: emails.value.split("\n").filter(n => n),
    };
    console.log(request_data);
    axios
        .patch("/api/v1/mailboxnotifier/" + route.params.device_id + "/", request_data)
        .then(() => {
            data.enable_save = false;
            update_mailbox_notifier();
        })
        .catch((err) => {
            alert(err);
        })
}

function delete_room_sensor() {
    axios
        .delete("/api/v1/mailboxnotifier/" + route.params.device_id + "/")
        .then(() => {
            data.show_delete_modal = false;
            update_mailbox_notifier();
            router.push({ name: 'mailbox_notifier_view' });
        })
        .catch((err) => {
            alert(err);
        })
}
</script>