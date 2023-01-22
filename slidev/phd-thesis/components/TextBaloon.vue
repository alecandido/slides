<script lang="ts">
  export default {
    props: {
      border: {
        type: Boolean,
        default: false
      }
    },
  }

</script>

<template>
  <div class="bg-coolgray-200 c-zinc-800 rounded-2"
    dark="bg-zinc-900 c-coolgray-200"
    justify="center" flex="~ col" shadow="black lg" 
    :class="border && 'b-zinc-800 dark-b-coolgray-100 border-2'">
      <slot/>
  </div>
</template>
