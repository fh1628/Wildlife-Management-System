<template>
    <v-card>
      <v-tabs
        v-model="tab"
        bg-color="#023020"
        style="color: white"
        align-tabs="center"
      >
        <v-tab width="15%" v-for="(label,key) in labels" :key="key" :value="label">{{label}}</v-tab>
      </v-tabs>

      <v-card-text>
        <v-window v-model="tab">
          <v-window-item class="d-flex justify-center" value="locations">
            <LocationTable v-if="tab === 'locations'" style="width: 80%" />
          </v-window-item>

          <v-window-item value="habitats">
          </v-window-item>

          <v-window-item value="populations">
            Populations Table
          </v-window-item>

          <v-window-item value="species">
            Species Table
          </v-window-item>

          <v-window-item value="researchers">
            Researchers Table
          </v-window-item>

          <v-window-item value="organizations">
            Organizations Table
          </v-window-item>
        </v-window>
      </v-card-text>
  </v-card>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import LocationTable from './LocationTable.vue'

export default defineComponent({
  components: { LocationTable },
  data() {
    return  {
      tab: null,
      labels: ['locations', 'habitats', 'populations', 'species', 'researchers', 'organizations']
    }
  }
})
</script>

<style lang="scss" scoped>
</style>