<template>
    <div class="pt-5 needs-validation">
        <form @submit="checkForm" @submit.prevent="create" method="post">
            <div class="form-group">
                <label class="form-label">Name</label>
                <input
                    type="text"
                    class="form-control"
                    id="name"
                    v-model="company.name"
                    v-validate="'required'"
                    name="name"
                    placeholder="Enter name"
                >
                <div class="errors-block pt-1 text-md-left">
                  <p class="form-errors" v-if="nameErrors && nameErrors.length">
                    {{ nameErrors }}
                  </p>
                </div>
            </div>

            <div class="form-group">
                <label for="description">Description</label>
                <input
                    type="text"
                    class="form-control"
                    id="description"
                    v-model="company.description"
                    name="description"
                    placeholder="Enter description"
                >
            </div>

            <div class="form-group">
                <label for="country">Country</label>
                <select
                    name="country"
                    class="form-control"
                    v-validate="'required'"
                    id="country"
                    v-model="company.country"
                >
                    <option value="BY">Belarus</option>
                    <option value="PL">Poland</option>
                    <option value="LT">Lithuania</option>
                    <option value="LV">Latvia</option>
                </select>
                <div class="errors-block pt-1 text-md-left">
                  <p class="form-errors" v-if="countryErrors && countryErrors.length">
                    {{ countryErrors }}
                  </p>
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Create</button>
        </form>
        <div class="errors-block pt-4 text-md-center">
          <p v-if="errors && errors.length">
              {{ errors }}
          </p>
        </div>
    </div>

</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            company: {
                name: '',
                description: '',
                country: '',
            },
            submitted: false,
            showErrors: true,
            errors: null,
            nameErrors: null,
            countryErrors: null,
        }
    },
    methods: {
        checkForm: function (e) {
            if (this.company.name && this.company.country) {
              return true;
            }
            if (!this.company.name) {
              this.nameErrors = 'Name is required.';
            }
            if (!this.company.country) {
              console.log(e)
              this.countryErrors = 'Country is required.';
            }
            e.preventDefault();

        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios
                  .post('http://127.0.0.1:8000/api/companies/',
                      this.company
                  )
                  .then(response => {
                      this.$router.push('/companies');
                  })
                  .catch(error => {
                    console.log(error.response.data);
                    console.log(error.response.status);
                    const response = error.response.data.name[0];
                    this.errors = response.charAt(0).toUpperCase() + response.slice(1);
                  })
            });
        },
    },
}
</script>

<style>
.form-errors, .errors-block {
  color: #dc0c0c;
}
</style>