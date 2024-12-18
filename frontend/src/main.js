import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';

import LoginPage from './components/LoginPage.vue';
import RegisterPage from './components/RegisterPage.vue';
import DashboardPage from './components/DashboardPage.vue';
import ForgotPass from './components/ForgotPass.vue';
import LandingPage from './components/LandingPage.vue';

const app = createApp(App);

const routes = [
  { path: '/', component: LandingPage },
  { path: '/login', component: LoginPage },
  { path: '/register', component: RegisterPage },
  { path: '/forgot_pass', component: ForgotPass },
  { path: '/dashboard/:user_id', component: DashboardPage, name: 'dashboard', props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

app.use(router);

app.mount('#app');