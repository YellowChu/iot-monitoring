<template>
<footer class="fixed-bottom">
    <transition name="fade">
        <div v-if="props.bool_trigger">
            <div class="waves-bg-1">
                <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
                    <path d="M0,0V5.63C149.93,59,314.09,71.32,475.83,42.57c43-7.64,84.23-20.12,127.61-26.46,59-8.63,112.48,12.24,165.56,35.4C827.93,77.22,886,95.24,951.2,90c86.53-7,172.46-45.71,248.8-84.81V0Z" class="shape-fill"></path>
                    <defs>
                        <linearGradient id="wave-gradient-1">
                            <stop offset="5%" stop-color="#324d76" />
                            <stop offset="95%" stop-color="#537fc1" />
                        </linearGradient>
                    </defs>
                </svg>
            </div>
            <div class="waves-bg-2">
                <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
                    <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
                    <defs>
                        <linearGradient id="wave-gradient-2">
                            <stop offset="5%" stop-color="#791e6a80" />
                            <stop offset="95%" stop-color="#A2268E" />
                        </linearGradient>
                    </defs>
                </svg>
            </div>
        </div>
    </transition>
</footer>
</template>

<style>
.waves-bg-1 {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    overflow: hidden;
    line-height: 0;
    transform: rotate(180deg);
}

.waves-bg-1 svg {
    position: relative;
    display: block;
    width: calc(126% + 1.3px);
    height: 332px;
}

.waves-bg-1 .shape-fill {
    fill: url("#wave-gradient-1");
}

.waves-bg-2 {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    overflow: hidden;
    line-height: 0;
    transform: rotate(180deg);
}

.waves-bg-2 svg {
    position: relative;
    display: block;
    width: calc(137% + 1.3px);
    height: 186px;
}

.waves-bg-2 .shape-fill {
    fill: url("#wave-gradient-2");
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


<script setup>
import { defineProps } from "vue";


let props = defineProps({
    bool_trigger: Boolean,
})

console.log(props.bool_trigger);
</script>