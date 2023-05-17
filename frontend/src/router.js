import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      redirect: "/index"
    },
    {
      path: "/index",
      name: "index",
      component: () => import("./components/IndexComponent.vue")
    },
    {
      path: "/companies",
      name: "companies",
      component: () => import("./components/CompanyComponent.vue")
    },
    {
      path: "/company/edit/:id",
      name: "company-edit",
      component: () => import("./components/CompanyEditComponent.vue")
    },
    {
      path: "/company/create",
      name: "company-create",
      component: () => import("./components/CompanyCreateComponent.vue")
    },
    {
      path: "/shipments",
      name: "shipments",
      component: () => import("./components/ShipmentComponent.vue")
    },
    {
      path: "/shipment/edit/:id",
      name: "shipment-edit",
      component: () => import("./components/ShipmentEditComponent.vue")
    },
    {
      path: "/shipment/create",
      name: "shipment-create",
      component: () => import("./components/ShipmentCreateComponent.vue")
    }
  ]
});
