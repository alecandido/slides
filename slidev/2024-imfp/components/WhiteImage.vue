<script setup>
const props = defineProps(["src"]);

let path = "/assets/" + props.src;
</script>

<template>
  <div bg-white rounded-3xl p-lg flex="~ justify-center items-center">
    <img v-bind:src="path" w="100%" />
  </div>
</template>
