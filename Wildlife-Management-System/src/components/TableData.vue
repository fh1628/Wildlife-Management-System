<template>
  <v-table
    fixed-header
    height="30rem"
    hover
  >
    <thead>
      <tr>
        <th class="text-left" v-for="(header,key) in headerLabels" :key="key">
          {{header}}
        </th>
        <th />
        <th />
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="(row,key) in data"
        :key="key"
      >
        <td @click="()=>test(row)" v-for="(column, idx) in row" :key="idx">{{ column ? column : 'NULL' }}</td>
        <td><v-btn color="blue" variant="tonal" icon="mdi-pencil" size="small" /></td>
        <td><v-btn color="red" variant="tonal" icon="mdi-delete" size="small" /></td>
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
    },
    methods: {
      test(column) {
        console.log(column)
      }
    }
})
</script>
