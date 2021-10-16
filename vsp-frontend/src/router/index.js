import { createRouter, createWebHashHistory } from 'vue-router';
import App from '../App.vue';
import SignUp from '../components/SignUp.vue';
import LogIn from '../components/LogIn.vue';

const routes = [
  {
    path: '/',
    name: 'root',
    component: App,
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
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
