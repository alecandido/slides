---
theme: bricks
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: TH retreat 2023 - Alessandro Candido
mdc: true
---

# Alessandro Candido

TH retreat 2023

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    <iconamoon-arrow-right-6-circle-fill class="inline" scale="150"/>
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="mailto:a.candido@cern.ch" class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon:email />
  </a>
  <a href="https://github.com/slidevjs/slidev" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---
transition: fade-out
layout: default
---

<div class="absolute top-0 left-0 w-full h-full" flex="~" justify="center">
  <img src="/assets/affiliation-map.svg" scale="120">
</div>

---
transition: slide-up
level: 2
---

# <eos-icons-neural-network/> PDF
Theory and methods 

<div m="x-20" flex="~ row" justify="center">

|  |  |
| --- | --- |
| <kbd>DIS</kbd> | [yadism](https://github.com/NNPDF/yadism): Yet Another DIS Module |
| <kbd>Evolution</kbd> | [EKO](https://github.com/NNPDF/eko): Evolution Kernel Operator |
| <kbd>Grids</kbd> / <kbd>FK tables</kbd> | [PineAPPL](https://github.com/NNPDF/pineappl): PineAPPL is not APPLgrid |
| <kbd>GPPDF</kbd> | <mdi-pickaxe m="r-3"/> Work in progress <mdi-pickaxe m="l-2" scale="x--100"/>|

</div>

<div flex="~ row" justify="center" items="center" h="30" m="5">
  <img src="/assets/n3pdf.png" h="15" m="5"/>
  <img src="/assets/nnpdf.png" h="10" m="5"/>
</div>

---
transition: slide-right
layout: default
---

<div class="absolute top-10 left-0 w-full h-full" flex="~" justify="center">
  <img src="/assets/pineline.svg" scale="115">
</div>

<p c="fuchsia" absolute="~" top="20" right="20" italic="~">
  <a href="https://nnpdf.github.io/pineline">https://nnpdf.github.io/pineline</a>
</p>


---
transition: slide-down
layout: items
---

# The 4.0 family

<div grid="~ rows-2 cols-2" w="full" h="full">
<div>

## Baseline

Including IC and ICA

</div>
<div>

## QED

</div>
<div>

## N3LO

</div>
<div>

## MHOU
</div>
</div>

---
transition: fade-out
layout: section
---

# <mdi-cosine-wave scale="y--100"/> GPPDF

Gaussian Processes extraction

<div flex="~ row" justify="center">

[`lsqfitgp`](https://gattocrucco.github.io/lsqfitgp/docs/)

</div>

::right::

<div m="t--20 l-5">
  <img src="/assets/gpfit.png" h="70" m="-5">
  <img src="/assets/gphyper.png" h="70" m="-5">
</div>

---
transition: slide-down
layout: image-right
image: '/assets/cryo.jpg'
---

# Quantum <clarity-atom-solid inline="~"/>

<div class="absolute top-12 left-25 w-150 h-full" flex="~" justify="center">
  <img src="/assets/qibo-ecosystem.svg">
</div>

---
layout: image-right
image: '/assets/qrc-lab.svg'
---

# Quantum <clarity-atom-solid inline="~"/>
<br>

- sotware framework and user interface
- applications
- hardware execution & algorithms acceleration


<div absolute="~" bottom="10">
  <a href="https://files-prod.tii.ae/360/TII-QRC-Computing-Lab.html" italic="~" c="gray" font="size-3">
    TII Quantum computing lab
  </a>
</div>

---
transition: slide-up
layout: image-left
image: '/assets/zcu.png'
---

# <carbon-chip /> FPGA

<!--

# LaTeX

```ts {all|2|1-6|9|all}
interface User {
  id: number
  firstName: string
  lastName: string
  role: string
}

function updateUser(id: number, update: User) {
  const user = getUser(id)
  const newUser = { ...user, ...update }
  saveUser(id, newUser)
}
```
-->

<!-- <arrow v-click="[3, 4]" x1="400" y1="420" x2="230" y2="330" color="#564" width="3" arrowSize="1" /> -->

<!--
[^1]: [Learn More](https://sli.dev/guide/syntax.html#line-highlighting)

<style>
.footnotes-sep {
  @apply mt-20 opacity-10;
}
.footnotes {
  @apply text-sm opacity-75;
}
.footnote-backref {
  display: none;
}
</style>
-->

<!--

# LaTeX

LaTeX is supported out-of-box powered by [KaTeX](https://katex.org/).

<br>

Inline $\sqrt{3x-1}+(1+x)^2$


Block
$$ {1|3|all}
\begin{array}{c}

\nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} &
= \frac{4\pi}{c}\vec{\mathbf{j}}    \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\

\nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\

\nabla \cdot \vec{\mathbf{B}} & = 0

\end{array}
$$

<br>

[Learn more](https://sli.dev/guide/syntax#latex)
-->

---
layout: statement
class: text-center
---

# Get in touch!

[Documentations](https://sli.dev) · [GitHub](https://github.com/slidevjs/slidev) · [Showcases](https://sli.dev/showcases.html)
