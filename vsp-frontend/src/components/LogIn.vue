<template>
  <div class="login">
    <div class="form-container">
      <img src="" alt="logo" class="logo" />

      <form v-on:submit.prevent="processLogInUser" class="form">
        <label for="email" class="label">Username</label>
        <input
          type="text"
          id="email"
          placeholder="email@example.com"
          class="input input-email"
          v-model="user.username"
        />

        <label for="password" class="label">Password</label>
        <input
          type="password"
          id="password"
          placeholder="*********"
          class="input input-password"
          v-model="user.password"
        />

        <input
          type="submit"
          value="Log in"
          class="primary-button login-button"
        />
        <a href="/">Forgot my password</a>
      </form>

      <button class="secondary-button signup-button">Sign up</button>
    </div>
    <p id="customAlert" class="customAlert"></p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'logIn',

  data() {
    return {
      user: {
        username: '',
        password: '',
      },
    };
  },
  methods: {
    processLogInUser() {
      axios
        .post('https://virtual-store-app.herokuapp.com/login/', this.user, {
          headers: {},
        })
        .then((result) => {
          const dataLogIn = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };

          this.$emit('completedLogIn', dataLogIn);
        })
        .catch((error) => {
          if (error.response.status === '401') {
            const customAlert = document.getElementById('customAlert');
            customAlert.innerText = 'Error 401: Credenciales incorrectas';
          }
        });
    },
  },
};
</script>

<style>
:root {
  --white: #ffffff;
  --black: #000000;
  --very-light-pink: #c7c7c7;
  --text-input-field: #f7f7f7;
  --hospital-green: #acd9b2;
  --sm: 14px;
  --md: 16px;
  --lg: 18px;
}
body {
  margin: 0;
  font-family: 'Quicksand', sans-serif;
}
.login {
  width: 100%;
  height: 100vh;
  display: grid;
  place-items: center;
}
.form-container {
  display: grid;
  grid-template-rows: auto 1fr auto;
  width: 300px;
  background-color: #fff;
  border-radius: 5px;
  padding: 20px 20px;
}
.logo {
  width: 150px;
  margin-bottom: 48px;
  justify-self: center;
  display: none;
}
.form {
  display: flex;
  flex-direction: column;
}
.form a {
  color: var(--hospital-green);
  font-size: var(--sm);
  text-align: center;
  text-decoration: none;
  margin-bottom: 52px;
}
.label {
  font-size: var(--sm);
  font-weight: bold;
  margin-bottom: 4px;
}
.input {
  background-color: var(--text-input-field);
  border: none;
  border-radius: 8px;
  height: 30px;
  font-size: var(--md);
  padding: 6px;
  margin-bottom: 12px;
}
.input-email {
  margin-bottom: 22px;
}
.primary-button {
  background-color: var(--hospital-green);
  border-radius: 8px;
  border: none;
  color: var(--white);
  width: 100%;
  cursor: pointer;
  font-size: var(--md);
  font-weight: bold;
  height: 50px;
}
.secondary-button {
  background-color: var(--white);
  border-radius: 8px;
  border: 1px solid var(--hospital-green);
  color: var(--hospital-green);
  width: 100%;
  cursor: pointer;
  font-size: var(--md);
  font-weight: bold;
  height: 50px;
}
.login-button {
  margin-top: 14px;
  margin-bottom: 30px;
}
.customAlert {
  font-size: var(--md);
  font-weight: bold;
}
@media (max-width: 640px) {
  .logo {
    display: block;
  }
  .form a {
    margin-bottom: 70px;
  }
  .secondary-button {
    position: absolute;
    bottom: 0;
    max-width: 300px;
    margin-bottom: 20px;
  }
}
</style>
