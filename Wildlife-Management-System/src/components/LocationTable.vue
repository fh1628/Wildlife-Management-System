<template>
    <TableData :header-labels="headerLabels" :data="tableData" />
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
            tableData: [],
        }
    }
    
})
</script>
