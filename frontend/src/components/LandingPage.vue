<template>
    <div id="container">
        <div id="top-section">
            <div id="top-section-title">
                <h3>Aquaeasy</h3>
            </div>
            
            <div id="top-section-menu">
                <h4 class="links">Home</h4>
                <h4 class="links">About Us</h4>
                <h4 class="links">Contact</h4>
            </div>

            <div id="top-section-button">
                <button id="login-btn">Log in</button>
                <button id="signup-btn">Sign up</button>
            </div>
        </div>
        
        <div id="body-section">
            <div id="left-content">
                <div id="body-section-title">
                    <h2>Lorem Ipsum Dolor.</h2>
                </div>

                <div id="body-section-desc">
                    <h4>Lorem ipsum dolor sit amet, consectetur</h4>
                    <h4>adipiscing elit, sed do eiusmod tempor incidunt</h4>
                </div>

                <div id="body-section-button">
                    <button>Explore</button>                    
                </div>
            </div>

            <div id="right-content">
            
            </div>
        </div>

        <div id="footer-section">
            
        </div>
    </div>
</template>

<script>


export default {
    name: 'LandingPage',
    methods: {
        
    }
}
</script>

<style scoped lang="scss">

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
    width: 95vw;
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
    height: 75vh;
    width: 95vw;
    display: flex;
    flex-direction: row;
}

#left-content {
    background-color: blue;
    width: 50vw;
    display: flex;
    flex-direction: column;
    align-items: center;
}

#body-section-title {
    height: 30vh;
    width: 100vw;
    background-color: red;
}

#body-section-desc {
    height: 40vh;
    width: 100vw;
    background-color: grey;
}

#body-section-button {
    height: 30vh;
    width: 100vw;
    background-color: green;
}


#right-content {
    width: 50vw;
    background-color: blue;
}

#footer-section {
    height: 10vh;
    width: 95vw;
    
    background-color: yellow;
}
</style>