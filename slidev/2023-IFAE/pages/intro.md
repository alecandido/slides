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

Le due maggiori novità introdotte da NNPDF 4.0 sono state:
- una **migliore metodologia**, basata su tecniche note di Machine Learning 
- una crescita consistente nel numero di **nuovi pacchetti di dati da LHC**.

<div w="full" flex="~" justify="center" items="center" m="y-12">
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

Definisce la dipendenza delle PDF dalla scala non fisica $\mu_F$


<div flex="~ gap-8" justify="evenly" w="full" m="8">
  <section flex="~ col" justify="center">

$$
  \mu^2 \frac{\text{d}{\textbf{f}}}{\text{d}\mu^2}(\mu^2) = \textbf{P} (a_s(\mu^2),\mu^2) \otimes \textbf{f}(\mu^2)
$$

  </section>
  <section flex="~ col" justify="center">
    <bkg-img src="ev-op.svg" p="6" w="md"/>
  </section>
</div>


Queste equazioni definoscono un insieme di **operatori lineari** $\textbf{E}(\mu^2 \leftarrow
\mu_0^2)$ **sulle PDF**:

$$
  \textbf{f}(\mu^2) = \textbf{E}(\mu^2 \leftarrow \mu_0^2) \otimes \textbf{f}(\mu_0^2)
$$

<div m="t-12 b-12">
Per generarli, abbiamo scritto una libreria dedicata: <b>Evolutionary Kernel Operator
(EKO)</b>

<div w="full" flex="~" justify="end" m="t--12">
  <cite-arxiv aref="2202.02338" right="0" class="relative"/>
</div>
</div>

<div m="t-6 b-6" flex="~" justify="center">
  <bkg-img src="eko.png" p="2" w="1/5"/>
</div>
