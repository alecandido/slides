<script setup lang="ts">
import { computed } from "vue";
import type { CSSProperties } from "vue";

/**
 * Resolve urls from frontmatter and append with the base url
 */
function resolveAssetUrl(url: string) {
  if (url.startsWith("/")) return import.meta.env.BASE_URL + url.slice(1);
  return url;
}

const props = defineProps({
  background: {
    default: "",
  },
  innerColor: {
    default: "#bbb",
  },
  outerColor: {
    default: "#0000",
  },
});

const style = computed(() => ({
  color: "white",
  backgroundImage: `radial-gradient(${props.innerColor},${
    props.outerColor
  }), url(${resolveAssetUrl(props.background)})`,
  backgroundRepeat: "no-repeat",
  backgroundPosition: "center",
  backgroundSize: "cover",
}));
</script>

<template>
  <div class="slidev-layout cover">
    <div :style="style" z="-2" absolute="~" h="full" w="full" filter="blur-2" />
    <div class="my-auto w-full" backdrop="blur-xl">
      <slot />
    </div>
  </div>
</template>
