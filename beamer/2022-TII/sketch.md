# Sketch

## Guidelines

- try to follow practical examples
  - take well known tools and repositories as examples
- point out good examples
  - better to know what to do (learn what to avoid as a second step)
  - stress variety: there is not a single correct way of doing things

## Outline

- a project is a problem
  - start identifying what exactly is your problem
  - you should try to define boundaries at the beginning, not to outgrow the
    initial purpose
    - example: UNIX philosophy, one tool one task, complexity by composition
    - maintainability is critical
- start to draw your solution
  - if possible, in abstract terms
  - your solution will depend on tools availability, but it should drive your
    tools choice - do not choose a given solution because you want to use that
    tool: there are always many available
- tools choice
  - language choice: of course this is more or less the first choice, but take
    into account the alternatives
  - libraries and dependencies: this is often more important than the language
    itself
  - maintainability matters
    - as least dependencies as possible
    - your dependencies should be healthy: check the project status and history
  - keep it simple, stupid
  - principle of least power
  - the expertise of your collaborators is fundamental
- developer tools: project maintenance and collaboration
  - Git is not GitHub (and it is already good enough)
  - hooks are bare Git
  - there are languages with little or vast choices
    - `cargo` is wonderful out of the box
    - Python and C/C++ require plenty of choices
- lib vs app
  - if it is a very small project, with a short lifespan, it doesn't matter
  - if it isn't, then it matters -> for a library you always want a stable and
    useful API for your users
  - for an application, it might seem you don't need, but it is way better if
    you allow for it
    - scripting is always useful, to tune details and automate pipelines
    - plugin systems are frequent
    - app -> platform
      - typical
      - often not desirable ["Zawinski's
        Law"](https://en.wikipedia.org/wiki/Jamie_Zawinski#Zawinski's_Law)

## Reserve

- https://en.wikipedia.org/wiki/Brooks%27s_law
- Design Patterns
  - good to know: https://refactoring.guru/design-patterns
  - often not good to use:
    - https://en.wikipedia.org/wiki/Software_design_pattern#Criticism
    - I don't remember where I read it, but someone wrote "If I see _any_
      pattern in my code, that is a sign of duplication. Do not use 'patterns',
      write modular code."
