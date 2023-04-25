<template>
    <v-card>
      <v-tabs
        v-model="tab"
        bg-color="#023020"
        style="color: white"
        align-tabs="center"
      >
        <v-tab v-for="(label,key) in labels" :key="key" :value="label">{{label}}</v-tab>
      </v-tabs>

      <v-card-text>
        <LocationTable v-if="tab === 'locations'" class="table"/>
        <HabitatTable v-if="tab === 'habitats'" class="table" @changeTab="(val) => {tab = val}" />
        <PopulationTable v-if="tab === 'populations'" class="table" @changeTab="(val) => {tab = val}" />
        <SpeciesTable v-if="tab === 'species'" class="table" />
        <ResearcherTable v-if="tab === 'researchers'" class="table" @changeTab="(val) => {tab = val}" />
        <AssistantResearcher v-if="tab === 'assistant researchers'" class="table" @changeTab="(val)=> {tab = val}" />
        <OrganizationTable v-if="tab === 'organizations'" class="table" />
      </v-card-text>
  </v-card>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import HabitatTable from './HabitatTable.vue'
import LocationTable from './LocationTable.vue'
import PopulationTable from './PopulationTable.vue'
import SpeciesTable from './SpeciesTable.vue'
import ResearcherTable from './ResearcherTable.vue'
import OrganizationTable from './OrganizationTable.vue'
import AssistantResearcher from './AssistantResearcher.vue'

export default defineComponent({
  components: { LocationTable, HabitatTable, PopulationTable, SpeciesTable, ResearcherTable, OrganizationTable, AssistantResearcher },
  data() {
    return  {
      tab: 'locations',
      labels: ['locations', 'habitats', 'populations', 'species', 'researchers', 'assistant researchers' ,  'organizations']
    }
  }
})
</script>

<style lang="scss" scoped>
.table {
  margin: 2rem;
}
</style>