<template>
    <TableData :header-labels="headerLabels" :data="tableData" :primary-keys="primaryKeys" />
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import TableData from './TableData.vue'
import HabitatService from "../api/HabitatService"

export default defineComponent({
    components: {
        TableData,
    },
    mounted () {
        console.log('mounted')
        HabitatService.getAllHabitats()
        .then((response) => {
            this.tableData = response.data
        });
    },
    data() {
        return {
            headerLabels: ['Name', 'Type', 'Conservation Status', 'Degradation Level', 'Latitude','Longitude'],
            primaryKeys: ['Name'],
            tableData: [],
        }
    }
    
})
</script>
