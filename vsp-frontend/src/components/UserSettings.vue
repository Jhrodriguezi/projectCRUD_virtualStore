<template>
  <!--    <div v-if="loaded" class="information">
        <h1>Información de su cuenta</h1>
        <h2>Nombre: <span>{{name}}</span></h2>
        <h2>Saldo: <span>{{balance}} COP </span></h2>
        <h2>Correo electrónico: <span>{{email}}</span></h2>
    </div>
  -->
  <div class="userSettings">
    <div class="form-container">
      <h1 class="title">My account</h1>
      <form v-on:submit.prevent="processUpdateUser" class="form">
        <div v-if="loaded">
          <label for="username" class="label">Username</label>
          <input
            type="text"
            id="name"
            class="input input-name"
            v-model="user.username"
          />
          <label for="name" class="label">Name</label>
          <input
            type="text"
            id="name"
            class="input input-name"
            v-model="user.name"
          />

          <label for="lastname" class="label">Lastname</label>
          <input
            type="text"
            id="lastname"
            class="input input-lastname"
            v-model="user.lastname"
          />

          <label for="email" class="label">Email</label>
          <input
            type="text"
            id="email"
            class="input input-email"
            v-model="user.email"
          />
          <label for="password" class="label">Password</label>
          <input
            type="password"
            id="password"
            class="input input-password"
            v-model="user.password"
          />
        </div>

        <input
          type="submit"
          value="Actualizar"
          class="primary-button login-button"
        />
      </form>
      <button
          type="button"
          class="danger-button"
          v-on:click="processDeleteUser()"
        >Eliminar</button>
    </div>
    <p id="customAlert" class="customAlert"></p>
  </div>
</template>

<script>
import jwt_decode from "jwt-decode";
import axios from 'axios';

export default {
    name: "userSettings",

    data: function(){
        return {
          user:{
            username: '',
            name: '',
            lastname:'',
            email: '',
            password: '',
            },
          loaded: false,
        }
    },

    methods: {
      async processUpdateUser() {
      await this.verifyToken();
      let token=localStorage.getItem("token_access");
      let userId = jwt_decode(token).user_id.toString();
      
      axios
        .patch(`https://vsp-backend.herokuapp.com/user/update/${userId}`, this.user,
          {headers: {'Authorization': `Bearer ${token}`}},)
        .then(() => {
          alert("Actualización exitosa")
          this.user.password="";
          const customAlert = document.getElementById('customAlert');
          if(customAlert.innerText!=""){
            customAlert.innerText = '';
          }
        })
        .catch((error) => {
          console.log(error);
          const customAlert = document.getElementById('customAlert');
          customAlert.innerText = 'ERROR: Fallo en la actualización.';
        });
    },
    async processDeleteUser() {
      await this.verifyToken();
      let token=localStorage.getItem("token_access");
      let userId = jwt_decode(token).user_id.toString();
      
      axios
        .delete(`https://vsp-backend.herokuapp.com/user/delete/${userId}`,
          {headers: {'Authorization': `Bearer ${token}`}},)
        .then(() => {
          alert("Eliminación exitosa")
          this.$emit('logOut');
        })
        .catch((error) => {
          console.log(error);
          const customAlert = document.getElementById('customAlert');
          customAlert.innerText = 'ERROR: Fallo en la eliminación.';
        });
    },
        getData: async function () {

            if (localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null) {
                this.$emit('logOut');
                return;
			}

            await this.verifyToken();
            
            let token = localStorage.getItem("token_access");
            let userId = jwt_decode(token).user_id.toString();
            
            axios.get(`https://vsp-backend.herokuapp.com/user/${userId}`, {headers: {'Authorization': `Bearer ${token}`}})
                .then((result) => {

                    this.user.username = result.data.username;
                    this.user.name = result.data.name;	
                    this.user.lastname = result.data.lastname;
                    this.user.email = result.data.email;
                    this.loaded=true;
                    })
                .catch(() => {
                    this.$emit('logOut');
                });
        },

        verifyToken: function () {
            return axios.post("https://vsp-backend.herokuapp.com/refresh/", {refresh: localStorage.getItem("token_refresh")}, {headers: {}})
				.then((result) => {
					localStorage.setItem("token_access", result.data.access);		
				})
				.catch(() => {
					this.$emit('logOut');
				});
        }
    },

    created: async function(){
        this.getData();
    },
}
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
.userSettings {
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

.danger-button {
  background-color: red;
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