# Let's go Bayesian

## Fitting 101

All of the steps accompanied with pictures

- you take a bunch of point with a known underlying low, and rather small errors
  - a parabola, with ~10 points resolving well the curvature (small errors
    compared to curvature)
  - this is our beautiful BSM
- you then take your simple model and try to fit it
  - a line
  - our poorly describing SM
- the result of your fit is: a very **large chi2**

Let's stop here: the moment you obtain a very large chi2 for your best fit, you
know something is not working. This might well be an evidence for something new!

Now let's instead resume the usual procedure:

- you kick out some data, claiming they are old and there were limitations in
  the systematics control and so on
  - your chi2 improves, but it is still not enough
    - picture: remove points at random, ~20%
  - data selection can hide some new physics, but if few data are removed, and
    they don't cover any special kinematic range, not much is going to change
    - picture: remove massive amount of points, it almost works (red cross)
    - picture: remove points all one side of parabola, it works almost perfectly (red cross)
- now the final ingredient: tolerance, i.e. you arbitrarily raised the error on
  your parameters
  - finally you managed to get a parabola inside a line uncertainty, regardless
    of data uncertainties (that were clearly saying: we have small errors, this
    is a parabola and we resolving it well)

If your Standard Model has not enough parameters for this, no problem: PDF at
rescue.
We have all parameters and uncertainty we need to hide New Physics.

But then if Standard Model is really a line, what is supposed to be the PDF?

- a line as well?
- a parabola?
- a higher order polynomial?

We don't know, so one way is to assume an object that is general enough to
describe what we see in data.
But then we are back again! Maybe we won't blow uncertainties, but we have
"enough parameters to fit an elephant" (cit. JCM).

We need some less controversial assumptions.

But what can we tell about an unknown function, without theoretical insight on
the way it is generated.
Well, we have a clue about the "natural variable" to express this function with,
and this is already a measure. Then, if we are "hunting for features", we know
we can't resolve high frequency/short distance features, before we understand
the long distance one. Moreover, other constraint (e.g. sum rules) are already
telling us something about this functions. We should put clues together...

## Neural

So, why not to use techniques that have already been proved successful?

For example: let's replace polynomial parameterization with a Neural Network!
(here NNPDF logo)

- this is a nice idea:
  - you will need some time to adapt the techniques to the specific needs, since
    the usual problems they are solving is rather different
  - you will obtain a very more general result: errors are small and smaller
    only where data are constraining it, and much larger only where there are
    not sufficient data
    - for PDFs larger error are, e.g., in the large-x region
- but you have to motivate your performances
  - how can we tell it is good, if there is no single number as the chi2 we can
    compare? (there is the test chi2 and the loss function, but to some
    extent this is engineered on purpose)
  - it is going to be heavily tested, but: how many tests are enough?
  - if closure tested: should it behave differently on data that are not real
    data? working well on fake data is a guarantee it will perform well also on
    real ones

There will be always people complaining about your _black box_.
(picture: black box with white question marks on faces)
(cite: CTEQ paper/hopscotch procedure)

But what is doing the _black box_ for you? It is making assumptions,
essentially, the same reasonable assumptions we discussed above.

But maybe, in a mathematically clear problem, there are simpler way to make
assumptions on your unknown objects: choosing an **explicit prior**.

## Bayesian

The Bayes theorem is extremely simple, and the likelihood (essentially a
multi-Gaussian) we were already consuming as loss-function in all previous
attempts.

Then:

- the only **ingredient** we miss is a prior; before our prior was spelled out as
  cuts in our space (slicing the polynomials of given order subspace) or
  implicit in training algorithm used (the neural network); but we can do more
  then assigning a {0,1} weight (we have real numbers at hand) and we can
  explain it better than just a model that works
  - picture: 2-D slice of 3-D space
  - picture: NN
- the **result** we'll get will be greatly improved: instead of a Gaussian
  distribution in parameter space (polynomial fit) or the outcome of a complex
  procedure (propagate through pseudo-data replicas) we will get a distribution,
  and an analytically derived one

Point is what prior should be choose?
Now we are forced to decide, but that's a good thing: we were choosing even
before, simply it was less explicit.

A sensible choice for a function space is a Gaussian process.
Why?

- because a Gaussian is a sensible choice for a generic random variable:
  describes the distribution just in term of an average and covariance, so it's
  the minimal choice
- which average? It doesn't matter so much, as long as there is enough variance
- but how to constraints? The covariance

The covariance will be a bilinear kernel on the function domain, and it can
encode a lot of information.
In particular, the kernel can be engineered to respect the structures already
present in the space, like the metric and the measure.

The prior is then encoding the true information that we have about our unknown
object, being general enough, but not more general to allow for things we
consider extremely unlikely.
Doing this, it is reducing the complexity of the space.

## Extra MCPDF complications

In practice:

## Resources

https://mlu-explain.github.io/double-descent/
