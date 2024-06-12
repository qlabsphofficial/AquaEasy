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
                <h1>Lorem Ipsum Dolor.</h1>
            </div>

            <div id="page-description">
                <h4>Lorem ipsum dolor sit amet, consectetur</h4>
                <h4>adipiscing elit, sed do eiusmod tempor incididunt</h4>
                <button>Explore</button>
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

#right-content {
    width: 60vw;
    display: flex;
    align-items: center;
}
</style>