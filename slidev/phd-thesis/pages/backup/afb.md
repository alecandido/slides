# Drell--Yan Forward-Backward Asymmetry

<div w="full" flex="~" justify="end" m="t--8">
  <cite-arxiv aref="2209.08115" right="0" class="relative"/>
</div>

This is an interesting case study for PDF extrapolation.

<div m="y-8" class="flex justify-center">
  <bkg-img src="afb/diagram.png" p="2" w="3/7"/>
</div>

$$
A_{\text{fb}}(\cos\theta^*) \equiv \frac{\frac{\text{d}\sigma}{\text{d}\cos\theta^*}(\cos\theta^*)
- \frac{\text{d}\sigma}{\text{d}\cos\theta^*}(-\cos\theta^*)}{ \frac{\text{d}\sigma}{\text{d}\cos\theta^*}(\cos\theta^*)
+ \frac{\text{d}\sigma}{\text{d}\cos\theta^*}(-\cos\theta^*) } \, ,\quad \cos\theta^*>0
$$

---

# Extrapolation

<div m="t--4 b--2" class="flex justify-center">
  <bkg-img src="afb/coupling-ratio.png" p="2" w="3/7"
    hover="scale-170 translate-y-15" transition="700"/>
</div>

LO expression:
$$
A_{\text{fb}}(\cos\theta^*)   = \frac{\cos\theta^*}{(1+\cos^2(\theta^*))}R_{\text{fb}}
\qquad
R_{\text{fb}}\equiv \frac{\sum_q g_{A,q}}{\sum_{q'} g_{S,{q'}}}
$$

$$
g_{A,q} =\frac{\pi \alpha^2}{3 s}
\int\limits_{m_{\ell\bar{\ell}}^{\text{min}}}^{\sqrt s}
\frac{\text{d}m_{\ell\bar{\ell}}}{m_{\ell\bar{\ell}}}A_{q}(m)\!\!\int\limits_{\log(m_{\ell\bar{\ell}}/\sqrt
s)}^{\log(\sqrt s/m_{\ell\bar{\ell}})}\!\!\text{d}y_{\ell\bar{\ell}}\,
\mathcal{L}_{A,q}(m_{\ell\bar{\ell}},y_{\ell\bar{\ell}})
$$

---

# $R_{\text{fb}}$ relative uncertainty

<div m="y-20"/>

<div m="y-2" flex="~ row" justify="around" items="center" w="full">
  <bkg-img src="afb/rfb-absolute-unc.png" p="2" w="34/70"
    hover="scale-130 translate-x-25" transition="700"/>
  <bkg-img src="afb/rfb-relative-unc.png" p="2" w="34/70"
    hover="scale-130 translate-x--25" transition="700"/>
</div>

---

# The NLO picture

<div m="y-24"/>

<div m="y-2" flex="~ row" justify="around" items="center" w="full">
  <bkg-img src="afb/nlo-lower.png" p="2" w="34/70"
    hover="scale-170 translate-x-35" transition="700"/>
  <bkg-img src="afb/nlo-higher.png" p="2" w="34/70"
    hover="scale-170 translate-x--35" transition="700"/>
</div>
