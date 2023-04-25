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
            <add-dialog @submit="(data)=>addResearcher(data)" :labels="headerLabels" :types="types" text="Researcher" class="create-btn" />
            <v-card class="filter-container">
                <div class="filter-title">
                    <v-icon icon="mdi-filter-variant"></v-icon>
                    <p class="filter-text">Filter by</p>
                </div>
                <v-divider />
                <div class="filter-options">
                    <v-autocomplete
                        width="80%"
                        label="Type"
                        variant="underlined"
                        clearable
                        :items="['University','Company']"
                    ></v-autocomplete>
                    <v-autocomplete
                        label="Expertise"
                        variant="underlined"
                        clearable
                        v-model="filterExpertise"
                        :items="expertiseItems"
                    ></v-autocomplete>
                    <v-autocomplete
                        label="Species Scientific Name"
                        variant="underlined"
                        clearable
                        v-model="filterSpecies"
                        :items="speciesItems"
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
            headerLabels: ['Name', 'Email', 'Phone Number', 'Expertise', 'Species Scientific Name', 'Population ID'],
            types: ['text','email','number','text','text','number'],
            primaryKeys:['Email'],
            foreignKeys:[{'Species Scientific Name': 'species'},{'Population ID': 'populations'}],
            tableData: [],
            filterExpertise: null,
            filterSpecies: null,
            expertiseItems: [],
            speciesItems: [],
            snackbar:false,
            text: '',
            timeout: 2000,
        }
    },
    watch: {
        filterObject() {
            this.fetch()
        },
    },
    computed: {
        filterObject(){
            const object = {}
            if (this.filterExpertise) {
                object['Expertise'] = this.filterExpertise
            }
            if (this.filterSpecies) {
                object['SpeciesScientificName'] = this.filterSpecies
            }
            return object
        } 
    },
    methods: {
        async fetch() {
            ResearcherService.getFilteredResearchers(this.filterObject)
            .then((response) => {
                this.tableData = response.data
            })
            // .then((response)=> this.tableData = response.data);
            ResearcherService.getColumn({'Expertise':''})
            .then((response) => {
                const data = response.data
                // console.log(data)
                const x = new Set(data.map(d=>d[0]))
                // console.log([...x])

                this.expertiseItems = [...new Set(data.map(d=>d[0]))]

            })
            ResearcherService.getColumn({'SpeciesScientificName':''})
            .then((response) => {
                const data = response.data
                this.speciesItems = [... new Set(data.map(d=>d[0]))]

            })
            // PopulationService.getColumn({'Climate':''})
            // .then((response) => {
            //     const data = response.data
            //     this.climateItems = [.. Set(data.map(d=>d[0]))]
            //     console.log(this.climateItems)

            // })
            
            
        },
        async addResearcher(dataArray) {
            ResearcherService.addResearcher(dataArray)
            .then(async ()=> {
                await this.fetch(); 
                this.text = 'Researcher was added successfully!'
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
            ResearcherService.updateResearcher(arr)
            .then(async (res)=> {
                await this.fetch()
                console.log("FETVHEC")
                this.text = 'Researcher was updated successfully!'
                this.snackbar = true
            })
        },
        async deleteResearcher(arr) {
            console.log('new arr', arr)
            ResearcherService.deleteResearcher(arr)
            .then(async (res)=> {
                await this.fetch()
                this.text = 'Researcher was deleted successfully!'
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
