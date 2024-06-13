<template>
    <div id="container">
        <div id="top-section">
            <div id="top-section-title">
                <h3>Aquaeasy</h3>
            </div>
            
            <div id="top-section-menu">
                <h4 class="links" @click="changePageContent('HomePage')">Home</h4>
                <h4 class="links" @click="changePageContent('AboutUs')">About Us</h4>
                <h4 class="links" @click="changePageContent('Contact')">Contact</h4>
            </div>

            <div id="top-section-button">
                <button id="login-btn" @click="this.$router.push('/login')">Log in</button>
                <button id="signup-btn" @click="this.$router.push('/register')">Sign up</button>
            </div>
        </div>
        
        <div id="body-section">
            <component :is="this.current_component"></component>
        </div>

        <div id="footer-section">
            <p>AquaEasy: Water Quality Monitoring</p>
            <p>© 2024 AquaEasy, Inc. All rights reserved.</p>
        </div>
    </div>
</template>

<script>
import HomePage from './HomePage.vue';
import AboutUs from './AboutUsPage.vue';
import ContactPage from './ContactPage.vue';

export default {
    components: {HomePage, AboutUs, ContactPage},
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

                case 'Contact':
                    this.current_component = 'ContactPage';
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
    transform: translateX(-5%);
    animation: hoverInHorizontal .6s ease-in-out;
    animation-fill-mode: forwards;
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

.links {
    cursor: pointer;
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
    height: 30%;
    width: 28%;
    border-radius: 3px;
    border: 1px solid transparent;
    transition: .4s;
    cursor: pointer;
}

#login-btn {
    background-color: white;
}

#login-btn:hover {
    background-color: #1497DD;
    color: white;
}

#signup-btn {
    background-color: #1497DD;
    color: white;
}

#signup-btn:hover {
    border: 1px solid #1497DD;
    background-color: transparent;
    color: #1497DD;
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

@keyframes hoverInHorizontal {
    0% {
        opacity: 0;
    }

    100% {
        opacity: 1;
        transform: translateX(0);
    }
}
</style>