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
  pt[PyTorch] --> qibo(((qibo)))
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
transition: abrupt
---

# Qibolab - Interface

<div w="full children:90%" flex="~ justify-center row" >

```mermaid
flowchart LR
  subgraph input
    circ[Circuit] --> pulse[Pulse sequence]
  end
  pulse --> platform[Platform]
  platform --> driver[Driver] --> board[Electronics]
  subgraph physical
    board --> QPU
  end
  style input stroke:#e78,stroke-width:2px
```

</div>

<div grid="~ cols-2 rows-3" h="65%" gap-sm p="sm t-0">
<div row-span-2>

- platform
- pulses

</div>
<div col-start-1>
    Pulse sequence plot (from notebook?)
</div>
<div row-span-3 row-start-1 col-start-2>

```python
def create():
    instrument = DummyInstrument("myinstr", "0.0.0.0:0")

    channels = ChannelMap()
    channels |= Channel(
        "readout", 
        port=instrument.ports("o1")
    )
    ...

    return Platform(
        "myplatform", 
        qubits={qubit.name: qubit}, 
        instruments={instrument.name: instrument},
        ...
    )
```

</div>
</div>

---

# Qibolab - Drivers

<div w="full children:90%" flex="~ justify-center row" >

```mermaid
flowchart LR
  subgraph input
    circ[Circuit] --> pulse[Pulse sequence]
  end
  pulse --> platform[Platform]
  platform --> driver[Driver] --> board[Electronics]
  subgraph physical
    board --> QPU
  end
  style physical stroke:#e78,stroke-width:2px
```

</div>

<div grid="~ cols-5" gap-sm p="sm" m-t-5>
<div flex="~ col justify-center items-center" m-t--10>
<div p="sm x-2xl" rounded bg="slate-200 dark:slate-800">

- [Qblox](https://www.qblox.com/)
- [Zurich](https://www.zhinst.com/)
- [QM](https://www.quantum-machines.co/)
- [QICK](https://github.com/openquantumhardware/qick)

</div>
</div>
<div col-span-4>

```sh
      move      1,R0        # Start at marker output channel 0 (move 1 into R0)
      nop                   # Wait a cycle for R0 to be available.

loop: set_mrk   R0          # Set marker output channels to R0
      upd_param 1000        # Update marker output channels and wait 1μs.
      asl       R0,1,R0     # Move to next marker output channel (left-shift R0).
      nop                   # Wait a cycle for R0 to be available.
      jlt       R0,16,@loop # Loop until all 4 marker output channels have been set once.

      set_mrk   0           # Reset marker output channels.
      upd_param 4           # Update marker output channels.
      stop                  # Stop sequencer.
```

<div m-t--10 z-2 relative>
<p text-right italic m-r-20>

by
[Qblox](https://qblox-qblox-instruments.readthedocs-hosted.com/en/master/cluster/q1_sequence_processor.html#example)

</p>
</div>

</div>
</div>

---

# Qibosoq - Server on QICK

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
