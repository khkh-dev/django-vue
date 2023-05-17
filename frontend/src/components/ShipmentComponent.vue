<template>
    <div class="container">
    <div class="row">
    <div class="col-12">
      <table class="table table-bordered">
        <thead>
          <tr>
            <th scope="col">Id</th>
            <th scope="col">Title</th>
            <th scope="col">Description</th>
            <th scope="col">Quantity</th>
            <th scope="col">Delivery Country</th>
            <th scope="col">Availability</th>
            <th scope="col">Delivery Status</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody v-if="shipments && shipments.length">
          <tr v-for="shipment of shipments" v-bind:key="shipment.id">
            <td>{{ shipment.id }}</td>
            <td>{{ shipment.title }}</td>
            <td>{{ shipment.description }}</td>
            <td>{{ shipment.quantity }}</td>
            <td>{{ shipment.delivery_country }}</td>
            <td>{{ shipment.availability }}</td>
            <td>{{ shipment.delivery_status }}</td>
            <td class="td-actions">
                <router-link :to="{name: 'shipment-edit', params: { id: shipment.id }}" class="btn btn-success"><i class="fas fa-edit"></i></router-link>
                <button class="btn btn-danger" v-on:click="deleteShipment(shipment)"><i class="far fa-trash-alt"></i></button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="errors-block pt-4 text-md-left">
        <p class="message-block" v-if="errors && errors.length">
            {{ errors }}
        </p>
      </div>
      <p class="message-block" v-if="shipments.length == 0">No shipments</p>
      <div class="block-add">
        <router-link :to="{name: 'shipment-create'}" class="btn btn-primary rounded-0 btn-block">Create new shipment</router-link>
      </div>
    </div>
    </div>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    data() {
        return {
            shipments: [],
            showErrors: true,
            errors: null,
        }
    },
    created() {
        this.all();
    },
    methods: {
        all: function () {
            axios.get('http://127.0.0.1:8000/api/shipments/')
                .then( response => {
                    this.shipments = response.data
                });
        },
        deleteShipment: function(shipment) {
            if (confirm('Delete ' + shipment.title)) {
                axios.delete(`http://127.0.0.1:8000/api/shipments/${shipment.id}/`)
                    .then( response => {
                        this.all();
                    })
                    .catch(error => {
                      console.log(error.response.data);
                      console.log(error.response.status);
                      this.errors = "Shipment not found."
                    });
            }
        },
    },
}
</script>

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

td.td-actions {
  border: 0;
}

.td-actions {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.btn-block {
  display: block;
  width: 20%;
}

.block-add {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
}

.errors-block {
  color: #dc0c0c;
}

.message-block {
  text-align: center;
}
</style>