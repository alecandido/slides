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

My ecosystem of bash scripts is not optimal, but quick enough:

- bash is no good in the long run, since it is not (really) a general purpose
  programming language, so when it grows scales bad -> Better Python or
  something similar
- it is optimal to work with files, so for a small project like this speeds up
  things

#### Reproducible science

- I wrote a YAML "schema"
- and YAML descriptions following the schema
- problems:
  - the schema is not really well-defined, and quickly changing for increasing
    needs
    - it is a 2-3 days project
    - **solution**: have experience, lay down a reasonably comprehensive and
      extendable schema + version the schema as well
  - what is a "schema" in this sense is not well-defined as well:
    - **solution**: formal specifications exists for YAML schema
      - https://asdf-standard.readthedocs.io/en/1.0.3/schemas/yaml_schema.html
      - https://json-schema-everywhere.github.io/yaml
    - inspired by the more successful [JSON schema](https://json-schema.org/)
    - inspired on the much older [XML Schema Definition
      (XSD)](<https://en.wikipedia.org/wiki/XML_Schema_(W3C)>)
  - I need to keep the input files synceds to values in the description files
    - **solution**: write a generator (1-2h of work at most, once schema
      established)
    - this allows to have multiple versions and updates of input files
- this is still kind of a manual solution, other people faced the problem, and
  there are frameworks to assist
  - https://juliadynamics.github.io/DrWatson.jl/dev/
    - logo (with href)
    - githuburl
    - brief description
      - by nonlinear dynamics community (org:
        [JuliaDynamics](https://juliadynamics.github.io/JuliaDynamics/) href
        small website screenshot)
    - bib citation
  - in the machine learning and data analysis community there is a similar
    problem for data - now that machine learning has professional applications
    there are products to manage data
    - [DVC](https://dvc.org/) (href owl logo, see repo), roughly "Git for data"
  - all these tools are open source

### Paper conclusions and comparison

Compare with my results.

Main difference: `1e6` vs `3e5` fluid particles.

## Renew Simulation
