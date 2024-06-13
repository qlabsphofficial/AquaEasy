<script>
export default {
    name: 'ContactPage',
    data (){
        return {

        }
    },
    methods: {
        
    },
}
</script>

<template>
    <div id="contact-container">
        <div id="top-content">
            <h1>GET IN TOUCH</h1>

            <div id="contact-channels">
                <h3>Phone: 0999999999</h3>
                <h3>Email: aquaeasy@gmail.com</h3>
            </div>
        </div>

        <div id="bottom-content">
            <div id="left-content">
                <input type="text" placeholder="Your name...">
                <input type="email" placeholder="Your email...">
                <input type="text" placeholder="Your contact number...">
                <button>Send Message</button>
            </div>

            <div id="right-content">
                <textarea name="" id="" cols="120" rows="23" placeholder="Your message..."></textarea>
            </div>
        </div>
    </div>
</template>

<style scoped>
#contact-container {
    height: 70vh;
    width: 100%;
    position: relative;
    display: flex;
    flex-direction: column;
}

#top-content {
    height: 30vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
}

#bottom-content {
    height: 70%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

#left-content {
    width: 50vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    transform: translateY(-5%);
    animation: hoverIn .6s ease-in-out;
    animation-fill-mode: forwards;
    animation-delay: .4s;
    opacity: 0;
}

#left-content input {
    height: 5vh;
    margin: 2.5% 2.5% 0% 0%;
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

textarea {
    font-size: 13px;
    padding: 2%;
    font-family: Avenir, Helvetica, Arial, sans-serif;
    resize: none;
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