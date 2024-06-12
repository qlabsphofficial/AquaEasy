<script>
export default {
    name: 'HomePage',
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
            <div id="page-header">
                <h1>Water Quality Monitoring</h1>
            </div>

            <div id="page-description">
                <h4>AquaEasy revolutionizes the way you monitor and control your water usage,</h4>
                <h4>providing a seamless experience for homeowners, businesses, and agricultural operations.</h4>
                <button>Explore</button>
            </div>
        </div>

        <div id="right-content">
            <img src="@/assets/loginbg.jpg">
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
    width: 50vw;
    display: flex;
    flex-direction: column;
}

#page-header {
    height: 40vh;
    display: flex;
    align-items: end;
    font-weight: bold;
    font-size: 24px;
}

#page-description {
    height: 60vh;
    display: flex;
    flex-direction: column;
    align-items: start;
}

h4 {
    margin: 1%;
}

button {
    margin-top: 4%;
    height: 12%;
    width: 20%;
    border-radius: 3px;
    border: 1px solid transparent;
}

#right-content {
    width: 50vw;
    display: flex;
    align-items: center;
}   

#right-content img {
    height: 100%;
    width: 100%;
    border-radius: 48px;
    border: 1px solid transparent;
}
</style>