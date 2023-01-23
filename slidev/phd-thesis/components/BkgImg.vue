<script setup lang="ts">
  const props=defineProps({
    dark: Boolean,
    default: false
  })

  let cls="";
  if (props.dark) {
    cls += " dark"
  } else {
    cls += " light"
  }
</script>

<template>
  <img :class="cls" rounded="~" transition="all 500" hover="scale-105">
</template>

<style>
  .light {
    @apply dark-bg-white
  }
  .dark {
    @apply bg-black dark-bg-inherit
  }
</style>
