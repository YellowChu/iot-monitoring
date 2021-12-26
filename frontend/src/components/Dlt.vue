<template>
<div id="demo">
    <button @click="show = !show">
        Toggle
    </button>

    <transition name="fade">
        <p v-if="show">hello</p>
    </transition>
</div>
</template>

<style>
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
export default {
    name: "DltLtr",
    data() {
        return {
            show: true
        }
    }
}
</script>
