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
          <v-app-bar-nav-icon color="white"></v-app-bar-nav-icon>

          <v-toolbar-title class="toolbar-title">Wildlife Management System</v-toolbar-title>

          <v-spacer></v-spacer>

          <v-btn icon color="white">
            <v-icon>mdi-export</v-icon>
          </v-btn>
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
    }
  }
}

.container {
  margin: 5rem;
}
</style>