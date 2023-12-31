<template>
    <div id="container">
        <div class="nav-link">
            <img src="" alt="" class="nav-link-icon">
            <h4>Dashboard</h4>
        </div>

        <div class="nav-link">
            <img src="" alt="" class="nav-link-icon">
            <h4>Archive</h4>
        </div>

        <div class="nav-link">
            <img src="" alt="" class="nav-link-icon">
            <h4>FAQs</h4>
        </div>

        <div class="nav-link">
            <img src="" alt="" class="nav-link-icon">
            <h4>Profile</h4>
        </div>

        <div class="nav-link">
            <img src="" alt="" class="nav-link-icon">
            <h4>Log Out</h4>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SideNavigation',
    methods: {

    }
}
</script>

<style scoped lang="scss">
#container {
    display: flex;
    flex-wrap: wrap;
    height: 100vh;
    width: 15vw;
    position: absolute;
    top: 0;
    left: 0;
    background-color: #6B9AB5;
}
</style>