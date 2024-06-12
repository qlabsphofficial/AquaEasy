<template>
    <div id="container">
        <div id="top-section">
            <div id="top-section-title">
                <h3>Aquaeasy</h3>
            </div>
            
            <div id="top-section-menu">
                <h4 class="links" @click="changePageContent('HomePage')">Home</h4>
                <h4 class="links" @click="changePageContent('AboutUs')">About Us</h4>
                <h4 class="links" @click="changePageContent('Dashboard')">Contact</h4>
            </div>

            <div id="top-section-button">
                <button id="login-btn">Log in</button>
                <button id="signup-btn">Sign up</button>
            </div>
        </div>
        
        <div id="body-section">
            <component :is="this.current_component"></component>
        </div>

        <div id="footer-section">
            <p>Lorem ipsum dolor sit amet, consectetur adisplacing elit, sed do</p>
            <p>eiusmod tempar incididunt</p>
        </div>
    </div>
</template>

<script>
import HomePage from './HomePage.vue';
import AboutUs from './AboutUsPage.vue';

export default {
    components: {HomePage, AboutUs},
    name: 'LandingPage',

    data () {
        return {
            current_component: HomePage
        }
    },

    methods: {
        async changePageContent(page){
            switch(page){
                case 'HomePage':
                    this.current_component = 'HomePage';
                    break;

                case 'AboutUs':
                    this.current_component = 'AboutUs';
                    break;

                case 'Display Data':
                    this.current_component = 'UploadContent';
                    break;

                case 'Upload History':
                    this.current_component = 'UploadHistory';
                    break;
            }
        }
    },
}
</script>

<style scoped>
#container {
    height:100vh;
    width: 100vw;
    position: absolute;
    top: 0;
    left: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
}

#top-section {
    height: 15vh;
    width: 94vw;
    display: flex;
    flex-direction: row;
}

#top-section-title {
    width: 20vw;
    display: flex;
    align-items: center;
}

#top-section-menu {
    width: 50vw;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
}

.links, button {
    margin-left: 8%;
}

#top-section-button {
    width: 25vw;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: end;
}

button {
    height: 40%;
    width: 28%;
    border-radius: 3px;
    border: 1px solid transparent;
}

#login-btn {
    background-color: white;
}

#signup-btn {
    background-color: blue;
    color: white;
}

#body-section {
    height: 70vh;
    width: 94vw;
    display: flex;
    flex-direction: row;
}

#footer-section {
    height: 15vh;
    width: 94vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    font-weight: bold;
}

p {
    margin: 0;
}
</style>