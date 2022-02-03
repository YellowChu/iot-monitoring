
import axios from "axios";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import FontAwesomeIcon from "@/utilities/fontawesome_icons.js";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";


axios.defaults.baseURL = (window.location.protocol === "https:" ? "https://iot-monitored.herokuapp.com" : "http://localhost:8000")

createApp(App)
    .component("font-awesome-icon", FontAwesomeIcon)
    .use(router)
    .mount("#app");
