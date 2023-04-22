<template>
    <TableData :header-labels="headerLabels" :data="tableData" :primary-keys="[]" />
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import TableData from './TableData.vue'
import OrganizationService from "../api/OrganizationService"

export default defineComponent({
    components: {
        TableData,
    },
    mounted () {
        console.log('mounted')
        OrganizationService.getAllOrganizations()
        .then((response) => {
            this.tableData = response.data
        });
    },
    data() {
        return {
            headerLabels: ['Contact Email', 'Name', 'Mission', 'Website'],
            tableData: [],
        }
    }
    
})
</script>
