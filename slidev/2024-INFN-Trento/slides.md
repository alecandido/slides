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

# Simulation and Control

Quantum middleware


---

# Qibo

Execution

<img src="assets/backends.svg" m="t--10"/>

---

# State vector

Preserve whole information.

<div grid="~ cols-2" h="full" gap="lg" p="sm t-10 b-20" class="children:(flex-(~ col) p-sm)">
<div bg="red-950">

<div flex="~ row justify-center" m="t-5 b-20">

### Challenges

</div>

- linear algebra
    - *i.e. array library*
- performances
- memory management

</div>
<div bg="blue-950">

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

# Results

<div h="full" grid="~ cols-2" gap="sm" class="children:(flex-(~ col) gap-sm children:(rounded-md p-sm bg-white))">
  <div>
    <img src="assets/qj_multigpu.svg"/>
    <img src="assets/qj_evol.svg"/>
  </div>
  <div>
    <img src="assets/qj_qft.svg"/>
    <img src="assets/qj_dry_vs_sim.svg"/>
  </div>
</div>

---

# Automatic differentiation

Framework portability: implement in one, export derivatives.

Applications: QML

---

# Clifford

pro:

- scalability
- error correction

---

# Tensor network

challenges:

- arrays (already there)
- contractions
- approximations

pro:

- scalability
- general purpose

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
layout: none
---

<div z--2 absolute="~" h="full" w="full" flex="~ justify-center items-center">

# [Platform dashboard](http://login.qrccluster.com:10000/)

</div>

<iframe src="http://login.qrccluster.com:10000/" h="200%" w="200%" scale="50" translate="x--120 y--70"/>

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
