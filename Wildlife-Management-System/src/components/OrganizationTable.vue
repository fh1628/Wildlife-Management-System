<template>
    <div class="main-table-container">
        <div class="filters">
            <v-snackbar
                v-model="snackbar"
                :timeout="timeout"
                >
                {{ text }}

                <template v-slot:actions>
                    <v-btn
                    color="blue"
                    variant="text"
                    @click="snackbar = false"
                    >
                    Close
                    </v-btn>
                </template>
            </v-snackbar>
            <add-dialog @submit="(data)=>addOrganization(data)" :labels="headerLabels" :types="types" text="Organization" class="create-btn" />
        </div>
        <v-card style="padding: 1rem;">
            <TableData :header-labels="headerLabels" :data="tableData" :primary-keys="primaryKeys" :types="types" @updateRow="val => updateOrganization(val)" @deleteRow="val => deleteOrganization(val)" />
        </v-card>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import TableData from './TableData.vue'
import OrganizationService from "../api/OrganizationService"
import AddDialog from './AddDialog.vue'

export default defineComponent({
    components: {
        TableData, AddDialog
    },
    mounted () {
        console.log('mounted')
        this.fetch()
    },
    data() {
        return {
            headerLabels: ['Contact Email', 'Name', 'Mission', 'Website'],
            primaryKeys:['Contact Email'],
            types: ['text','text','text','text'],
            tableData: [],
            snackbar:false,
            text: '',
            timeout: 2000,
        }
    },
    methods: {
        async fetch() {
            OrganizationService.getAllOrganizations()
            .then((response) => {
                this.tableData = response.data
            })
            // .then((response)=> this.tableData = response.data);
            // PopulationService.getColumn({'Climate':''})
            // .then((response) => {
            //     const data = response.data
            //     this.climateItems = [.. Set(data.map(d=>d[0]))]
            //     console.log(this.climateItems)

            // })
            
            
        },
        async addOrganization(dataArray) {
            OrganizationService.addOrganization(dataArray)
            .then(async ()=> {
                await this.fetch(); 
                this.text = 'Organization was added successfully!'
                this.snackbar = true
            })
            .catch((error)=> {
                console.log(error)
                if (error.response.status === 400){
                    const error_msg = error.response.data.error === 'Duplicate' ? "Cannot insert duplicate primary key." : "Foreign key does not exist in table.";
                    alert(`Integrity error! ${error_msg}`)
                }
                else alert('SERVER ERROR!')
            })
        },
        async updateOrganization(arr) {
            console.log('new arr', arr)
            OrganizationService.updateOrganization(arr)
            .then(async (res)=> {
                await this.fetch()
                console.log("FETVHEC")
                this.text = 'Organization was updated successfully!'
                this.snackbar = true
            })
        },
        async deleteOrganization(arr) {
            console.log('new arr', arr)
            OrganizationService.deleteOrganization(arr)
            .then(async (res)=> {
                await this.fetch()
                this.text = 'Organization was deleted successfully!'
                this.snackbar = true
            })
        },
        index(val) {
            return this.headerLabels.indexOf(val)
        },
        getData(val) {
            if (!this.tableData.length) {
                return []
            }
            const idx = this.index(val)
            const dataArray = this.tableData.map((row) => row[idx])
            return [... new Set(dataArray)] 
        },
    }
    
})
</script>
