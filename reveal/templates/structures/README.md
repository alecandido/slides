# Presentation structures

Presentation structures to be build with jinja.

The main goals are:
- to have reusable presentations layout
- to organize slides in more files, instead of the single `index.html`, that
    instead is built by jinja

## Organization
Each folder will contain:
- `template.html`: the structure template with jinja syntax
- `structure.yaml`: a configuration file to be read with variables configuration
    and further data used in template compile process
