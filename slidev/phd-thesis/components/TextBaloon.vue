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
  <div class="bg-zinc-900 c-coolgray-200 rounded-2 justify-center" flex="~ col" shadow="black lg" :class="border && 'b-coolgray-100 border-2'">
      <slot/>
  </div>
</template>
