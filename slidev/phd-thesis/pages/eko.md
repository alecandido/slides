# DGLAP evolution

Define PDFs dependency on unphysical scale $\mu_F$

$$
  \mu^2 \frac{\text{d}{\textbf{f}}}{\text{d}\mu^2}(\mu^2) = \textbf{P} (a_s(\mu^2),\mu^2) \otimes \textbf{f}(\mu^2)
$$

<br m="2">

These equations define a set of **linear operators** $\textbf{E}(\mu^2 \leftarrow
\mu_0^2)$ **on PDF** sets:

$$
  \textbf{f}(\mu^2) = \textbf{E}(\mu^2 \leftarrow \mu_0^2) \otimes \textbf{f}(\mu_0^2)
$$

<div m="y-10" flex="~" justify="center">
  <bkg-img src="theory/ev-op.svg" p="6" w="md"/>
</div>

---

# [EKO](https://github.com/NNPDF/eko)

Evolutionary Kernel Operator

<div w="full" flex="~" justify="end" m="t--8">
  <cite-arxiv aref="2202.02338" right="0" class="relative"/>
</div>

<div m="t--12 b-6" flex="~" justify="center">
  <bkg-img src="theory/eko.png" p="2" w="1/5"/>
</div>

The main goal of EKO is to compute **reusable evolution operators** (i.e. EKOs).

<div flex="~" justify="center"
  hover="scale-180"
  transition="800">

```mermaid
flowchart LR
  rc("runcard 📄") -- "run 🦓" --> eko("EKO 📦")
```

</div>

It does so, by solving DGLAP equations in $N$-space, but providing an $x$-space
output for compatibility with existing PDF sets.

<div m="y-6" flex="~" justify="center">
  <bkg-img src="theory/mellin.svg" p="4" w="lg"/>
</div>

---

# Original features

<div float="right" w="1/4" m="t--4">
  <span p="2" b="1 black op-10" dark="b-white b-op-10" rounded="0.7">
    <Link to="17">Pineline</Link> integration
  </span>
</div>

- Intrinsic evolution

<div m="y-6" flex="~" justify="center">
  <bkg-img src="theory/intrinsic.svg" p="4" w="xs"/>
</div>

- Full backward VFNS (including intrinsic)

<div m="y-6" flex="~" justify="center">
  <bkg-img src="theory/back-vfns.svg" p="4" w="sm"/>
</div>


---

# ... and more to come

<div/>

More than anything else, EKO is an evolution **framework**, still rapidly
growing collecting many contributions, from new and existing applications.

The goal is to have all of them in a single place, for anyone interested in
solving DGLAP.

<div float="right" w="3/7">

- storage
- distributed computation
- $N$ space
  [expressions](https://github.com/NNPDF/eko/tree/split-math-in-module/src/ekore) [database](https://github.com/NNPDF/eko/issues/185)
- curated [docs](https://eko.readthedocs.io/)
- improved maintainability (more modular, organic design, CI/CD, packaging
 and distribution)

</div>

- Factorization scale vars 
  - first truly expanded
  - full *resummation* scales <cite-arxiv aref="2205.15900" right="0" class="relative"/>
- QED implementation
  - up to NLO QCD-QED and NNLO QED
  - fixed (non-running) QED coupling
- $N^3LO$ evolution and matching
  - *in-house* splitting functions
- Polarized evolution
- Time-like evolution

Of course, everything on top of reimplemented features: up to NNLO evolution and
matching, EXA/EXP/TRN (and more flexible variations), $\alpha_s$ evolution,
interpolation, ...

