<template>
  <div class="container">
    <div class="row justify-content-center">
        <b-navbar type="light" variant="light">
          <b-navbar-nav>
            <b-nav-item to="/">Home Page</b-nav-item>
            <b-nav-item to="/companies">Companies</b-nav-item>
            <b-nav-item to="/shipments">Shipments</b-nav-item>
          </b-navbar-nav>
        </b-navbar>
        <router-view />
      </div>

    </div>
</template>

<style>
.container {
  padding: 2rem 0rem;
}

h4 {
  margin: 2rem 0rem 1rem;
}

td, th {
  vertical-align: middle;
}
</style>