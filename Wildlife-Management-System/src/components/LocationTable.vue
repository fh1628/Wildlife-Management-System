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
            <add-dialog @submit="(data)=>addLocation(data)" :labels="headerLabels" :types="types" class="create-btn" />
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
                        :items="getData('Type')"
                    ></v-autocomplete>
                    <v-autocomplete
                        label="Country"
                        variant="underlined"
                        :items="getData('Country')"
                    ></v-autocomplete>
                    <v-autocomplete
                        label="Climate"
                        variant="underlined"
                        :items="getData('Climate')"
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
                        label="Elevation"
                    />
                </div>
            </v-card>
        </div>
        <v-card style="padding: 1rem;">
            <TableData :header-labels="headerLabels" :data="tableData" :primary-keys="primaryKeys" @updateRow="(val)=>updateLocation(val)" />
        </v-card>
    </div>
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import TableData from './TableData.vue'
import LocationService from "../api/LocationService"
import AddDialog from './AddDialog.vue'

export default defineComponent({
    components: {
        TableData,
        AddDialog,
    },
    mounted () {
        console.log('mounted')
        LocationService.getAllLocations()
        .then((response) => {
            this.tableData = response.data
        });
    },
    data() {
        return {
            headerLabels: ['Latitude', 'Longitude', 'Name', 'Type', 'Country','Area', 'Climate',  'Elevation'],
            types:['number','number','text','text','text','number','text','number'],
            primaryKeys: ['Latitude', 'Longitude'],
            tableData: [],
            snackbar:false,
            text: '',
            timeout: 2000,
        }
    },
    methods: {
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
        async fetchData() {
            return LocationService.getAllLocations()
            .then((response) => {
                this.tableData = response.data
            });
        },
        async addLocation(dataArray) {
            LocationService.addLocation(dataArray)
            .then(async ()=> {
                await this.fetchData(); 
                this.text = 'Location was added successfully!'
                this.snackbar = true
            })
            .catch(()=> {
                alert('Cannot add duplicate primary key!')
            })
        },
        async updateLocation(arr) {
            console.log('new arr', arr)
            LocationService.updateLocation(arr)
            .then((res)=> {
                console.log(res.data)
                this.text = 'Location was updated successfully!'
                this.snackbar = true
            })
        }
    },
    computed: {
    }
    
})
</script>

<style lang="scss">
.main-table-container {
    display: flex;
    align-items: center;
    .filters {
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 17%;
        margin-right: 2rem;
        .create-btn {
            margin-bottom: 2rem;
        }
        .filter-container{
            margin-bottom: 2rem;
            .filter-title{
                display: flex;
                align-items: center;
                padding: 0.5rem;
                .filter-text {
                    font-size: 1rem;
                    margin-left: 0.5rem;
                }
            }
            .filter-options {
                padding: 1rem;
            }
            .sort-options {
                padding-top: 1rem;
                padding-inline: 1rem;
            }
        }   
}
}
</style>