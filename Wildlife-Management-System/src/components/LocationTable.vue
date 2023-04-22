<template>
<div class="main">
    <div class="filters">
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
        <TableData :header-labels="headerLabels" :data="tableData" :primary-keys="primaryKeys" />
    </v-card>
</div>
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import TableData from './TableData.vue'
import LocationService from "../api/LocationService"

export default defineComponent({
    components: {
        TableData,
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
            primaryKeys: ['Latitude', 'Longitude'],
            tableData: [],
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
    },
    computed: {
    }
    
})
</script>

<style lang="scss" scoped>
.main {
    display: flex;
    align-items: center;
    .filters {
        width: 15%;
        margin-right: 2rem;
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