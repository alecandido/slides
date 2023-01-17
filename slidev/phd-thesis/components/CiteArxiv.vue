<script lang="ts">
  export default {
    props: {
      aref: String
    }
  }
</script>

<template>
  <a class="arxiv-ref" :href="'https://arxiv.org/abs/' + aref">
    <code class="c-green">
      [arXiv: {{ aref }}]
    </code>
  </a>
</template>

<style>
  a.arxiv-ref {
    border-style: none !important;
  }

  a.arxiv-ref:hover code {
    @apply c-green-700
  }
</style>


