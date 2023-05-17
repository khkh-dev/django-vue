<template>
    <div class="pt-5">
        <form @submit="checkForm" @submit.prevent="update" method="post">
            <div class="form-group">
                <label for="title">Title</label>
                <input
                    type="text"
                    class="form-control"
                    id="title"
                    v-model="shipment.title"
                    v-validate="'required'"
                    name="title"
                    placeholder="Enter title"
                >
                <div class="errors-block pt-1 text-md-left">
                  <p class="form-errors" v-if="titleErrors && titleErrors.length">
                    {{ titleErrors }}
                  </p>
                </div>
            </div>

            <div class="form-group">
                <label for="description">Description</label>
                <input
                    type="text"
                    class="form-control"
                    id="description"
                    v-model="shipment.description"
                    name="description"
                    placeholder="Enter description"
                >
            </div>

            <div class="form-group">
                <label for="quantity">Quantity</label>
                <input
                    type="number"
                    class="form-control"
                    id="quantity"
                    v-model="shipment.quantity"
                    v-validate="'required'"
                    name="quantity"
                    placeholder="Enter quantity"
                >
                <div class="errors-block pt-1 text-md-left">
                  <p class="form-errors" v-if="quantityErrors && quantityErrors.length">
                    {{ quantityErrors }}
                  </p>
                </div>
            </div>

            <div class="form-group">
              <label for="company">Company</label>
              <select
                name="company"
                class="form-control"
                id="company"
                v-model="shipment.company"
              >
              <option v-for="item in options" :value="item.id" :key="item.id">{{ item.name }}</option>
              </select>
            </div>

            <div class="form-group">
                <label for="delivery_country">Delivery Country</label>
                <select
                    name="delivery_country"
                    class="form-control"
                    id="delivery_country"
                    v-model="shipment.delivery_country"
                >
                    <option value="BY">Belarus</option>
                    <option value="PL">Poland</option>
                    <option value="LT">Lithuania</option>
                    <option value="LV" disabled>Latvia</option>
                </select>
            </div>

            <div class="form-group">
                <label for="availability">Availability</label>
                <select
                    name="availability"
                    class="form-control"
                    id="availability"
                    v-model="shipment.availability"
                >
                    <option value="AVAILABLE">Available</option>
                    <option value="NOT AVAILABLE">Not available</option>
                </select>
            </div>

            <div class="form-group">
                <label for="delivery_status">Delivery Status</label>
                <select
                    name="delivery_status"
                    class="form-control"
                    id="delivery_status"
                    v-model="shipment.delivery_status"
                >
                    <option value="CREATED">Created</option>
                    <option value="RECEIVED">Information received</option>
                    <option value="IN QUEUE">In queue</option>
                    <option value="IN TRANSIT">In transit</option>
                    <option value="PICKUP">Available for pickup</option>
                    <option value="DELIVERED">Delivered</option>
                    <option value="CANCELED">Canceled</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Update</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            shipment: {
                title: '',
                description: '',
                quantity: 1,
                company: '',
                delivery_country: '',
                availability: '',
                delivery_status: ''
            },
            submitted: false,
            options: [],
            selectedOption: null,
            showErrors: true,
            titleErrors: null,
            quantityErrors: null,
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/shipments/' + this.$route.params.id + '/')
            .then( response => {
                this.shipment = response.data
            });
        this.loadOptions();
    },
    methods: {
        loadOptions: function () {
            axios.get('http://127.0.0.1:8000/api/companies/')
                .then( options => {
                    this.options = options.data;
                    console.log("this.options", this.options)
                });
        },
        checkForm: function (e) {
            if (this.shipment.title && this.shipment.quantity  > 0 && this.shipment.company
                && this.shipment.delivery_country && this.shipment.availability && this.shipment.delivery_status) {
              return true;
            }
            if (!this.shipment.title) {
              this.titleErrors = 'Title is required.';
            }
            if (this.shipment.quantity <= 0) {
              this.quantityErrors = 'Quantity must be greater than zero.';
            }
            e.preventDefault();
        },
        update: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios
                    .put(`http://127.0.0.1:8000/api/shipments/${this.shipment.id}/`,
                        this.shipment
                    )
                    .then(response => {
                        this.$router.push('/shipments');
                    })
            });
        }
    },
}
</script>

<style>
.form-errors, .errors-block {
  color: #dc0c0c;
}
</style>