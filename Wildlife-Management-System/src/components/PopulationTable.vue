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
            <add-dialog @submit="(data)=>addPopulation(data)" :labels="headerLabels" :types="types" text="Population" class="create-btn" />
            <v-card class="filter-container">
                <div class="filter-title">
                    <v-icon icon="mdi-filter-variant"></v-icon>
                    <p class="filter-text">Filter by</p>
                </div>
                <v-divider />
                <div class="filter-options">
                    <v-autocomplete
                        clearable
                        label="Species Scientific Name"
                        variant="underlined"
                        v-model="filterSpecies"
                        :items="speciesItems"
                    ></v-autocomplete>
                    <v-autocomplete
                        clearable
                        label="Habitat Name"
                        variant="underlined"
                        v-model="filterHabitat"
                        :items="habitatItems"
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
                        v-model="sort"
                        label="Size"
                    />
                </div>
            </v-card>
        </div>
        <v-card style="padding: 1rem;">
            <TableData @changeTab="(val)=> $emit('changeTab',val)" :header-labels="headerLabels" :data="tableData" :primary-keys="primaryKeys" :foreign-keys="foreignKeys" :types="types" @updateRow="val => updatePopulation(val)" @deleteRow="val => deletePopulation(val)" />
        </v-card>
    </div>
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import TableData from './TableData.vue'
import PopulationService from "../api/PopulationService"
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
            headerLabels: ['ID', 'Size', 'Trend', 'Growth Rate', 'Density','Habitat Name', 'Species Scientific Name'],
            primaryKeys: ['ID'],
            foreignKeys:[{'Species Scientific Name': 'species'},{'Habitat Name': 'habitats'}],
            types:['number','number','text','number','number','text','text'],
            tableData: [],
            speciesItems: [],
            habitatItems: [],
            filterSpecies: null,
            filterHabitat:  null,
            snackbar:false,
            text: '',
            timeout: 2000,
            sort: false,
        }
    },
    watch: {
        filterObject() {
            console.log("CJHANGED")
            this.fetch()
        },
        sort() {
            this.fetch()
        }
    },
    computed: {
        filterObject(){
            const object = {}
            if (this.filterSpecies) {
                object['SpeciesScientificName'] = this.filterSpecies
            }
            if (this.filterHabitat) {
                object['HabitatName'] = this.filterHabitat
            }
            return object
        } 
    },
    methods: {
         async fetch() {
            (!this.sort ? PopulationService.getFilteredPopulations(this.filterObject): PopulationService.sortPopulation(this.filterObject))
            .then((response) => {
                this.tableData = response.data
            })
            // .then((response)=> this.tableData = response.data);
            PopulationService.getColumn({'SpeciesScientificName':''})
            .then((response) => {
                const data = response.data
                // console.log(data)
                const x = new Set(data.map(d=>d[0]))
                // console.log([...x])

                this.speciesItems = [...new Set(data.map(d=>d[0]))]

            })
            PopulationService.getColumn({'HabitatName':''})
            .then((response) => {
                const data = response.data
                this.habitatItems = [... new Set(data.map(d=>d[0]))]

            })
            // PopulationService.getColumn({'Climate':''})
            // .then((response) => {
            //     const data = response.data
            //     this.climateItems = [.. Set(data.map(d=>d[0]))]
            //     console.log(this.climateItems)

            // })
            
            
        },
        async addPopulation(dataArray) {
            console.log(dataArray)
            PopulationService.addPopulation(dataArray)
            .then(async ()=> {
                await this.fetch(); 
                this.text = 'Population was added successfully!'
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
        async updatePopulation(arr) {
            console.log('new arr', arr)
            PopulationService.updatePopulation(arr)
            .then(async (res)=> {
                await this.fetch()
                this.text = 'Population was updated successfully!'
                this.snackbar = true
            })
        },
        async deletePopulation(arr) {
            console.log('new arr', arr)
            PopulationService.deletePopulation(arr)
            .then(async (res)=> {
                await this.fetch()
                this.text = 'Population was deleted successfully!'
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
