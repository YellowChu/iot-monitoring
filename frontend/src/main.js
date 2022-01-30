import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import axios from "axios";

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

import { library } from "@fortawesome/fontawesome-svg-core";
import { faUser, faLock } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";


axios.defaults.baseURL = (window.location.protocol === "https:" ? "https://iot-monitored.herokuapp.com" : "http://localhost:8000")

library.add(faUser);
library.add(faLock);

createApp(App).use(router).component("font-awesome-icon", FontAwesomeIcon).mount("#app");
