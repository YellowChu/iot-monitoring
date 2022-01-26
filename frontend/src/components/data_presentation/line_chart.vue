<template>
    <div class="example">
        <h4>Composition API Line chart</h4>
        <apexcharts
            width="1200"
            height="600"
            type="line"
            :options="chartOptions"
            :series="series.yaxis"
        />
    </div>
</template>

<script setup>
import { defineProps, reactive, toRefs } from "vue";
import apexcharts from "vue3-apexcharts";

const props = defineProps({
    xaxis: Array,
    yaxis: Array,
})

const { xaxis, yaxis } = toRefs(props);

console.log(props.xaxis)

// const xaxis = reactive([
//     "Tue, 21 Dec 2021 11:17:48 GMT",
//     "Tue, 21 Dec 2021 12:09:27 GMT",
//     "Tue, 21 Dec 2021 16:11:59 GMT",
// ])
// const yaxis = reactive([30, 50, 49])

const chartOptions = reactive({
    xaxis: {
        type: "datetime",
        categories: xaxis,
    },
});
const series = reactive({
    yaxis: [{
        name: "series-1",
        data: yaxis
    }]
});
</script>
