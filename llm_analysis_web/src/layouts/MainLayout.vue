<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>

        <q-toolbar-title>
          Langauge Learning Model Analysis
        </q-toolbar-title>

        <div>LLM v1.0</div>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>

defineOptions({
  name: 'MainLayout'
})

</script>
