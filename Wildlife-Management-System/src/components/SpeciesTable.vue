<template>
    <TableData :header-labels="headerLabels" :data="tableData" :primary-keys="primaryKeys" />
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
    }
    
})
</script>
