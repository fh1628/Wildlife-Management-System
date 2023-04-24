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
                        label="Species Scientific Name"
                        variant="underlined"
                        :items="getData('Species Scientific Name')"
                    ></v-autocomplete>
                    <v-autocomplete
                        label="Habitat Name"
                        variant="underlined"
                        :items="getData('Habitat Name')"
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
                        label="Size"
                    />
                    <!-- <v-checkbox
                        label="Trend"
                    /> -->
                </div>
            </v-card>
        </div>
        <v-card style="padding: 1rem;">
            <TableData @changeTab="(val)=> $emit('changeTab',val)" :header-labels="headerLabels" :data="tableData" :primary-keys="primaryKeys" :foreign-keys="foreignKeys" />
        </v-card>
    </div>
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import TableData from './TableData.vue'
import PopulationService from "../api/PopulationService"

export default defineComponent({
    components: {
        TableData,
    },
    mounted () {
        console.log('mounted')
        PopulationService.getAllPopulations()
        .then((response) => {
            this.tableData = response.data
        });
    },
    data() {
        return {
            headerLabels: ['ID', 'Size', 'Trend', 'Growth Rate', 'Density','Habitat Name', 'Species Scientific Name'],
            primaryKeys: ['ID'],
            foreignKeys:[{'Species Scientific Name': 'species'},{'Habitat Name': 'habitats'}],
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
