<template>
    <TableData :header-labels="headerLabels" :data="tableData" :primary-keys="primaryKeys" />
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
            tableData: [],
        }
    }
    
})
</script>
