<script setup lang="ts">
  import { reactive } from "vue"

  const props = defineProps({
    ncols: {
      type: Number,
      default: 2
    }
  })
  
  const style = reactive({'grid-template-columns': `repeat(${props.ncols}, minmax(0, 1fr))`})
  const names = Array.from({length: props.ncols}, (_, i) => `col-${i+1}`)
</script>

<template>
  <div class="slidev-layout w-full h-full">
    <slot/>
    <div grid="~ gap-8" :style="style">
      <section v-for="name in names">
        <slot :name="name"/>
      </section>
    </div>
  </div>
</template>
