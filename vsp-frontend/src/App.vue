<template>
  <div id="app" class="app">
    <div class="header">
      <h1>Virtual Store</h1>
      <nav>
        <button v-if="is_auth" v-on:click="loadHome">Home</button>
        <button v-if="!is_auth" v-on:click="loadLogIn">LogIn</button>
        <button v-if="!is_auth" v-on:click="loadSignUp">SignUp</button>
        <button v-if="is_auth" v-on:click="loadMyOrder">MyOrder</button>
        <button v-if="is_auth" v-on:click="loadProductPage">Products</button>
        <button v-if="is_auth" v-on:click="loadUserSettings">Configuración</button>
        <button v-if="is_auth" v-on:click="logOut">Cerrar sesión</button>
      </nav>
    </div>
    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:logOut="logOut"
      >
      </router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',

  data() {
    return {
      is_auth: false,
    };
  },

  components: {},

  methods: {
    verifyAuth() {
      this.is_auth = localStorage.getItem('isAuth') || false;

      if (this.is_auth === false) this.$router.push({ name: 'logIn' });
      else this.$router.push({ name: 'home' });
    },

    loadLogIn() {
      this.$router.push({ name: 'logIn' });
    },

    loadSignUp() {
      this.$router.push({ name: 'signUp' });
    },

    completedLogIn(data) {
      localStorage.setItem('isAuth', true);
      localStorage.setItem('username', data.username);
      localStorage.setItem('token_access', data.token_access);
      localStorage.setItem('token_refresh', data.token_refresh);
      alert('Autenticación Exitosa');
      this.verifyAuth();
    },

    completedSignUp(data) {
      alert('Registro Exitoso');
      this.completedLogIn(data);
    },

    loadHome() {
      this.$router.push({ name: 'home' });
    },

    loadMyOrder() {
      this.$router.push({ name: 'myOrder' });
    },

    loadProductPage() {
      this.$router.push({ name: 'productPage' });
    },

    loadUserSettings() {
      this.$router.push({ name: 'userSettings' });
    },

    logOut() {
      localStorage.clear();
      alert('Sesión Cerrada');
      this.verifyAuth();
    },
  },

  created() {
    this.verifyAuth();
  },
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
.app {
  height: 100vh;
}

.header {
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #283747;
  color: #e5e7e9;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header h1 {
  width: 20%;
  text-align: center;
}

.header nav {
  height: 100%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  font-size: 20px;
}

.header nav button {
  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 0 0 0 10px;
  cursor: pointer;
}

.header nav button:hover {
  color: #283747;
  background: #e5e7e9;
  border: 1px solid #e5e7e9;
}
.main-component {
  background: #ffffff;
  height: 100vh;
  background: center / cover no-repeat
    url(https://images.pexels.com/photos/9072394/pexels-photo-9072394.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260);
}
</style>
