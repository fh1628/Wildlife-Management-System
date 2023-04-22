<template>
  <v-table
    fixed-header
    height="300px"
  >
    <thead>
      <tr>
        <th class="text-left" v-for="(header,key) in headerLabels" :key="key">
          {{header}}
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="item in data"
        :key="item.name"
      >
        <td>{{ item.name }}</td>
        <td>{{ item.calories }}</td>
      </tr>
    </tbody>
  </v-table>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    props: {
        headerLabels: {
            type: Array,
            required: true,
        },
        data: {
            type: Array,
            required: true,
        }
    },
    data() {
    }
})
</script>
