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
            <add-dialog @submit="(data)=>addHabitat(data)" :labels="headerLabels" :types="types" text="Habitat" class="create-btn" />
            <v-card class="filter-container">
                <div class="filter-title">
                    <v-icon icon="mdi-filter-variant"></v-icon>
                    <p class="filter-text">Filter by</p>
                </div>
                <v-divider />
                <div class="filter-options">
                    <v-autocomplete
                        clearable
                        width="80%"
                        label="Type"
                        variant="underlined"
                        v-model="filterType"
                        :items="typeItems"
                    ></v-autocomplete>
                    <v-autocomplete
                        clearable
                        label="Conservation Status"
                        v-model="filterStatus"
                        variant="underlined"
                        :items="statusItems"
                    ></v-autocomplete>
                </div>
            </v-card>
            <v-card class="filter-container">
                <div class="filter-title">
                    <v-icon icon="mdi-sort"></v-icon>
                    <p class="filter-text">Sort by</p>
                </div>
                <v-divider />
                <div class="sort-options">
                    <v-checkbox
                        label="Degradation Level"
                    />
                </div>
            </v-card>
        </div>
        <v-card style="padding: 1rem;">
            <TableData @changeTab="(val)=> $emit('changeTab',val)" :header-labels="headerLabels" :data="tableData" :primary-keys="primaryKeys" :foreign-keys="foreignKeys" :types="types" @updateRow="(val)=>updateHabitat(val)" @deleteRow="(val)=>deleteHabitat(val)"/>
        </v-card>
    </div>
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import TableData from './TableData.vue'
import HabitatService from "../api/HabitatService"
import AddDialog from './AddDialog.vue'

export default defineComponent({
    components: {
        TableData,
        AddDialog
    },
    mounted () {
        this.fetch()
    },
    data() {
        return {
            headerLabels: ['Name', 'Type', 'Conservation Status', 'Degradation Level', 'Latitude','Longitude'],
            types:['text','text','text','text','number','number'],
            primaryKeys: ['Name'],
            foreignKeys: [{'Latitude': 'locations'}, {'Longitude': 'locations'}],
            tableData: [],
            filterType: null,
            filterStatus: null,
            typeItems: [],
            statusItems: [],
            snackbar:false,
            text: '',
            timeout: 2000,
        }
    },
    watch: {
        filterObject(){
            this.fetch()
        }
    },
    methods: {
        async fetch() {
            HabitatService.getFilteredHabitats(this.filterObject)
            .then((response) => {
                this.tableData = response.data
            })
            // .then((response)=> this.tableData = response.data);
            HabitatService.getColumn({'HabitatType':''})
            .then((response) => {
                const data = response.data
                // console.log(data)
                const x = new Set(data.map(d=>d[0]))
                // console.log([...x])

                this.typeItems = [...new Set(data.map(d=>d[0]))]

            })
            HabitatService.getColumn({'ConservationStatus':''})
            .then((response) => {
                const data = response.data
                this.statusItems = [... new Set(data.map(d=>d[0]))]

            })
            // LocationService.getColumn({'Climate':''})
            // .then((response) => {
            //     const data = response.data
            //     this.climateItems = [.. Set(data.map(d=>d[0]))]
            //     console.log(this.climateItems)

            // })
            
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
        async updateHabitat(arr) {
            console.log('new arr', arr)
            HabitatService.updateHabitat(arr)
            .then(async (res)=> {
                await this.fetch()
                this.text = 'Habitat was updated successfully!'
                this.snackbar = true
            })
        },
        async deleteHabitat(arr) {
            console.log('new arr', arr)
            HabitatService.deleteHabitat(arr)
            .then(async (res)=> {
                await this.fetch()
                this.text = 'Habitat was deleted successfully!'
                this.snackbar = true
            })
        },
        async addHabitat(dataArray) {
            HabitatService.addHabitat(dataArray)
            .then(async ()=> {
                await this.fetch(); 
                this.text = 'Habitat was added successfully!'
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
    },
    computed: {
        filterObject(){
            const object = {}
            if (this.filterType) {
                object['HabitatType'] = this.filterType
            }
            if (this.filterStatus) {
                object['ConservationStatus'] = this.filterStatus
            }
            return object
        } 
    }
    
})
</script>
