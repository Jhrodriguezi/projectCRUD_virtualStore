<template>
  <nav class="nav-home">
    <img src="../assets/icons/icon_menu.svg" alt="menu" class="menu" />
    <div class="navbar-left">
      <img src="../assets/logo.png" alt="logo" class="logo" />
      <ul>
        <li>
          <a href="/">All</a>
        </li>
        <li>
          <a href="/">Video Cards</a>
        </li>
        <li>
          <a href="/">Laptops</a>
        </li>
        <li>
          <a href="/">components</a>
        </li>
        <li>
          <a href="/">Cases</a>
        </li>
      </ul>
    </div>
    <div class="navbar-right">
      <ul>
        <li class="navbar-email">Email@example.com</li>
        <li class="navbar-shopping-cart">
          <img
            src="../assets/icons/icon_shopping_cart.svg"
            alt="shopping cart"
          />
          <div>2</div>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
// @ is an alias to /src
export default {};
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
.nav-home {
  display: flex;
  justify-content: space-between;
  padding: 0 24px;
  border-bottom: 1px solid var(--very-light-pink);
  background-color: #fff;
}
.menu {
  display: none;
}
.logo {
  width: 100px;
}
.navbar-left ul,
.navbar-right ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  align-items: center;
  height: 60px;
}
.navbar-left {
  display: flex;
}
.navbar-left ul {
  margin-left: 12px;
}
.navbar-left ul li a,
.navbar-right ul li a {
  text-decoration: none;
  color: var(--hospital-green);
  border: 1px solid var(--white);
  padding: 8px;
  border-radius: 8px;
}
.navbar-left ul li a:hover,
.navbar-right ul li a:hover {
  border: 1px solid var(--hospital-green);
  color: var(--hospital-green);
}
.navbar-email {
  color: var(--very-light-pink);
  font-size: var(--sm);
  margin-right: 12px;
}
.navbar-shopping-cart {
  position: relative;
}
.navbar-shopping-cart div {
  width: 16px;
  height: 16px;
  background-color: var(--hospital-green);
  border-radius: 50%;
  font-size: var(--sm);
  font-weight: bold;
  position: absolute;
  top: -6px;
  right: -3px;
  display: flex;
  justify-content: center;
  align-items: center;
}
@media (max-width: 640px) {
  .menu {
    display: block;
  }
  .navbar-left ul {
    display: none;
  }
  .navbar-email {
    display: none;
  }
}
</style>
