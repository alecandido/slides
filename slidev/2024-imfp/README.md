# Export

Export with:

```sh
pnpm export --dark -c
```

### Broken

The results gallery is apparently broken, since it doesn't show the two full columns,
and "scrolls" too little.

# Plan

- Quantum platforms
  - gate-based
  - continuous variables
    : coherent and squeezed states
  - annealer
    - ???
- Quantum hardware
  : DiVincenzo criteria?
  - superconducting
  - ion traps
    - ???
  - photonics
  - (neutral atoms)
  - (Majorana fermions)
    : ask Alberto in case
  - ...
    : flash many more proposals?
- Quantum algorithms
  : creating building blocks
  - amplitude amplification
    - e.g. Grover
  - QFT
    - e.g. Shor
    - simpler: quantum JPEG
  - further advantage:
  - QML disclaimer
    - inference advantage (not training)
    - curse of dimensionality
- Qibo
  : structure similar to Trento
  - backends
    - cloud access (qibo-client)
  - simulation
    - state vector
    - tensor networks
    - Clifford
  - control
    : bridging together without losing capabilities
    - various electronics
  - calibration
    - monitoring
