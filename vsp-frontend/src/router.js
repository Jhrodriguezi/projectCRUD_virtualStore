import { createRouter, createWebHashHistory } from 'vue-router';
import App from './App.vue';
import Home from './components/Home.vue';
import SignUp from './components/SignUp.vue';
import LogIn from './components/LogIn.vue';
import MyOrder from './components/MyOrder.vue';
import ProductPage from './components/ProductPage.vue';
import UserSettings from './components/UserSettings.vue';

const routes = [
  {
    path: '/',
    name: 'root',
    component: App,
  },
  {
    path: '/user/home',
    name: 'home',
    component: Home,
  },
  {
    path: '/user/logIn',
    name: 'logIn',
    component: LogIn,
  },
  {
    path: '/user/signUp',
    name: 'signUp',
    component: SignUp,
  },
  {
    path: '/user/myOrder',
    name: 'myOrder',
    component: MyOrder,
  },
  {
    path: '/user/productPage',
    name: 'productPage',
    component: ProductPage,
  },
  {
    path: '/user/mysettings',
    name: 'userSettings',
    component: UserSettings,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
