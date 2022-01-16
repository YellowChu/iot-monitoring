import { createRouter, createWebHistory } from "vue-router";
import LandingPage from "@/views/LandingPage.vue"
import HomeSensor from "@/views/HomeSensor.vue";
import MailboxNotifier from "@/views/MailboxNotifier.vue"

import DltLtr from "@/components/Dlt.vue";
import Test from "@/components/Test.vue";

const routes = [
    {
        path: "/",
        name: "LandingPage",
        component: LandingPage,
    },
    {
        path: "/home_sensor",
        name: "HomeSensor",
        component: HomeSensor,
        children: [
            {
                path: "dlt_ltr",
                name: "dlt_ltr",
                component: DltLtr,
            },
            {
                path: "test",
                name: "Test",
                component: Test,
            },
        ]
    },
    {
        path: "/mailbox_notifier",
        name: "MailboxNotifier",
        component: MailboxNotifier,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
