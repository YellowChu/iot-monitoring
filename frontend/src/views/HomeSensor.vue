<template>
    <div>
        <router-link to="/home_sensor/dlt_ltr">Delete Later</router-link>
        <router-link to="/home_sensor/test">Test</router-link>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    methods: {
        back_to_main_menu() {
            console.log("..");
            this.$parent.change_menu("default");
        }
    }
}
</script>
