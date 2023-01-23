<script setup lang="ts">
  const props = defineProps({
    title: String
  })
</script>

<template>
  <article b="1 dark:zinc-800" rounded="1">
    <header flex="~" justify="center" bg="zinc-200 dark:zinc-800" p="1">
      <h2 class="title">{{ props.title }}</h2>
    </header>
    <section class="body" p="x-4 y-2" flex="~" justify="center">
      <slot/>
    </section>
  </article>
</template>

<style>
  h2.title {
    @apply text-sm font-bold
  }
  section.body p {
    @apply m-0
  }
</style>
