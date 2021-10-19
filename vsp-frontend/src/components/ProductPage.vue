<template>
  <div class="cards-container">
    <div class="product-card">
      <img
        src="https://images.pexels.com/photos/7046727/pexels-photo-7046727.jpeg?auto=compress&cs=tinysrgb&h=640&w=480"
        alt="Games"
      />
      <div class="product-info">
        <div>
          <p>$120,00</p>
          <p>Games</p>
        </div>
        <figure>
          <img src="../assets/icons/bt_add_to_cart.svg" alt="" />
        </figure>
      </div>
    </div>
    <div class="product-card">
      <img
        src="https://images.pexels.com/photos/7046727/pexels-photo-7046727.jpeg?auto=compress&cs=tinysrgb&h=640&w=480"
        alt="Games"
      />
      <div class="product-info">
        <div>
          <p>$120,00</p>
          <p>Games</p>
        </div>
        <figure>
          <img src="../assets/icons/bt_add_to_cart.svg" alt="" />
        </figure>
      </div>
    </div>
    <div class="product-card">
      <img
        src="https://images.pexels.com/photos/7046727/pexels-photo-7046727.jpeg?auto=compress&cs=tinysrgb&h=640&w=480"
        alt="Games"
      />
      <div class="product-info">
        <div>
          <p>$120,00</p>
          <p>Games</p>
        </div>
        <figure>
          <img src="../assets/icons/bt_add_to_cart.svg" alt="" />
        </figure>
      </div>
    </div>
    <div class="product-card">
      <img
        src="https://images.pexels.com/photos/7046727/pexels-photo-7046727.jpeg?auto=compress&cs=tinysrgb&h=640&w=480"
        alt="Games"
      />
      <div class="product-info">
        <div>
          <p>$120,00</p>
          <p>Games</p>
        </div>
        <figure>
          <img src="../assets/icons/bt_add_to_cart.svg" alt="" />
        </figure>
      </div>
    </div>
    <div class="product-card">
      <img
        src="https://images.pexels.com/photos/7046727/pexels-photo-7046727.jpeg?auto=compress&cs=tinysrgb&h=640&w=480"
        alt="Games"
      />
      <div class="product-info">
        <div>
          <p>$120,00</p>
          <p>Games</p>
        </div>
        <figure>
          <img src="../assets/icons/bt_add_to_cart.svg" alt="" />
        </figure>
      </div>
    </div>
    <div class="product-card">
      <img
        src="https://images.pexels.com/photos/7046727/pexels-photo-7046727.jpeg?auto=compress&cs=tinysrgb&h=640&w=480"
        alt="Games"
      />
      <div class="product-info">
        <div>
          <p>$120,00</p>
          <p>Games</p>
        </div>
        <figure>
          <img src="../assets/icons/bt_add_to_cart.svg" alt="" />
        </figure>
      </div>
    </div>
    <div class="product-card">
      <img
        src="https://images.pexels.com/photos/7046727/pexels-photo-7046727.jpeg?auto=compress&cs=tinysrgb&h=640&w=480"
        alt="Games"
      />
      <div class="product-info">
        <div>
          <p>$120,00</p>
          <p>Games</p>
        </div>
        <figure>
          <img src="../assets/icons/bt_add_to_cart.svg" alt="" />
        </figure>
      </div>
    </div>
    <div class="product-card">
      <img
        src="https://images.pexels.com/photos/7046727/pexels-photo-7046727.jpeg?auto=compress&cs=tinysrgb&h=640&w=480"
        alt="Games"
      />
      <div class="product-info">
        <div>
          <p>$120,00</p>
          <p>Games</p>
        </div>
        <figure>
          <img src="../assets/icons/bt_add_to_cart.svg" alt="" />
        </figure>
      </div>
    </div>
  </div>
</template>

<script>
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
.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, 240px);
  gap: 20px;
  place-content: center;
  padding: 100px 0 0 0;
}
.product-card {
  width: 270px;
  background-color: #fff;
  border-radius: 5px;
  padding: 20px 20px;
}
.product-card img {
  width: 240px;
  height: 240px;
  border-radius: 20px;
  object-fit: cover;
}
.product-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 12px;
}
.product-info figure {
  margin: 0;
}
.product-info figure img {
  width: 35px;
  height: 35px;
}
.product-info div p:nth-child(1) {
  font-weight: bold;
  font-size: var(--md);
  margin-top: 0;
  margin-bottom: 4px;
}
.product-info div p:nth-child(2) {
  font-size: var(--sm);
  margin-top: 0;
  margin-bottom: 0;
  color: var(--very-light-pink);
}
@media (max-width: 640px) {
  .cards-container {
    grid-template-columns: repeat(auto-fill, 140px);
  }
  .product-card {
    width: 140px;
  }
  .product-card img {
    width: 140px;
    height: 140px;
  }
}
</style>
