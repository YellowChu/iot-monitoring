<template>
<div>
    <section>
        <div class="row align-items-center">
            <div class="col-xl-6 col-md-12" align="center"> 
                <h1 class="fw-bold" style="color: #BB004B; font-size: 64px">IoT Gardienne</h1>
                <h2 class="fw-bold" style="color: #074879; font-size: 32px">Babysit your sensors</h2>
            </div>
            <div class="col-xl-6 col-md-12" align="center">
                <svg
                    id="visual"
                    viewBox="0 0 900 600"
                    width="900"
                    height="600"
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:xlink="http://www.w3.org/1999/xlink"
                    version="1.1"
                >
                    <g transform="translate(424.97215582167075 340.72865571132576)">
                        <path
                            d="M134.7 -134C181.2 -88.2 230.1 -44.1 228.7 -1.4C227.2 41.2 175.5 82.5 129 130.2C82.5 177.8 41.2 231.9 -14.7 246.6C-70.7 261.4 -141.4 236.8 -166.4 189.1C-191.4 141.4 -170.7 70.7 -169.3 1.4C-167.9 -67.9 -185.8 -135.8 -160.8 -181.6C-135.8 -227.4 -67.9 -251.2 -11.9 -239.3C44.1 -227.4 88.2 -179.8 134.7 -134"
                            fill="#537fc1">
                        </path>
                    </g>
                    <g transform="translate(420.6853276220704 320.52504242546365)">
                        <path
                            d="M142.1 -156.4C175.2 -108.9 187.1 -54.4 192.5 5.4C198 65.3 196.9 130.6 163.7 165.7C130.6 200.9 65.3 206 15 191C-35.4 176 -70.7 141 -120.7 105.9C-170.7 70.7 -235.4 35.4 -240.1 -4.7C-244.8 -44.8 -189.6 -89.6 -139.6 -137.1C-89.6 -184.6 -44.8 -234.8 4.8 -239.6C54.4 -244.4 108.9 -203.9 142.1 -156.4"
                            fill="#BB004B"
                        ></path>
                    </g>
                </svg>
            </div>
        </div>
    </section>

    <section class="second">
        <div class="wave">
            <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
                <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
            </svg>
        </div>
        <h2 class="fw-bold mt-5 pt-5" style="color: rgb(255, 255, 255); font-size: 64px">Products</h2>
        <div class="row w-100 mt-5 align-items-center">
            <div class="col-xl-6 col-md-12 mt-md-5" align="center">
                <div class="product-card w-50 p-5" align="left">
                    <h5 style="font-size: 48px; border-bottom: 4px solid rgb(255, 255, 255);"><b>Room Sensor 📡</b></h5>
                    <p class="text-muted mt-5" style="font-weight: 700; font-size: 20px">
                        Monitore your ambient temperature and pressure. I actually don't know what this is for, it might have some gardening uses.
                    </p>
                    <div align="right">
                        <router-link
                            :to="{ name: 'room_sensor_view' }"
                            class="product-icon"
                        >
                            <font-awesome-icon :icon="['fas', 'chevron-circle-right']" size="3x"/>
                        </router-link>
                    </div>
                </div>
            </div>
            <div class="col-xl-6 col-md-12 mt-md-5" align="center"> 
                <div class="product-card w-50 p-5" align="left">
                    <h5 style="font-size: 48px; border-bottom: 4px solid rgb(255, 255, 255);"><b>Mailbox Notifier 📬</b></h5>
                    <p class="text-muted mt-5" style="font-weight: 700; font-size: 20px">
                        Using light sensor placed inside a mailbox, you will get notified when new mail comes. This might be useful when it is finished.
                    </p>
                    <div align="right">
                        <router-link
                            :to="{ name: 'mailbox_notifier_view' }"
                            class="product-icon"
                        >
                            <font-awesome-icon :icon="['fas', 'chevron-circle-right']" size="3x"/>
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="third">
        <div class="tilt">
            <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
                <path d="M1200 120L0 16.48 0 0 1200 0 1200 120z" class="shape-fill"></path>
            </svg>
        </div>
        <div class="row align-items-center mt-5">
            <div class="col mt-5 pt-5" align="center"> 
                <p class="fw-bold" style="color: #ffffff; font-size: 64px">
                    Utilizing LoRa technology
                </p>
                <p class="fw-bold" style="color: #273946; font-size: 64px">
                    and LoRaWAN network.
                </p>
            </div>
        </div>
    </section>

    <!-- <teleport to="body">
        <wave_footer
            :bool_trigger="true"
        ></wave_footer>
    </teleport> -->
</div>
</template>

<style scoped>
section {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 400px;
    padding-top: 10rem;
    padding-bottom: 10rem;
}
.product-icon {
    color: white;
}
.product-icon:hover {
    transition: 0.2s ease;
    color: #8a5b98;
}

.product-card {
    border: 4px solid #f5f5f5;
    color: rgb(255, 255, 255);
    background: #4b464e;
    border-radius: 8px;
}

.second {
    background: linear-gradient(#8a5b98, #150f19);
}

.third {
    background: linear-gradient(#adcded, #074879);   
}

.wave {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    overflow: hidden;
    line-height: 0;
}

.wave svg {
    position: relative;
    display: block;
    width: calc(163% + 1.3px);
    height: 133px;
}

.wave .shape-fill {
    fill: #FFFFFF;
}

.tilt {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    overflow: hidden;
    line-height: 0;
}

.tilt svg {
    position: relative;
    display: block;
    width: calc(163% + 1.3px);
    height: 339px;
}

.tilt .shape-fill {
    fill: #150f19;
}
</style>

<script setup>
// import wave_footer from "@/components/ui/wave_footer.vue";
</script>