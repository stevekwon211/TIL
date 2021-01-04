# Model and Cost Function

## Model Representation

- Input variables (Input features)
  $$
  x^{(i)}
  $$

- Output variables (Target variables)
  $$
  y^{(i)}
  $$

- A list of training example
  $$
  (x^{(i)},y^{(i)});i = 1, ...,m
  $$
  ___m___ is called a __training set__

![Untitled Diagram (1)](https://user-images.githubusercontent.com/61633137/103527035-18692580-4ec5-11eb-9ef8-2313d878379b.png) 

- How do we represent _h_?

$$
h_\theta(x) = \theta_0 + \theta_1x
$$

- Linear regression with one variable.
  Univariate linear regression.

<br>

## Cost Function

- We can measure the accuracy of our hypothesis function by using a **cost function**. 
  This takes an average difference (actually a fancier version of an average) of all the results of the hypothesis with inputs from x's and the actual output y's.

- __Squared error function__ or __Mean squared error__
  $$
  J(\theta_0,\theta_1) = \frac{1}{2m}\sum_{i=1}^m(\hat{y_i} - y_i)^2 = \frac{1}{2m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})^2
  $$

- The mean is halved (1/2) as a convenience for the computation of the __gradient descent__, as the derivative term of the square function will cancel out the (1/2) term.

<br>

## Revision

- Hypothesis
  $$
  h_\theta(x) = \theta_0 + \theta_1x
  $$

- Parameters
  $$
  \theta_0, \theta_1
  $$

- Cost Function
  $$
  J(\theta_0,\theta_1) = \frac{1}{2m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})^2
  $$

- Goal = _Minimize Parameters_
  $$
  J(\theta_0, \theta_1)
  $$
  

<br>

## Simplified Formula

- Hypothesis
  $$
  h_\theta= \theta_1x
  $$

- Parameters
  $$
  \theta_1
  $$

- Cost Function
  $$
  J(\theta_1) = \frac{1}{2m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})^2
  $$
  <br>
  $$
  h_\theta(x^{(i)}) = \theta_1x^{(i)}
  $$
  
- Goal = _Minimize Parameters_
  $$
  J(\theta_1)
  $$

<br>

