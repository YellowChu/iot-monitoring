import { createRouter, createWebHistory } from "vue-router";

import room_sensor_view from "@/views/room_sensor_view.vue"
import about_view from "@/views/about_view.vue"

import room_sensor_dashboard from "@/components/room_sensor/room_sensor_dashboard.vue"
import room_sensor_data from "@/components/room_sensor/room_sensor_data.vue"
import room_sensor_downlink from "@/components/room_sensor/room_sensor_downlink.vue"
import room_sensor_settings from "@/components/room_sensor/room_sensor_settings.vue"

import user_login from "@/components/user/user_login.vue"

const routes = [
    {
        path: "/room_sensor",
        alias: "/",
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
        path: "/about",
        name: "about_view",
        component: about_view,
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
