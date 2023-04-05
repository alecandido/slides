---
layout: cols
---

# Funzioni partoniche (PDF)

<div w="full" flex="~" justify="end" m="t--8 b-4">
  <cite-arxiv aref="2109.02653" right="0" class="relative"/>
</div>

La definizione delle PDF è una conseguenza di una proprietà della Cromodinamica
Quantistica (QCD): la *fattorizzazione*

$$
\sigma = \hat{\sigma} \otimes f + \mathcal{O}(\Lambda^2/Q^2)
$$

<div grid="~ cols-2 gap-8" m="8">
  <bkg-img src="pdfs/40-q3.svg" p="x-6"/>
  <bkg-img src="pdfs/40-q100.svg" p="x-6"/>
</div>

Per ottenere un intero **PDF set** sono necessari molti ingredienti...

---

<div m="y--2"/>

Le due maggiori novità introdotte da NNPDF 4.0 sono state:
- una **migliore metodologia**, basata su tecniche note di Machine Learning 
- una crescita consistente nel numero di **nuovi pacchetti di dati da LHC**.

<div w="full" flex="~" justify="center" items="center" m="y-8">
  <bkg-img src="organization.png" w="150" p="8"/>
</div>

Invece, l'apparato per le predizioni teoriche è rimasto piuttosto consistente
con le versioni precedenti, anche se l'applicazione è stata estesa ai nuovi
dati.

---
layout: cols
---

# Evoluzione perturbativa (DGLAP)

<div/>

<div grid="~ cols-3 gap-8" justify="left" w="10/11" m="y--3 l-30">
  <section flex="~ col" justify="center">

Definiscono la dipendenza delle PDF dalla scala non fisica $\mu_F$


  </section>
  <section flex="~ col" justify="center" m="r-8">

$$
  \mu^2 \frac{\text{d}{\textbf{f}}}{\text{d}\mu^2}(\mu^2) = \textbf{P} (a_s(\mu^2),\mu^2) \otimes \textbf{f}(\mu^2)
$$

  </section>
</div>


Queste equazioni definoscono un insieme di **operatori lineari** $\textbf{E}(\mu^2 \leftarrow
\mu_0^2)$ **sulle PDF**:

<div flex="~ gap-8" justify="evenly" w="full" m="4">
  <section flex="~ col" justify="center">

$$
  \textbf{f}(\mu^2) = \textbf{E}(\mu^2 \leftarrow \mu_0^2) \otimes \textbf{f}(\mu_0^2)
$$

  </section>
  <section flex="~ col" justify="center">
    <bkg-img src="ev-op.svg" p="6" w="md"/>
  </section>
</div>


<div m="t-12">
Per generarli, abbiamo scritto una libreria dedicata: <b><a
href="https://github.com/NNPDF/eko">Evolutionary Kernel Operator (EKO)</a></b>

<div w="full" flex="~" justify="end" m="t-2">
  <cite-arxiv aref="2202.02338" right="0" class="relative"/>
</div>
</div>

<div flex="~" justify="center" m="t--4">
  <bkg-img src="eko.png" p="2" w="1/5"/>
</div>
