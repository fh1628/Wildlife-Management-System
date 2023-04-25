<template>
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="auto"
    >
      <template v-slot:activator="{ props }">
        <v-btn
          color="green"
          v-bind="props"
        >
          Add {{text}}
        </v-btn>
      </template>

      <v-card width="700" height="600">
        <v-card-text class="text-h5 text-center">
          Create {{ text}}
          <v-sheet width="80%" class="mx-auto my-10">
            <v-form @submit.prevent>
              <v-text-field
                v-for="(label,key) in labels"
                :key="key"
                 v-model="dataArray[key]"
                :type="types[key]"
                :label="label"
                :rules="rules"
                clearable
                dense
              ></v-text-field>
              <v-btn type="submit" block class="mt-2"
               @click="()=> {
                  $emit('submit',dataArray)
                }">Submit</v-btn>
            </v-form>
          </v-sheet>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props:{ 
    labels: {
      type: Array,
      required: false,
    },
    types: {
      type: Array,
      required: false,
    },
    text: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
      dialog: false,
      dataArray: this.labels.map((val)=>null)
    }
  }
})
</script>
