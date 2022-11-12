# DS-Tau arXiv:2005.04244

## Reproduce results

### The problem

- ALMA observations
- why DS-Tau is special?
  - the widest gap of the Taurus survey
- previous estimates
- current candidate & strategy
  - the simplest model that can explain the formation of the gap, that is a
    single planet on a circular, non-inclined orbit
  - 3D hydrodynamical simulations + 3D Monte Carlo radiative transfer
    simulations
- alternatives (more complex, more free parameters)
  - multiple planet system
  - planet on an eccentric orbit
  - planet on an inclined orbit
  - lower disc viscosity combined with a sub-Neptune mass planet
  - turn the observed broad disc ring into multiple narrow rings

Basically ALMA images are still low enough resolution to allow plenty of
options.

### The numerical setup

### Paper results

### My results

#### How did I obtained my results?

- extracting parameters from the paper
- documenting the choice
- running fully reproducible simulations
  - reproducibility is already quite possible with the paper, since it describes
    "most" of the parameters involved (do not specify software version)
  - but also reproducibility complexity matters: if I have to work out
    parameters that are not so clear, the results is "less" reproducible (here
    the problem is also the user being unexpert)
  - that's why my results are reproducible launching single bash script,
    [publicly
    available](https://github.com/AleCandido/fluiddynamics_exam/blob/main/ds-tau/full.bash)
  - and software version is pinned by Git Submodules

Declare software version, publish runcards:

- in the arXiv bundle (a bit hidden), or, even better
- on a public repository (linked in the paper)

### Paper conclusions and comparison

Compare with my results.

Main difference: `1e6` vs `3e5` fluid particles.

## Renew Simulation
