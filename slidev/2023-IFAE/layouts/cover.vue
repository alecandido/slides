<script setup lang="ts">
  import { computed } from 'vue'
  import { handleBackground } from '@slidev/theme-default/layoutHelper'
  const props = defineProps({
    background: {
      default: '',
    }
  })

  const style = computed(() => handleBackground(props.background, true))
</script>

<template>
  <div class="slidev-layout cover" :style="style">
    <div class="my-auto w-full h-full">
      <slot />
    </div>
  </div>
</template>
