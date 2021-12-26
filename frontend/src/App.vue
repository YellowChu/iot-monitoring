<template>
    <div class="demo">
        <transition-group tag="div" class="div-slider" :name="back? 'slideback' : 'slide'">
            <div v-if="currentIndex === 0" key="1" class="nav-bar-container">
                    <router-link to="/home_sensor" class="left-nav" @click="next()">
                        <div class="left-container">
                            <img class="icon" src="@/assets/sensor-icon.svg">
                            <h1 class="icon_text">Home Sensor</h1>
                        </div>      
                    </router-link>
                    <router-link to="/mailbox_notifier" class="right-nav" @click="next()">
                        <div class="right-container">
                            <img class="icon" src="@/assets/mailbox-icon.svg">
                            <h1>Mailbox Notifier</h1>
                        </div>
                    </router-link>
            </div>
            <div v-if="currentIndex === 1" key="2" class="nav-bar-container">
                <div class="view">
                    <router-link to="/" @click="prev()">
                        <button>Back</button>
                    </router-link>
                    <router-view></router-view>
                </div>
            </div>
        </transition-group>
    </div>
</template>

<style>
.nav-bar-container {
    position: absolute;
    display: flex;
    height: inherit;
    width: inherit;
}

.view {
    background: #19507e;
    width:inherit;
}

.slide-leave-active,
.slide-enter-active {
    transition: 1s;
}
.slide-enter-from {
    transform: translate(100%, 0);
}
.slide-leave-to {
    transform: translate(-100%, 0);
}

.slideback-leave-active,
.slideback-enter-active {
    transition: 1s;
}
.slideback-enter-from {
    transform: translate(-100%, 0);
}
.slideback-leave-to {
    transform: translate(100%, 0);
}

.div-slider{
    overflow: hidden;
    height: 100%;
    width: 100%;
}

.slid-enter-active,
.slid-leave-active {
    transition: 0.5s;
}

.slid-leave-to {
    transform: translateX(100%);
}
.slid-enter-from {
    transform: translateX(-100%);
}

html, body {
    margin: 0;
}

.icon {
    width: 13rem;
    fill: red;
}

.left-nav {
    height: 100%;
    width: 50%;
    background: rgb(53, 34, 34);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: PLS;
}
.left-nav:hover {
    background-color: rgb(82, 19, 19);
    cursor: pointer;
}

.right-nav { 
    height: 100%;
    flex-grow: 1;
    background: #2d373f;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: PLS;
}
.right-nav:hover {
    background: #19507e;
    cursor: pointer;
}

@font-face {
    font-family: "PLS";
    src: url("./assets/Viga-Regular.ttf") format("truetype");
}
</style>


<script>
export default {
    name: "App",
    data() {
        return {
            picked: false,
            back: false,
            currentIndex: 0
        }
    },
    methods: {
        next(){
            this.back = false;
            this.currentIndex++;
        },
        prev(){
            this.back = true;
            this.currentIndex--;
        }
    }
}
</script>