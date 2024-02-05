---
theme: default
highlighter: shikiji
lineNumbers: false
info: |
  <https://qibo.science/>

  <https://github.com/qiboteam/qibo>
drawings:
  persist: false
transition: slide-left
title: Simulation and control software
mdc: true
background: assets/qibo_ecosystem_webpage.svg
innerColor: '#304'
class: text-center
layout: mycover
---

<h1 c="white">Simulation and Control</h1>

<p c="white">Quantum middleware</p>


---

# Qibo

Execution

<img src="assets/backends.svg" m="t--10"/>

---

# State vector

Preserve whole information.

<div grid="~ cols-2" h="full" gap="lg" p="sm t-10 b-20" class="children:(flex-(~ col) p-sm)">
<div bg="dark:red-950 red-200">

<div flex="~ row justify-center" m="t-5 b-20">

### Challenges

</div>

- linear algebra
    - *i.e. array library*
- performances
- memory management

</div>
<div bg="dark:blue-950 blue-200">

<div flex="~ row justify-center" m="t-5 b-20">

### Approach

</div>

Adopt **widespread** and **optimized frameworks**, to benefit from their expertise
(*software reuse*).

**Chisel the last layer** on top of each framework, to mold it on our use case.

</div>
</div>

---

# Backends mechanism

Plug the framework.

<br m="2">

Structure the integration of the various libraries.

<img src="assets/state-vector.svg"/>

Common operations are implemented once and reused (when possible).

---
transition: slide-up
---

# Results

<div h="full" grid="~ cols-2" gap="sm" class="children:(flex-(~ col) gap-sm children:(rounded-md p-sm bg-white))">
  <div>
    <img src="assets/qj_qft.svg"/>
    <img src="assets/qj_dry_vs_sim.svg"/>
  </div>
  <div>
    <img src="assets/qj_multigpu.svg"/>
    <img src="assets/qj_evol.svg"/>
  </div>
</div>

---

<div h="full" m="t--35 b-30" grid="~ cols-2" gap="sm" class="children:(flex-(~ col justify-end) gap-sm children:(rounded-md p-sm bg-white))">
  <div>
    <img src="assets/qj_dry_vs_sim.svg"/>
    <img src="assets/qj-grace-managed.png"/>
  </div>
  <div>
    <img src="assets/qj-grace-cpu.png"/>
    <img src="assets/qj-grace-cupy.png"/>
  </div>
</div>

<h3 text-right>

[*on advanced hardware*](https://gist.github.com/migueldiascosta/0a0dbe061982bc4cc2bc7171785a4b86)

</h3>

---

# Automatic differentiation

for quantum machine learning (QML)


<div grid="~ cols-3" m-t-15>
<div>
  Autodiff simulation is fundamental to support QML investigation.

  A dedicated differentiable backend in simulation can considerably help algorithms
  development.

  Moving towards a single interface, encompassing both simulation and quantum hardware
  implementations.
</div>

<div col-span-2>

```mermaid
flowchart LR
  subgraph user
    tf ~~~ fw
    pt ~~~ fw
    jx ~~~ fw
  end
  tf[Tensorflow] --> qibo --> ifw["<em>e.g.</em> TensorFlow"]
  pt[PyTorch] --> qibo
  jx[JAX] --> qibo
  fw[...] --> qibo
  qibo -.-> hw[Parameter shift rule]
  qibo -.-> hw1[...]
  subgraph implementation
    hw1 ~~~ ifw
    hw1 ~~~ hw
  end
```

*Framework portability: implement in one, export derivatives.*

</div>
</div>

---

# Clifford

pro:

- scalability
- error correction

---

# Tensor network

Optimized for observables.

<div grid="~ cols-5" gap="sm">

<div col-span-3>
<img src="assets/quimb-circuit.svg"/>
</div>

<div>
Contractions:

[Inkscape plot]
</div>
</div>

---

# QiboTN

<div w="full" flex="~ row justify-center">
<img w="80%" bg="white" p="5 t-2" rounded="lg" src="assets/qibotn.png"/>
</div>

---
layout: image-left
image: assets/qrc-lab.svg
---

<div flex="~ col justify-center" h-full p-10>

# Qibolab

Quantum control

</div>

---

# Interface

- platform
- pulses

---

# Drivers

---

# Qibosoq

---

# Towards multitech

- Input ->
  - circuits
  - pulses could be generic enough
- -> QPU
  - wrapped by drivers

---

# [Platform dashboard](http://login.qrccluster.com:10000/)

<div h-full p-lg flex="~ col justify-center" gap="lg" class="children:(w-full p-lg rounded-lg bg-#111217)">
  <img src="assets/dashboard.png"/>
  <img src="assets/dashboard-slurm.png"/>
</div>

---

# Qibocal

An owed mention

<div flex="~ justify-center" h="full">
  <img src="assets/qq_qibocal.svg" h="80%"/>
</div>


---
layout: none
---

<div z--2 absolute="~" h="full" w="full" flex="~ justify-center items-center">

# [Qibocal reports](http://login.qrccluster.com:9000)

</div>

<iframe src="http://login.qrccluster.com:9000/" h="200%" w="200%" scale="50" translate="x--120 y--70"/>

---
layout: center
---

# Thanks
