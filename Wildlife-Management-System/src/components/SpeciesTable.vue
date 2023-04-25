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
            <add-dialog @submit="(data)=>addSpecies(data)" :labels="headerLabels" :types="types" text="Species" class="create-btn" />
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
                        label="Location"
                        variant="underlined"
                        v-model="filterLocation"
                        :items="locationItems"
                    ></v-autocomplete>
                    <v-autocomplete
                        clearable
                        width="80%"
                        label="Conservation Status"
                        variant="underlined"
                        v-model="filterStatus"
                        :items="statusItems"
                    ></v-autocomplete>
                    <v-autocomplete
                        clearable
                        label="Geographic Distribution"
                        variant="underlined"
                        v-model="filterDist"
                        :items="distItems"
                    ></v-autocomplete>
                    <!-- <v-autocomplete
                        label="Climate"
                        variant="underlined"
                        :items="getData('Climate')"
                    ></v-autocomplete> -->
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
            <TableData :header-labels="headerLabels" :data="tableData" :primary-keys="primaryKeys" :types="types" @updateRow="val=>updateSpecies(val)" @deleteRow="val=>deleteSpecies(val)" />
        </v-card>
    </div>
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import TableData from './TableData.vue'
import SpeciesService from "../api/SpeciesService"
import AddDialog from './AddDialog.vue'
import LocationService from '../api/LocationService'

export default defineComponent({
    components: {
        TableData, AddDialog
    },
    mounted () {
        this.fetch()
    },
    data() {
        return {
            headerLabels: ['Scientific Name', 'Common Name', 'Conservation Status', 'Geographic Distribution'],
            types:['text','text','text','text'],
            primaryKeys: ['Scientific Name'],
            tableData: [],
            filterStatus: null,
            filterDist: null,
            statusItems: [],
            locationItems: [],
            filterLocation: null,
            filterItems: [],
            snackbar:false,
            text: '',
            timeout: 2000,
        }
    },
    watch: {
        filterObject() {
            console.log("CJHANGED")
            this.fetch()
        },
    },
    computed: {
        filterObject(){
            const object = {}
            if (this.filterStatus) {
                object['ConservationStatus'] = this.filterStatus
            }
            if (this.filterDist) {
                object['GeographicDistribution'] = this.filterDist
            }
            if (this.filterLocation) {
                console.log('ok')
            }
            return object
        } 
    },
    methods: {
        async fetch() {
            if (!this.filterLocation) SpeciesService.getFilteredSpecies(this.filterObject)
            .then((response) => {
                this.tableData = response.data
            })
            // .then((response)=> this.tableData = response.data);
            SpeciesService.getColumn({'ConservationStatus':''})
            .then((response) => {
                const data = response.data
                // console.log(data)
                const x = new Set(data.map(d=>d[0]))
                // console.log([...x])

                this.statusItems = [...new Set(data.map(d=>d[0]))]

            })
            SpeciesService.getColumn({'GeographicDistribution':''})
            .then((response) => {
                const data = response.data
                this.distItems = [... new Set(data.map(d=>d[0]))]

            })

            LocationService.getColumn({'LocationName':''})
            .then((resp) => {
                const data = resp.data
                this.locationItems = [...new Set(data.map(d=>d[0]))]
            })
            
            if (this.filterLocation){
                SpeciesService.getByPopulation(this.filterLocation)
                .then(resp => this.tableData = resp.data)
            }
            // PopulationService.getColumn({'Climate':''})
            // .then((response) => {
            //     const data = response.data
            //     this.climateItems = [.. Set(data.map(d=>d[0]))]
            //     console.log(this.climateItems)

            // })
            
            
        },
        async addSpecies(dataArray) {
            SpeciesService.addSpecies(dataArray)
            .then(async ()=> {
                await this.fetch(); 
                this.text = 'Species was added successfully!'
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
        async updateSpecies(arr) {
            console.log('new arr', arr)
            SpeciesService.updateSpecies(arr)
            .then(async (res)=> {
                await this.fetch()
                console.log("FETVHEC")
                this.text = 'Species was updated successfully!'
                this.snackbar = true
            })
        },
        async deleteSpecies(arr) {
            console.log('new arr', arr)
            SpeciesService.deleteSpecies(arr)
            .then(async (res)=> {
                await this.fetch()
                this.text = 'Species was deleted successfully!'
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
