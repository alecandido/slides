---
layout: section
---

# Conclusions

---

# Summary 📜

All my work has been focused on Parton Distribution Functions, and most of it as
a member of the NNPDF collaboration.

<div m="y-8"/>

My main research topic has been the development of a new generation of fast and
reproducible theory predictions for HEP processes, especially focused on the PDF
fitting tasks, including:
- a <b>Deep Inelastic Scattering library</b>, [`yadism`](https://github.com/NNPDF/yadism)
- a <b>DGLAP evolution library</b>, [`eko`](https://github.com/NNPDF/eko)
  - and keep benchmarking the two of them ([`banana`](https://github.com/N3PDF/banana))
- the development of the integrated [<b>Pineline</b>](https://github.com/NNPDF/pineline), involving:
  - contributions to [**PineAPPL**](https://github.com/NNPDF/pineappl)
  - the development of two further **integrations**,
      [`pineko`](https://github.com/NNPDF/pineko) and
      [`pinefarm`](https://github.com/NNPDF/pinefarm)

<div m="y-8"/>

Moreover, I worked on a series of applications:
- <b>intrinsic charm evidence</b> in NNPDF4.0
- study of the Drell--Yan <b>forward-backward asymmetry</b> 

<div m="y-8"/>

And other more methodology-related topics, like investigation of <b>PDF
positivity</b> beyond LO.

<style>
  code {
    @apply !p-y-0
  }
</style>

---

# Outlook 🔭

From now on...

The major ongoing efforts are focused on:

- putting into [<b>production</b> the whole
  <b>Pineline</b>](https://nnpdf.github.io/pineline/), replacing the old theory
  predictions providers
- adding new* features to the baseline fit:
  - <b>MHOU</b> @ NNLO, with *theory covariance matrix* formalism <cite-arxiv aref="1906.10698" right="0" class="relative"/>
  - <b>QED</b> evolution & luxQED
  - <b>N$^3$LO</b> addition

<p text="!xs">
  *<em>with respect to NNPDF4.0</em>
</p>

<div m="y-12"/>

But they are not the only ones:

- studies on **alternative methodologies** keep going
- more theory predictions: **polarized**, **time-like**, **NNLO grids** and **CC-DIS**
- more phenomenological investigations (**$\nu$ structure functions**)
- technical improvements (speed-up, distributed computation)
- user-facing improvements (docs, tutorials, public API, bundling)

---
layout: cover
background: amenities/nnpdf.jpg
---

<div class="flex justify-end items-end" h="full">
  <text-baloon p="4">
    <p m="!0">
      Many thanks to the whole <strong>NNPDF collaboration</strong>!
    </p>
  </text-baloon>
</div>

---
layout: cover
background: amenities/n3pdf.jpg
---

<div class="flex justify-begin items-begin">
  <text-baloon p="4">
    <p m="!0">
      ... and especially to our <b>Milan group</b>!!
    </p>
  </text-baloon>
</div>
