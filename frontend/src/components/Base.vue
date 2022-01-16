<template>
    <div class="base-view">
        <router-link to="/">
            <button @click="back_to_main_menu()">Back</button>
        </router-link>
        <router-view></router-view>
    </div>
</template>

<style>
.base-view {
    display: inline-block;
    margin: 1rem;
    padding: 2rem;
    background: #19507e;
}
</style>

<script>
export default {
    name: "baseView",
    methods: {
        back_to_main_menu() {
            this.$parent.prev();
        }
    }
}
</script>