<script>
export default {
    name: 'AboutUs',
    data (){
        return {

        }
    },
    methods: {
        
    },
}
</script>

<template>
    <div id="dashboard-container">
        <div id="left-content">
            <img src="@/assets/loginbg.jpg">
        </div>

        <div id="right-content">
            <div id="page-header">
                <h1>About us</h1>
            </div>

            <div id="right-content-container">
                <div id="page-description-top">
                    <p>AquaEasy was founded by a team of innovative 4th-year college students with a passion for technology and environmental sustainability. As developers and environmental enthusiasts, we recognized the urgent need for smarter water management solutions in a world facing increasing water scarcity.</p>
                </div>

                <div id="page-description-bottom">
                    <p>Our mission is to provide users with an intuitive, efficient, and powerful tool to monitor and optimize water usage, helping to conserve this precious resource for future generations. Join us on our journey to make water management easy and sustainable for everyone.</p>
                </div>

                <div id="page-description-icon">
                    <img src="@/assets/facebook.png">
                    <img src="@/assets/twitter.png">
                    <img src="@/assets/instagram.png">
                </div>
            </div>
        </div>

    </div>
</template>

<style scoped>

#dashboard-container {
    height: 70vh;
    width: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
}

#left-content {
    width: 40vw;
    display: flex;
    flex-direction: column;
}

#left-content img {
    height: 100%;
    width: 100%;
    border-radius: 48px;
    border: 1px solid transparent;
}

#right-content {
    width: 60vw;
    display: flex;
    flex-direction: column;
    align-items: center;
}

#page-header {
    width: 95%;
    height: 15%;
    display: flex;
    align-items: center;
}

#page-header h1 {
    margin-top: 0;
    font-weight: bold;
    font-size: 48px;
}

#right-content-container {
    width: 95%;
    height: 85%;
    display: flex;
    flex-direction: column;
}

#page-description-top, #page-description-bottom {
    width: 100%;
    height: 20%;
    display: flex;
    flex-direction: column;
    text-align: justify;
}

p {
    font-weight: bold;
}

#page-description-icon {
    width: 100%;
    height: 10%;
    display: flex;
    flex-direction: row;
    margin-top: 28%;
}

#page-description-icon img {
    margin-right: 8px
}
</style>