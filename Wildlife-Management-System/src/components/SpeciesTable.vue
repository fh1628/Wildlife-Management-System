<template>
    <div class="main-table-container">
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
                        label="Conservation Status"
                        variant="underlined"
                        :items="getData('Conservation Status')"
                    ></v-autocomplete>
                    <v-autocomplete
                        label="Geographic Distribution"
                        variant="underlined"
                        :items="getData('Geographic Distribution')"
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
            <TableData :header-labels="headerLabels" :data="tableData" :primary-keys="primaryKeys" />
        </v-card>
    </div>
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import TableData from './TableData.vue'
import SpeciesService from "../api/SpeciesService"

export default defineComponent({
    components: {
        TableData,
    },
    mounted () {
        console.log('mounted')
        SpeciesService.getAllSpecies()
        .then((response) => {
            this.tableData = response.data
        });
    },
    data() {
        return {
            headerLabels: ['Scientific Name', 'Common Name', 'Conservation Status', 'Geographic Distribution'],
            primaryKeys: ['Scientific Name'],
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
    }
    
})
</script>
