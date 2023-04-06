---
layout: cols
---

# Charm nel protone

Pesante ma presente

<div w="full" flex="~" justify="end" m="t--8">
  <cite-arxiv aref="2208.08372" right="0" class="relative"/>
</div>

<template #col-1>

Una componente di  **charm** nel protone non è una novità, dato che viene
generato dall'evoluzione perturbativa secondo le equazioni DGLAP, in uno schema
con 4 o più flavor (per produzione di coppie dal gluone).

Ma è anche possibile ottenere un quark charm differentemente:

- **perturbativa**: generata dall'evoluzione DGLAP
- **intrinseca**: generata dalla dinamica non perturbativa
- **estratta**: rilevata nel risultato di una determinazione dai dati

</template>
<template #col-2>

<div m="6" w="full" flex="~" justify="center">
  <video autoplay loop muted w="4/5" h="2/3" p="2" rounded="4"
    bg="black" shadow="~ dark">
    <source src="split.mp4" type="video/mp4">
  </video>
</div>

<div m="-12"/>

La componente charm nel fit <b>NNPDF4.0</b> non è direttamente *intrinseca*,
dato che viene scelto di eseguirlo in uno schema a 4 flavor (4FNS).

</template>

---
layout: cols
---

# Alla scoperta della componente **intrinseca**

<div m="y--2"/>

<template #col-1>
<div flex="~" justify="center" items="center">

```mermaid
flowchart TD
  data <-..-> fit
  fit -- "Matching: 4FNS ➤ 3FNS\n @ NNLO o N3LO" --> intrinsic

  data("Dati sperimentali e predizioni")
  fit("NNPDF4.0: parametrizzazione in 4FNS")
  style fit stroke:#65a30d
  intrinsic("3FNS PDFs: incluse le <strong>componenti intrinsiche del charm,
  <em>indipendenti dalla scala</em></strong>
  <em style='font-size: 0.8em'>PDF e incertezze MHO</em>")
  style intrinsic stroke:#e11d48
  classDef hl stroke-width:2px
  class intrinsic,fit hl
```

</div>
</template>
<template #col-2>

Gli **elementi di matrice dell'operatore (OME)** $\mathbf{A}^{(n_f)}(\mu_{h}^2)$
sono parzialmente noti fino a N$^3$LO.

<div m="0" class="flex justify-center">
  <bkg-img src="vfns-details.svg" p="6" w="xs"/>
</div>

L'**operatore inverso** (l'OME può essere invertito sia  *perturbativamente* che
*numericamente*):


<div m="0" class="flex justify-center">
  <bkg-img src="vfns-back-details.svg" p="6" w="xs"/>
</div>

</template>

<template #after>

<div m="y-8"/>

$$
\mathbf{f}^{(n_f+1)}(\mu_{F,1}^2) =
  \left[\mathbf{E}^{(n_f+1)}(\mu_{F,1}^2\leftarrow \mu_{h}^2)
        {\mathbf{R}^{(n_f)}}
        \mathbf{A}^{(n_f)}(\mu_{h}^2)
\mathbf{E}^{(n_f)}(\mu_{h}^2\leftarrow \mu_{F,0}^2) \right]\\
        \times \mathbf{f}^{(n_f)}(\mu_{F,0}^2)
$$

</template>


<style>
  p {
    @apply !text-sm !m-y-2
  }
</style>

---

# Evidenza

<div m="y-8" class="flex justify-center">
  <bkg-img src="3fns_Quad_MHOU.svg" p="2" w="sm" 
    hover="scale-150" transition="all 1000"/>
</div>

In uno schema <b>a 3 flavor (3FNS)</b> è possibile osserva un <b>picco</b>
simile a quello dei <b>quark in valenza</b>.
- per $x \leq 0.2$ le **incertezze perturbative** sono piuttosto ampie
- la **frazione di impulso** associata è complessivamente entro l'**1%**

---
layout: cols
---

# Predizioni e stabilità

<template #col-1>

<div m="y-10" class="flex justify-center">
  <bkg-img src="lhcb-zcharm-pheno.svg" p="6" w="xs"/>
</div>


Il fit con charm intrinseco produce <b>migliori predizioni</b> per alcuni
particolari dati, particolarmente sensibili alla presenza del charm, e *non
inclusi nel fit*.

</template>
<template #col-2>

L'<b>evidenza è stabile</b> sotto variazioni dei dati considerati, *inclusi*
quelli più sensibili al charm.

<div m="y-10" class="flex justify-center">
  <bkg-img src="pull_baseline_EMC_LHCb_Zc.svg" p="6" w="xs"/>
</div>

</template>
