<template>
    <TableData :header-labels="headerLabels" />
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import TableData from './TableData.vue'

export default defineComponent({
    components: {
        TableData,
},
    data() {
        return {
            headerLabels: ['Name', 'Email', 'Phone', 'Expertise', 'Species Scientific Name', 'Population ID']
        }
    }
})
</script>
