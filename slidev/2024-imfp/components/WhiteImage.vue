<script setup>
const props = defineProps(["src"]);

let path = import.meta.env.BASE_URL + props.src;
</script>

<template>
  <div bg-white rounded-3xl flex="~ justify-center items-center">
    <img v-bind:src="path" max-w="100%" max-h="100%" />
  </div>
</template>
