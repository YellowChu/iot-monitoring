<template>
    <div class="demo">
        <div class="main-container">
            <transition name="fade">
                <div v-if="!picked" class="main-menu">
                    <router-link to="/home_sensor" class="left-nav" :class="menu" @click="change_menu('left')">
                        <div>
                            <img class="icon" src="@/assets/sensor-icon.svg">
                            <h1 class="icon_text">Home Sensor</h1>
                        </div>      
                    </router-link>
                    <router-link to="/mailbox_notifier" class="right-nav" :class="menu" @click="change_menu('right')">
                        <div>
                            <img class="icon" src="@/assets/mailbox-icon.svg">
                            <h1>Mailbox Notifier</h1>
                        </div>
                    </router-link>
                </div>
            </transition>
            <transition name="fade">
                <div v-if="picked" class="view">
                    <div class="base-view">
                        <router-link to="/">
                            <button @click="change_menu('default')">Back</button>
                        </router-link>
                        <router-view></router-view>
                    </div>
                </div>
            </transition>
        </div>
    </div>
</template>

<style>
html, body {
    margin: 0;
}
@font-face {
    font-family: "icon-font";
    src: url("./assets/Viga-Regular.ttf") format("truetype");
}

.main-menu {
    position: absolute;
    display: flex;
    height: inherit;
    width: inherit;
}
.main-container{
    overflow: hidden;
    height: 100%;
    width: 100%;
}
.icon {
    width: 13rem;
    fill: red;
}
.view {
    background: #e7e9eb;
    width: inherit;
    height: inherit;
}
.base-view {
    display: inline-block;
    margin: 1rem;
    padding: 2rem;
    background: #19507e;
}

.left-nav {
    height: 100%;
    width: 50%;
    background: rgb(53, 34, 34);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: icon-font;
}
.left-nav:hover {
    background-color: rgb(82, 19, 19);
    cursor: pointer;
}
.left-nav.default {
    overflow: hidden;
    transition: max-height 0.3s ease-out;
    width: 50%;
    transition-property: width;
}
.left-nav.left {
    transition: max-height 0.3s ease-out;
    width: 100%;
    transition-property: width;
}
.left-nav.right {
    overflow: hidden;
    transition: max-height 0.3s ease-out;
    width: 0%;
    transition-property: width;
}

.right-nav { 
    height: 100%;
    flex-grow: 1;
    background: #2d373f;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: icon-font;
}
.right-nav:hover {
    background: #19507e;
    cursor: pointer;
}
.rigth-nav.default {
    transition: max-height 0.3s ease-out;
    width: 100%;
    transition-property: width;
}
.right-nav.left {
    overflow: hidden;
    transition: max-height 0.3s ease-out;
    width: 0%;
    transition-property: width;
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>


<script>
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

export default {
    name: "App",
    data() {
        return {
            picked: false,
            back: false,
            currentIndex: 0,
            menu: "default",
        }
    },
    methods: {
        next (){
            this.back = false;
            this.currentIndex++;
        },
        prev (){
            this.back = true;
            this.currentIndex--;
        },
        async change_menu (str) {
            // sleep is to wait for the animation to finish/start
            if (str == "default") {
                this.picked = false;
                await sleep(500);
                this.menu = str;
            } else {
                this.menu = str;
                await sleep(500);
                this.picked = true;
            }
        },
    }
}
</script>