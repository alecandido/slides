# Deep Inelastic Scattering

Lepton-hadron scattering

<div m="y-10" class="flex justify-center">
  <bkg-img src="theory/dis-diagram.svg" p="6" w="xs"/>
</div>

The ideal process to probe PDFs: a point-like particle scanning the composite
one.

---
src: ./dis/dimensions.html
---

---
src: ./dis/available.html
---

---

# [Yadism](https://github.com/NNPDF/yadism)

Yet another DIS module 

<div w="full" flex="~" justify="center" items="center" m="t--4 b-2">
  <bkg-img src="yadism.png" w="80" p="1"/>
</div>

There were already mainly two available DIS providers:
[APFEL](https://github.com/scarrazza/apfel/) and
[QCDNUM](https://www.nikhef.nl/~h24/qcdnum/).

But we needed:
<div float="right" w="3/7">
<ul>
 <li>integration in the <Link to="15">pineline</Link></li>
 <ul>
    <li>produce PineAPPL grids</li>
    <li>registered PineFarm provider</li>
 </ul>
 <li>curated <a>docs</a></li>
 <li>improved maintainability (more modular, organic design, CI/CD, packaging
 and distribution)</li>
</ul>
</div>

- an improved/rechecked scale variations implementation
- new analytical components
  - intrinsic NLO CC
  - improved heavy NNLO NC
  - heavy NNLO CC *(yet to come)*
- re-examine FNSs
- more TMC options
- extended and automated benchmarks

Yadism is also a [coefficients
database](https://github.com/NNPDF/yadism/tree/master/src/yadism/coefficient_functions):
they are implemented in such a way to be directly used by 3<sup>rd</sup>
parties!

---

# FONLL status
