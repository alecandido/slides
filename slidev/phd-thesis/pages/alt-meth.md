---
layout: section
---

# Alternative Methodology

---
layout: cols
---

# Function space

Actually a large one

<template #col-1>

A function $f: \R \to \R$ (or suitable intervals) lives in an
infinite-dimensional space.

This has a simple consequence:

<titled-box title="Under-determination">

Fitting an <b>unknown function</b> on a finite number of data is always an
<b>under-determined</b> problem.

</titled-box>

How to choose a solution, when **many** are available and **equivalent**?

</template>
<template #col-2>
  <div m="y-10" flex="~" justify="center">
    <bkg-img src="meth/underdetermined.svg" p="6" w="xs"/>
  </div>
</template>

---
layout: cols
---

# Assumptions

Declined in two main options

<template #col-1>
<div m="-4"/>

<titled-box title="Slicing">

One consists in reducing the number of parameters, by <b>slicing</b> a
suitable <b>hyperplane</b>

</titled-box>

In PDF language this corresponds to the choice of a **fixed parametrization**.
A suitable one can also remove loss-function zero-directions from the space.

  <div m="y-2" flex="~" justify="center">
    <bkg-img src="meth/sliced.svg" p="6" w="sm"/>
  </div>
</template>
<template #col-2>

<titled-box title="Regularization">

The second approach removes the zero-direction by <b>adding</b> some
<b>regularization</b>.

</titled-box>

This is what the **Neural Network** (and its training algorithm) is doing
under the hood.

  <div m="y-10" flex="~" justify="center">
    <bkg-img src="meth/regularized.svg" p="6" w="sm"/>
  </div>
</template>

---
layout: cols
---

# Bayes

Something conceptually simple, but still powerful

<div m="-4"/>

<template #col-1>

Typical examples of ML are:
- image and speech recognition
- generative tasks
- style transfer
- and so on...

All these problems have in common:
<div text="center">

very **high-dimensional** objects, with <b>poor analytical/algorithmic insight</b> on their
structure

</div>

Working out an explicit and effective representation for them would be
difficult.

<div text="center">

**This is not the case for PDFs!**

</div>
</template>
<template #col-2>

Math language description and clear analytic properties
are at hand: 
<div text="center sm" m="t--4 b-2">
  sum rules, power-like behavior, ...
</div>

  <div m="y-2" flex="~" justify="center">
    <bkg-img src="meth/pdf.svg" p="6" w="xs"/>
  </div>

$$
P(A|B) = \frac{P(B|A) P(A)}{P(B)}
$$

</template>

---
layout: cols
---

# Gaussian Processes

The prior

Like with NN we can limit the slicing*, using a suitable **regularization**, here
coming **from the prior**.


<template #col-1>
  <div m="y-2" flex="~" justify="center">
    <bkg-img src="meth/sine6.png" p="6" w="xs"/>
  </div>

Essentially a **multi-Gaussian** with a <b>metric-driven kernel</b>, with the
motivation that is simple, and sufficiently flexible.

</template>
<template #col-2>

Basic ideas:

- ***parametrization** exactly our delivery: we use PDF values at grid points (we
  would no expose more degrees of freedom anyhow, so no need to use them)
- **transformations** data are not in the PDF space, but we can use
  linear and non-linear (quadratic) transformations
- **sum rules** the Gaussian process allow us to impose them
  analytically (in practice, it is easier to impose them as zero-error data, but
  it is only a technicality)
- **integrability** integrability and extrapolation behavior it is
  implemented as constraints on hyper-parameters

</template>

<!-- Not only we limit the reduction of the number of parameters, but we can choose
the most relevant ones. To use the PDF, it has to be represented, and usually
this is done through interpolation. Keeping all the parameters used in the
subsequent interpolation, essentially the limitation are not coming any longer
from the fit, but from the usage. -->

---

# Prototype

Just a POC on completely fake data.

<div m="y-10" flex="~" justify="center">
  <bkg-img src="meth/fit-pdf-new.png" p="6" w="xl" 
  hover="scale-140 translate-y--10"
  transition="1000"/>
</div>
