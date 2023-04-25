<template>
  <v-table
    fixed-header
    height="30rem"
    hover
    id="table"
  >
    <thead>
      <tr>
        <th :class="['text-left','font-weight-bold', {'primary-key': isPrimaryKey(header)}, {'foreign-key': isForeignKey(header)} ]" v-for="(header,key) in headerLabels" :key="key" @click="()=>changeTab(header)">
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
      
        <td @click="()=>test(row)" v-for="(column, idx) in row" :key="idx">
          <v-text-field v-if="selectedRow === key && !isPrimaryKey(idx)" v-model="row[idx]" :type="types[idx]" :label="headerLabels[idx]" variant="underlined" />
          <p v-else>{{ columnName(column) }}</p>
          </td>
        <td>
          <v-btn v-if="selectedRow === key" color="green" variant="tonal" icon="mdi-check" size="small" @click="()=> {
            updateRow([...row]);
            selectedRow = null
            }" />
          <v-btn v-else color="blue" variant="tonal" icon="mdi-pencil" size="small" @click="()=> {selectedRow = key}" :disabled="selectedRow !== null" />
        </td>
        <td><v-btn color="red" variant="tonal" icon="mdi-delete" size="small" :disabled="selectedRow !== null && selectedRow !== key" @click="deleteRow([...row])" /></td>
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
        primaryKeys: {
            type: Array,
            required: false,
        },
        foreignKeys: {
            type: Array,
            required: false,
        },
        data: {
            type: Array,
            required: true,
        },
        types: {
          type: Array,
          required: false,
        }
    },
    data() {
      return {
        selectedRow: null,
      }
    },
    methods: {
      test(column) {
        console.log(column)
      },
      updateRow(dataArray) {
        this.$emit('updateRow', dataArray)
      },
      deleteRow(dataArray) {
        this.$emit('deleteRow', dataArray)
      },
      isPrimaryKey(value) {
        return this.primaryKeys.includes(value) || this.primaryIndex.includes(value)
      },
      columnName(col) {
        return col ? col:'NULL'
      },
      index(val) {
        return this.primaryKeys.indexOf(val);
      },
      changeTab(key) {
        this.$emit('changeTab', this.findTabToChange(key));
      },
      findTabToChange(key) {
        if (!this.isForeignKey(key)) return;
        const tempObj = this.foreignKeys.find((obj) => (obj[key]))
        return tempObj[key]
      },
      isForeignKey(key) {
        if (!this.foreignKeys) {
          return false;
        }
        const search = this.foreignKeys.find((obj) => obj[key])
        return search
      }
    },
    computed: {
      primaryIndex() {
        return this.primaryKeys.map((val)=>this.index(val))
      }
    }
})
</script>

<style lang="scss" scoped>
#table {
  thead {
    .primary-key {
      font-weight: 600;
      color: red;
    } 
    .foreign-key {
      font-style: italic;
      color: blue;
      cursor:pointer;
    }
}
}
</style>