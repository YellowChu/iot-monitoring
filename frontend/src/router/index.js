import { createRouter, createWebHistory } from "vue-router";

import homepage_view from "@/views/homepage_view.vue";
import user_login from "@/components/user/user_login.vue";

import room_sensor_view from "@/views/room_sensor_view.vue";
import room_sensor_dashboard from "@/components/room_sensor/room_sensor_dashboard.vue";
import room_sensor_data from "@/components/room_sensor/room_sensor_data.vue";
import room_sensor_downlink from "@/components/room_sensor/room_sensor_downlink.vue";
import room_sensor_settings from "@/components/room_sensor/room_sensor_settings.vue";

import mailbox_notifier_view from "@/views/mailbox_notifier_view.vue";
import mailbox_notifier_mail from "@/components/mailbox_notifier/mailbox_notifier_mail.vue";
import mailbox_notifier_settings from "@/components/mailbox_notifier/mailbox_notifier_settings.vue";

import car_tracker_view from "@/views/car_tracker_view.vue";
import car_tracker_location from "@/components/car_tracker/car_tracker_location.vue";
import car_tracker_settings from "@/components/car_tracker/car_tracker_settings.vue";


const routes = [
    {
        path: "/",
        name: "homepage_view",
        component: homepage_view,
    },
    {
        path: "/room_sensor",
        name: "room_sensor_view",
        component: room_sensor_view,
        children: [
            {
                path: ":device_id/dashboard",
                alias: ":device_id/",
                name: "room_sensor_dashboard",
                component: room_sensor_dashboard
            },
            {
                path: ":device_id/data",
                name: "room_sensor_data",
                component: room_sensor_data
            },
            {
                path: ":device_id/downlink",
                name: "room_sensor_downlink",
                component: room_sensor_downlink
            },
            {
                path: ":device_id/settings",
                name: "room_sensor_settings",
                component: room_sensor_settings
            },
        ]
    },
    {
        path: "/mailbox_notifier",
        name: "mailbox_notifier_view",
        component: mailbox_notifier_view,
        children: [
            {
                path: ":device_id/mail",
                alias: ":device_id/",
                name: "mailbox_notifier_mail",
                component: mailbox_notifier_mail
            },
            {
                path: ":device_id/settings",
                name: "mailbox_notifier_settings",
                component: mailbox_notifier_settings
            },
        ]
    },
    {
        path: "/car_tracker",
        name: "car_tracker_view",
        component: car_tracker_view,
        children: [
            {
                path: ":device_id/location",
                alias: ":device_id/",
                name: "car_tracker_location",
                component: car_tracker_location
            },
            {
                path: ":device_id/settings",
                name: "car_tracker_settings",
                component: car_tracker_settings
            },
        ]
    },
    {
        path: "/login",
        name: "user_login",
        component: user_login,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
