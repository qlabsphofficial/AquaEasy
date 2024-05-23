<template>
    <div id="container">
        <div id="login-panel">
            <h1>{{ message }}</h1>
            <h4>Water Quality Monitoring</h4>

            <div id="login-form">
                <h4>Username</h4>
                <input type="text" placeholder="Enter your username..." v-model="username">

                <h4>Password</h4>
                <input type="password" placeholder="Enter your password..." v-model="password">
            </div>

            <div id="forgot-section">
                <h5 id="forgot-pass">Forgot Password?</h5>
            </div>

            <div id="interactivity-section">
                <button @click="login()">Login</button>
                <br><br>
                <a id="sign-up" @click="() => { this.$router.push('/register') }">Don't have an account? Sign up.</a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'LoginPage',
    methods: {
        async login() {
            try {
                const response = await fetch(`https://aquaeasy.onrender.com/login?username=${this.username}&password=${this.password}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
                });

                if (response.ok) {
                    const responseData = await response.json();

                    if (responseData && responseData.response === 'Login successful.') {
                        this.$router.push({ name: 'dashboard', params: { user_id: responseData.user_data.id } });
                    } else {
                        this.message = 'LOGIN FAILED.';
                        setTimeout(() => { this.message = 'LOGIN'}, 2000);
                    }
                } else {
                    console.log('Login Failed. Status:', response.status);
                }
            } catch (error) {
                console.error('An error occurred during login:', error.message);
            }
        }
    },
    data(){
        return {
            message: 'LOGIN',
            username: '',
            password: ''
        }
    }
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
    margin-top: 20%;
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
    height: 30%;
    width: 100%;
    text-align: center;
    
    button {
        height: 20%;
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

#forgot-section {
    width: 100%;
    margin-top: -10%;
    margin-bottom: 15%;
    text-align: right;
}
</style>