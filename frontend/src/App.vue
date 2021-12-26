<template>
    <transition name="slide">
        <div v-if="!picked" class="landing-page-nav">
            <router-link to="/home_sensor" class="left-nav" @click="picked = true">
                <div class="left-container">
                    <img class="icon" src="@/assets/sensor-icon.svg">
                    <h1 class="icon_text">Home Sensor</h1>
                </div>      
            </router-link>
            <router-link to="/mailbox_notifier" class="right-nav" @click="picked = true">
                <div class="right-container">
                    <img class="icon" src="@/assets/mailbox-icon.svg">
                    <h1>Mailbox Notifier</h1>
                </div>
            </router-link>
        </div>
    </transition>

    <div v-if="picked" class="landing-page-view">
        <button @click="picked = false">Back</button>
        <router-view></router-view>
    </div>
    <div id="demo">
        <h3>div slider</h3>
        <transition-group tag="div" class="div-slider" :name="back? 'slideback' : 'slide'">
            <div v-if="currentIndex === 0" key="1">
                <div class="card">
                    DIV 1
                </div>
            </div>
            <div v-if="currentIndex === 1" key="2" >
                <div class="card">
                    DIV 2
                </div>
            </div>
            <div v-if="currentIndex === 2" key="3" >
                <div class="card">
                    DIV 3
                </div>
            </div>
        </transition-group>
        <button @click="prev()" >prev</button>
        <button @click="next()">next</button>
    </div>
</template>

<style>
.demo {
  overflow: hidden;
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
  position: relative;
  height: 100px;
  width: 90%;
}

.div-slider .card {
  position: absolute;
  height: 100px;
  width: 90%;
  background-color: #60adff;
}


.landing-page-view {
    background: red;
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
.landing-page-nav { 
    display: flex;
    height: 50%;
}

.left-nav {
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