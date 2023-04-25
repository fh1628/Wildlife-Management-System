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
            <add-dialog @submit="(data)=>addResearcher(data)" :labels="headerLabels" :types="types" text="Assistant" class="create-btn" />
            <v-card class="filter-container">
                <div class="filter-title">
                    <v-icon icon="mdi-filter-variant"></v-icon>
                    <p class="filter-text">Filter by</p>
                </div>
                <v-divider />
                <div class="filter-options">
                    <v-autocomplete
                        width="80%"
                        label="Reports to"
                        variant="underlined"
                        clearable
                        v-model="filterResearcher"
                        :items="items"
                    ></v-autocomplete>
                </div>
            </v-card>
            <!-- <v-card class="filter-container">
                <div class="filter-title">
                    <v-icon icon="mdi-sort"></v-icon>
                    <p class="filter-text">Sort by</p>
                </div>
                <v-divider />
                <div class="sort-options">
                    <v-checkbox
                        label="Elevation"
                    />
                </div>
            </v-card> -->
        </div>
        <v-card style="padding: 1rem;">
            <TableData @changeTab="(val)=>$emit('changeTab',val)" :header-labels="headerLabels" :data="tableData" :primary-keys="primaryKeys" :foreign-keys="foreignKeys" :types="types" @updateRow="val=>updateResearcher(val)" @deleteRow="val=>deleteResearcher(val)" />
        </v-card>
    </div>
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import TableData from './TableData.vue'
import ResearcherService from "../api/ResearcherService"
import AddDialog from './AddDialog.vue'
import AssistantService from '../api/AssistantService'

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
            headerLabels: ['Name', 'Email', 'Reports to'],
            types: ['text','email','email'],
            primaryKeys:['Email', 'Reports to'],
            foreignKeys:[{'Reports to': 'researchers'}],
            tableData: [],
            filterResearcher: null,
            items: [],
            snackbar:false,
            text: '',
            timeout: 2000,
        }
    },
    watch: {
        filterObject() {
            console.log('CHANGED')
            this.fetch()
        },
    },
    computed: {
        filterObject(){
            const object = {}
            if (this.filterResearcher) {
                object['ResearcherEmail'] = this.filterResearcher
            }
            return object
        } 
    },
    methods: {
        async fetch() {
            AssistantService.getFilteredResearchers(this.filterObject)
            .then((response) => {
                this.tableData = response.data
            })
            // .then((response)=> this.tableData = response.data);
           AssistantService.getColumn({'ResearcherEmail':''})
            .then((response) => {
                const data = response.data
                // console.log(data)
                const x = new Set(data.map(d=>d[0]))
                // console.log([...x])

                this.items = [...new Set(data.map(d=>d[0]))]

            })
            // PopulationService.getColumn({'Climate':''})
            // .then((response) => {
            //     const data = response.data
            //     this.climateItems = [.. Set(data.map(d=>d[0]))]
            //     console.log(this.climateItems)

            // })
            
            
        },
        async addResearcher(dataArray) {
            AssistantService.addResearcher(dataArray)
            .then(async ()=> {
                await this.fetch(); 
                this.text = 'Assistant was added successfully!'
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
        async updateResearcher(arr) {
            console.log('new arr', arr)
            AssistantService.updateResearcher(arr)
            .then(async (res)=> {
                await this.fetch()
                console.log("FETVHEC")
                this.text = 'Assistant was updated successfully!'
                this.snackbar = true
            })
        },
        async deleteResearcher(arr) {
            console.log('new arr', arr)
            AssistantService.deleteResearcher(arr)
            .then(async (res)=> {
                await this.fetch()
                this.text = 'Assistant was deleted successfully!'
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
