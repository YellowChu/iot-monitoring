<template>
    <div class="line_chart">
        <apexcharts
            type="donut"
            :options="data.chart_options"
            :series="data.series"
        />
    </div>
</template>

<script setup>
/* eslint-disable */
import { defineProps, reactive, watch } from "vue";
import apexcharts from "vue3-apexcharts";


const props = defineProps({
    labels: Array,
    counts: Array,
})


let data = reactive({
    chart_options: {
        chart: {
            type: 'donut',
        },
        labels: props.labels,
        legend: {
            show: false
        },
    },
    series: props.counts,
})


watch(() => props.counts, () => {
    data.series = props.counts;
})
watch(() => props.labels, () => {
    data.chart_options = {
        labels: props.labels,
    }
})
</script>