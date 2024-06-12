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
    transform: translateY(-5%);
    animation: hoverIn .6s ease-in-out;
    animation-fill-mode: forwards;
    animation-delay: .4s;
    opacity: 0;
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
    transition: .4s;
    background-color: #1497DD;
    color: white;
}

button:hover {
    border: 1px solid #1497DD;
    background-color: transparent;
    color: #1497DD;
}

#right-content {
    width: 50vw;
    display: flex;
    align-items: center;
    transform: translateY(-5%);
    animation: hoverIn .6s ease-in-out;
    animation-fill-mode: forwards;
    animation-delay: .4s;
    opacity: 0;
}   

#right-content img {
    height: 100%;
    width: 100%;
    border-radius: 48px;
    border: 1px solid transparent;
}

@keyframes hoverIn {
    0% {
        opacity: 0;
    }

    100% {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>