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
                        label="Type"
                        variant="underlined"
                        :items="['University','Company']"
                    ></v-autocomplete>
                    <v-autocomplete
                        label="Expertise"
                        variant="underlined"
                        :items="getData('Expertise')"
                    ></v-autocomplete>
                    <v-autocomplete
                        label="Species Scientific Name"
                        variant="underlined"
                        :items="getData('Species Scientific Name')"
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
            <TableData :header-labels="headerLabels" :data="tableData" :primary-keys="primaryKeys" />
        </v-card>
    </div>
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import TableData from './TableData.vue'
import ResearcherService from "../api/ResearcherService"

export default defineComponent({
    components: {
        TableData,
    },
    mounted () {
        console.log('mounted')
        ResearcherService.getAllResearchers()
        .then((response) => {
            this.tableData = response.data
        });
    },
    data() {
        return {
            headerLabels: ['Name', 'Email', 'Phone Number', 'Expertise', 'Species Scientific Name', 'Population ID'],
            primaryKeys:['Email'],
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
