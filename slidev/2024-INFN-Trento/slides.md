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

challenges:

- linear algebra
- performances
- memory management

---

# Backends mechanism

- NumPy
- TensorFlow / PyTorch / JAX / ...
- Numba
- CuPy
- CuQuantum

---

# Automatic differentiation

Portability: implement in one, export derivatives.

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

# Control - Qibolab

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

<div z="-2" absolute="~" h="full" w="full" flex="~ justify-center items-center">

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

<div z="-2" absolute="~" h="full" w="full" flex="~ justify-center items-center">

# [Qibocal reports](http://login.qrccluster.com:9000)

</div>

<iframe src="http://login.qrccluster.com:9000/" h="200%" w="200%" scale="50" translate="x--120 y--70"/>

---
layout: center
---

# Thanks
