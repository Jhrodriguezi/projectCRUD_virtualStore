<template>
  <div class="login">
    <div class="form-container">
      <h1 class="title">My account</h1>

      <form v-on:submit.prevent="processSignUpUser" class="form">
        <div>
          <label for="username" class="label">Username</label>
          <input
            type="text"
            id="name"
            placeholder="Your username"
            class="input input-name"
            v-model="user.username"
          />

          <label for="name" class="label">Name</label>
          <input
            type="text"
            id="name"
            placeholder="Your name"
            class="input input-name"
            v-model="user.name"
          />

          <label for="lastname" class="label">Lastname</label>
          <input
            type="text"
            id="lastname"
            placeholder="Your lastname"
            class="input input-lastname"
            v-model="user.lastname"
          />

          <label for="email" class="label">Email</label>
          <input
            type="text"
            id="email"
            placeholder="email@example.com"
            class="input input-email"
            v-model="user.email"
          />

          <label for="password" class="label">Password</label>
          <input
            type="password"
            id="password"
            placeholder="*********"
            class="input input-password"
            v-model="user.password"
          />
        </div>

        <input
          type="submit"
          value="Create"
          class="primary-button login-button"
        />
      </form>
    </div>
    <p id="customAlert" class="customAlert"></p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SignUp',

  data() {
    return {
      user: {
        username: '',
        name: '',
        lastname:'',
        email: '',
        password: '',
      },
    };
  },
  methods: {
    processSignUpUser() {
      axios
        .post('https://vsp-backend.herokuapp.com/user/', this.user, {
          headers: {},
        })
        .then((result) => {
          const dataSignUp = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };

          this.$emit('completedSignUp', dataSignUp);
        })
        .catch((error) => {
          console.log(error);
          const customAlert = document.getElementById('customAlert');
          customAlert.innerText = 'ERROR: Fallo en el registro.';
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
}
.logo {
  width: 150px;
  margin-bottom: 48px;
  justify-self: center;
  display: none;
}
.title {
  font-size: var(--lg);
  margin-bottom: 36px;
  text-align: start;
}
.form {
  display: flex;
  flex-direction: column;
}
.form div {
  display: flex;
  flex-direction: column;
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
.input-name,
.input-lastname,
.input-email,
.input-password {
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
.login-button {
  margin-top: 14px;
  margin-bottom: 30px;
}
.customAlert {
  font-size: var(--md);
  font-weight: bold;
}
@media (max-width: 640px) {
  .form-container {
    height: 100%;
  }
  .form {
    height: 100%;
    justify-content: space-between;
  }
}
</style>
