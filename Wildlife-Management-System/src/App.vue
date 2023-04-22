<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import CustomTabs from './components/CustomTabs.vue'
// import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
    <div class="main">
      <div class="header">
        <v-toolbar
        color="#023020"
        class="toolbar"
        >
          <v-icon color="white" icon="mdi-forest" style="margin-left: 2rem; margin-right: 0.5rem;"></v-icon>

          <v-toolbar-title class="toolbar-title">Wildlife Management System</v-toolbar-title>


         
        </v-toolbar>
      </div>
      <div class="container">
        <CustomTabs />
      </div>
    </div>
</template>

  
<style lang="scss" scoped>
.header {
  margin-bottom: 3rem;
  .toolbar {
    .toolbar-title {
      color: white;
      font-weight: 500;
    }
  }
}

.container {
  margin: 5rem;
}
</style>