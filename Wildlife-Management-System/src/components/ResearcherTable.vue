<template>
    <TableData :header-labels="headerLabels" :data="tableData" :primary-keys="primaryKeys" />
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
    }
    
})
</script>
