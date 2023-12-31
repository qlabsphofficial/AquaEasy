<template>
    <div id="container">
        <div id="login-panel">
            <h1>Sign In</h1>
            <h4>Water Quality Monitoring</h4>

            <div id="login-form">
                <h4>Username</h4>
                <input type="text" placeholder="Enter your username...">

                <h4>Password</h4>
                <input type="password" placeholder="Enter your password...">

                <h4>Confirm Password</h4>
                <input type="password" placeholder="Confirm your password...">
            </div>

            <div id="interactivity-section">
                <button>Sign In</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'RegisterPage',
}
</script>

<style scoped lang="scss">
#container {
    height: 100vh;
    width: 100vw;
    background: url('@/assets/loginbg.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    display: flex;
    align-items: center;
    position: absolute;
    top: 0;
    left: 0;
}

#login-panel {
    height: 80vh;
    width: 25vw;
    padding: 2%;
    padding-left: 4%;
    padding-right: 4%;
    margin-left: 3%;
    background-color: white;
    border-radius: 15px;
    box-shadow: 2px 2px 2px #919191;
    text-align: left;

    h1 {
        margin-top: 15%;
        line-height: 0;
    }
}

#login-form {
    height: 40%;
    width: 100%;
    margin-top: 15%;
    align-items: center;
    justify-content: center;

    input {
        padding: 2%;
        width: 100%;
        margin-bottom: 5%;
        border: none;
        border-bottom: 1px solid #919191;
    }

    input:focus {
        outline: none;
    }
}

#interactivity-section { 
    width: 100%;
    margin-top: 30%;
    text-align: center;
    
    button {
        height: 5vh;
        width: 50%;
        background-color: #000;
        color: white;
        border-radius: 15px;
        border: 1px solid transparent;
        transition: .4s;
    }

    button:hover {
        background-color: transparent;
        border: 1px solid black;
        color: black;
    }
}
</style>