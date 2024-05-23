<template>
    <div id="container">
        <div id="login-panel">
            <h1>Sign In</h1>
            <h4>Water Quality Monitoring</h4>

            <div id="login-form">
                <h4>Username</h4>
                <input type="text" placeholder="Enter your username..." v-model="username">

                <h4>Password</h4>
                <input type="password" placeholder="Enter your password..." v-model="password">

                <h4>Confirm Password</h4>
                <input type="password" placeholder="Confirm your password..." v-model="confirm">

                <h4>First Name</h4>
                <input type="text" placeholder="Enter your first name..." v-model="first_name">

                <h4>Last Name</h4>
                <input type="text" placeholder="Enter your last name..." v-model="last_name">

                <h4>Email Address</h4>
                <input type="email" placeholder="Enter your email..." v-model="email">

                <h4>Contact Number</h4>
                <input type="text" placeholder="Enter your contact number..." v-model="contact">
            </div>

            <div id="interactivity-section">
                <button @click="register()">Sign In</button>
            </div>
        </div>
    </div>
</template>

<script>
export default { 
    name: 'RegisterPage',
    methods: {
        async register(){
            // const response = await fetch('http://127.0.0.1:8000/register', {
            const response = await fetch('https://aquaeasy.onrender.com/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    'username': this.username,
                    'password': this.password,
                    'confirm': this.confirm,
                    'first_name': this.first_name,
                    'last_name': this.last_name,
                    'contact': this.contact,
                    'email': this.email
                }),
            })

            if(response.ok){
                const responseData = await response.json();
                console.log(responseData.response);

                if (responseData.response == 'Registration successful.'){
                    this.$router.push('/');
                }
                else {
                    console.log('Failed');
                }
            }
            else {
                console.log(`Request failed with status ${response.status}`);
            }
        }
    },
    data(){
        return {
            username: '',
            password: '',
            confirm: '',
            first_name: '',
            last_name: '',
            contact: '',
            email: ''
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
    height: 60%;
    width: 95%;
    padding-right: 5%;
    overflow-y: scroll;
    margin-top: 15%;
    align-items: center;
    justify-content: center;

    input {
        padding: 2%;
        width: 96%;
        margin-bottom: 5%;
        border: none;
        border-bottom: 1px solid #919191;
    }

    input:focus {
        outline: none;
    }
}

#login-form::-webkit-scrollbar {
  width: 8px;
  border-radius: 15px;
}

#login-form::-webkit-scrollbar-thumb {
  background-color: #000;
  border-radius: 6px;
}

#login-form::-webkit-scrollbar-track {
  background: #f1f1f1;
}

#interactivity-section { 
    width: 100%;
    margin-top: 10%;
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