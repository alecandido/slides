---
# try also 'default' to start simple
theme: default
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
# apply any windi css classes to the current slide
highlighter: shiki
lineNumbers: false
info: |
  ## PhD Thesis
  Slides for the PhD Thesis Defense of Alessandro Candido.

  More at [phd.annibale.dev](https://phd.annibale.dev)
# persist drawings in exports and build
drawings:
  persist: false
# use UnoCSS
css: unocss
layout: cover
background: amenities/IMG20210709133314-1024x768.jpg
class: "text-center p-0"
---

<div class="flex justify-end items-center" h="full">
  <text-baloon class="p-8" :border="true">
    <h1 class="!text-3xl font-bold" style="font-variant: initial">Theory predictions</h1>
    <h2 class="!text-xl italic">for PDF fitting</h2>
  </text-baloon>
</div>

---
layout: image-right
image: protons/042917_proton_main.jpg
---

# Contents

<div style="height: 2rem"/>

1. introduction
2. theory
    - DIS
    - evolution
    - pipeline
3. methodology
4. applications

<style>
  li {
    line-height: 3rem !important;
  }
  li li {
    line-height: 2rem !important;
  }
</style>


---

# NNPDF 4.0
<div w="full" flex="~" justify="end">
  <cite-arxiv aref="2109.02653" right="0" class="relative"/>
</div>

<div grid="~ cols-2 gap-8" m="8 t-4 y-12">
  <bkg-img src="pdfs/40-q3.svg" p="x-6"/>
  <bkg-img src="pdfs/40-q100.svg" p="x-6"/>
</div>

To get to a full PDF set many ingredients are required...

---

The two most relevant novelties of NNPDF 4.0 have been:
- the Machine Learning improved methodology
- the great amount of new LHC data sets.

<div w="full" flex="~" justify="center" items="center" m="8">
  <bkg-img src="organization.png" w="150" p="8"/>
</div>

My main work has not yet been used for a main fit, and it concerns the remaining
part: *theory predictions*.

---
layout: section
---

# Theory predictions

---
layout: section
---

# Alternative Methodology

---
layout: section
---

# Applications

---
layout: section
---

# Conclusions

---

# Summary

---

# Outlook

---
layout: cover
background: amenities/Group_Picture_Varenna.jpg
---

<div class="flex justify-end items-end" h="full">
  <text-baloon p="4">
    <p m="!0">
      Many thanks to the whole <strong c="sky-400">NNPDF collaboration</strong>!
    </p>
  </text-baloon>
</div>

---
layout: cover
background: amenities/IMG_2297.jpg
---

<div class="flex justify-begin items-begin">
  <text-baloon p="4">
    <p m="!0">
      ... and especially to our <strong c="pink-400">Milan group</strong>!!
    </p>
  </text-baloon>
</div>

---
layout: section
---

# Backup

---
preload: false
src: pages/animations.md
---

---
src: pages/latex.md
---

---
src: pages/diagrams.md
---

