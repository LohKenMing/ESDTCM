// import axios from 'axios';
const PATIENT_URL = 'http://127.0.0.1:5001/patient';
const SESSION_URL = 'http://127.0.0.1:5001/patient';

const app = Vue.createApp({ 
    data() { 
        return { 
            patients: [],
        };
    }, 
    mounted() {
        axios.get('http://127.0.0.1:5001/patient')
          .then(response => {
            this.patients = response.data.data.patient;
            console.log(this.patients)
            // console.log(this.patients.patient[0])
          })
          .catch(error => {
            console.log(error);
          });
    },
});

app.component('patientinfo', { 
    props: ['patients'],
    template: `
    <table class='table table-white table-hover table-bordered no-more-tables'>
        <thead>
            <tr>
                <th scope='col-1'>ID</th>
                <th postscope='col'>Name</th>
                <th scope='col'>Email</th>
                <th scope='col'>Phone</th>
                <th scope='col'>Allergies</th>
            </tr>
        </thead>
        <tbody class='table-group-divider'>
            <tr v-for="patient in patients">
                <td data-title="ID">{{ patient._id }}</td>
                <td data-title="Name">{{ patient.patientName }}</td>
                <td data-title="Email">{{ patient.email }}</td>
                <td data-title="Phone">{{ patient.phoneNumber }}</td>
                <td data-title="Allergies">{{ patient.allergies }}</td>
            </tr>
        </tbody>
    </table>
    `
});

app.component('pastsession', { 
    template: `
    <table class='table table-white table-hover table-bordered no-more-tables'>
        <thead>
            <tr>
                <th scope='col-1'>Date</th>
                <th scope='col'>Order ID</th>
                <th scope='col'>3</th>
                <th scope='col'>Price</th>
                <th scope='col'>Status</th>
            </tr>
        </thead>
        <tbody class='table-group-divider'>
            <tr>
                <td data-title="Date">08/03/23</td>
                <td data-title="Order ID">asd</td>
                <td >asdasdasdasdasdasdasadasddasddasddasddasdasdada</td>
                <td data-title="Price">$100</td>
                <td data-title="Status"> <button type='button' class='btn btn-primary'>Make Payment</button> </td>
            </tr>
            
            <tr>
                <th scope='row'></th>
                <td></td>
                <td></td>
            </tr>
        </tbody>
    </table>
    `
});

const vm = app.mount('#app');