<template>
    <div id="container">
        <div id="navbar">
            <div id="app-banner">
                <h2>AquaEasy</h2>
            </div>

            <div class="nav-link">
                <img src="" alt="" class="nav-link-icon">
                <h4 @click="changeComponent('AnalysisComponent')">Dashboard</h4>
            </div>

            <div class="nav-link">
                <img src="" alt="" class="nav-link-icon">
                <h4 @click="changeComponent('HistoricalData')">Logs</h4>
            </div>

            <div class="nav-link">
                <img src="" alt="" class="nav-link-icon">
                <h4 @click="changeComponent('ChangeLogs')">Archive</h4>
            </div>

            <div class="nav-link">
                <img src="" alt="" class="nav-link-icon">
                <h4 @click="changeComponent('FaqPage')">FAQs</h4>
            </div>

            <div class="nav-link">
                <img src="" alt="" class="nav-link-icon">
                <h4 @click="accessProfile()">Profile</h4>
            </div>

            <div class="nav-link">
                <img src="" alt="" class="nav-link-icon">
                <h4 @click="this.$router.push('/')">Log Out</h4>
            </div>
        </div>

        <div id="main-content">
            <component :is="currentComponent" :user_data="this.user_data" />
        </div>
    </div>
</template>

<script>
import HistoricalData from './HistoricalData.vue';
import AnalysisComponent from './AnalysisComponent.vue';
import FaqPage from './FaqPage.vue';
import ProfilePage from './ProfilePage.vue';
import LoginPage from './LoginPage.vue';
import ChangeLogs from './ChangeLogs.vue';

export default {
    name: 'DashboardPage',
    components: {
        HistoricalData,
        AnalysisComponent,
        FaqPage,
        LoginPage,
        ProfilePage,
        ChangeLogs
    },  
    methods: {
        changeComponent(componentName){
            this.currentComponent = componentName;
        },
        accessProfile(){
            this.currentComponent = 'ProfilePage';
        },
        async retrieve_dashboard_data(){
            // const response = await fetch(`http://127.0.0.1:8000/retrieve_dashboard_data?user_id=${this.user_id}`);
            const response = await fetch(`https://aquaeasy.onrender.com/retrieve_dashboard_data?user_id=${this.user_id}`);
            const data = await response.json();

            if (!response.ok){
                console.log('Failed.');
            }
            else{
                this.user_data = data.payload.user_data;
                console.log(this.user_data);
            }            
        }
    },
    props: ['user_id'],
    data(){
        return {
            user_data: [],
            currentComponent: 'AnalysisComponent',
            turbidity_data: [],
            humidity_data: [],
            tds_data: [],
            ec_data: []
        }
    },
    mounted() {
        console.log(this.user_id);
        this.retrieve_dashboard_data();
    },
}
</script>

<style scoped lang="scss">
#container {
        height: 100vh;
        width: 100vw;
        display: flex;
        position: absolute;
        top: 0;
        left: 0;
    }

    #navbar {
        width: 220px;
        min-width: 220px;
        background-color: #1497DD;
        color: white;
        padding: 20px;
        box-sizing: border-box;
    }

    .nav-link {
        margin-bottom: 15px;
        cursor: pointer;
    }

    #main-content {
        overflow-y: scroll;
        flex-grow: 1;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
        box-sizing: border-box;
    }
</style>