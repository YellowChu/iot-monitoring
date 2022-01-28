<template>
    <div class="line_chart">
        <apexcharts
            type="line"
            :options="data.chart_options"
            :series="data.temperature_series.yaxis"
        />
    </div>
</template>

<script setup>
import { defineProps, reactive, watch } from "vue";
import apexcharts from "vue3-apexcharts";


// props and data
const props = defineProps({
    xaxis: Array,
    yaxis: Array,
    color: String,
})

console.log(props.color, props.xaxis, props.yaxis);

let data = reactive({
    chart_options: {
        chart: {
            toolbar: {
                show: true,
                tools:{
                    download: false,
                }
            }
        },
        colors: [props.color],
        markers: {
            size: [4, 6]
        },  
        xaxis: {
            type: "datetime",
            categories: props.xaxis,
        },
        yaxis: {
            labels: {
                formatter: function (val) {
                    return val.toFixed(2)
                }
            },
            crosshairs: {
                show: true,
            },
        }
    },
    temperature_series: {
        yaxis: [{
            name: "temperature",
            data: props.yaxis,
        }]
    }
})


// life cycle hooks and watchers
watch(() => props.xaxis, () => {
    data.chart_options = {
        xaxis: {
            categories: props.xaxis,
        },
    };
})
watch(() => props.yaxis, () => {
    data.temperature_series = {
        yaxis: [{
            data: props.yaxis,
        }]
    };
})
</script>
