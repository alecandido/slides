<script lang="ts">
export default {
  props: {
    aref: String,
  },
};
</script>

<template>
  <a class="arxiv-ref" :href="'https://arxiv.org/abs/' + aref">
    <code> [arXiv: {{ aref }}] </code>
  </a>
</template>

<style>
a.arxiv-ref {
  border-style: none !important;
  vertical-align: 20%;
}

a.arxiv-ref code {
  @apply bg-zinc-200 dark-bg-zinc-800;
  @apply c-green-600 dark-c-green-500;
}

a.arxiv-ref code:hover {
  @apply c-green-700 dark-c-green-300;
}

a.arxiv-ref code::before {
  content: "";
}
a.arxiv-ref code::after {
  content: "";
}
</style>
