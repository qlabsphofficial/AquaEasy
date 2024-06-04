<template>
    <div id="profile-section">
        <h1>Profile</h1>
    
        <div id="profile-details">
            <h4>Name: {{ user_data.first_name }} {{ user_data.last_name }}</h4>
            <h4>Email: {{ user_data.email }}</h4>
            <h4>Contact: {{ user_data.contact }}</h4>
        </div>
    </div>
</template>

<script>
// import current_address from '@/address';

export default {
    name: 'ProfilePage',
    props: {
        user_data: {}
    }
}
</script>

<style scoped lang="scss">
#profile-section {
    height: 90%;
    width: 90%;
    text-align: left;
}
</style>