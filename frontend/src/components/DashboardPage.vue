<template>
    <div id="container">
        <div id="navbar">
            <div id="app-banner">
                <img src="@/assets/team_logo.png" height="40%" width="40%">
                <h2>AquaEasy</h2>
            </div>

            <div class="nav-link" style="margin-top: 2.5%;">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-layout-dashboard"><rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/></svg>
                <h4 @click="changeComponent('AnalysisComponent')">Dashboard</h4>
            </div>

            <div class="nav-link">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-book-plus"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/><path d="M9 10h6"/><path d="M12 7v6"/></svg>
                <h4 @click="changeComponent('HistoricalData')">Logs</h4>
            </div>

            <div class="nav-link">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-book-x"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/><path d="m14.5 7-5 5"/><path d="m9.5 7 5 5"/></svg>
                <h4 @click="changeComponent('ChangeLogs')">Archive</h4>
            </div>

            <div class="nav-link">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-circle-help"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>
                <h4 @click="changeComponent('FaqPage')">FAQs</h4>
            </div>

            <div class="nav-link">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-circle-user"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="10" r="3"/><path d="M7 20.662V19a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v1.662"/></svg>
                <h4 @click="accessProfile()">Profile</h4>
            </div>

            <div class="nav-link">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-log-out"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/></svg>
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
import current_address from '@/address';

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
            const response = await fetch(`${current_address}/retrieve_dashboard_data?user_id=${this.user_id}`);
            const data = await response.json();

            if (response.ok){
                this.user_data = data.payload.user_data;
            }          
        }
    },
    props: ['user_id'],
    data(){
        return {
            currentComponent: 'AnalysisComponent',
            user_data: [],
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
        height: 100vh;
        width: 220px;
        min-width: 220px;
        background-color: #1497DD;
        color: white;
        padding: 20px;
        box-sizing: border-box;
        box-shadow: 2px 2px 2px 2px rgba(0, 0, 0, .3);
    }

    .nav-link {
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        margin-bottom: 15px;
        cursor: pointer;

        h4 {
            margin-left: 10%;
        }
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