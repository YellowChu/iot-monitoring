import { createRouter, createWebHistory } from "vue-router";

import home_sensor_list from "@/components/home_sensor_components/home_sensor_list.vue"
import home_sensor_about from "@/components/home_sensor_components/home_sensor_about.vue"
import home_sensor_data from "@/components/home_sensor_components/home_sensor_data.vue"
import home_sensor_command from "@/components/home_sensor_components/home_sensor_command.vue"
import home_sensor_settings from "@/components/home_sensor_components/home_sensor_settings.vue"

const routes = [
    {
        path: "/list",
        alias: "/",
        name: "home_sensor_list",
        component: home_sensor_list,
        children: [
            {
                path: ":device_id/data",
                name: "home_sensor_data",
                component: home_sensor_data
            },
            {
                path: ":device_id/command",
                name: "home_sensor_command",
                component: home_sensor_command
            },
            {
                path: ":device_id/settings",
                name: "home_sensor_settings",
                component: home_sensor_settings
            },
        ]
    },
    {
        path: "/about",
        name: "home_sensor_about",
        component: home_sensor_about,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
