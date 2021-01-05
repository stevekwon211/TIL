# Parameter Learning

## Gradient Descent

- Gradient descent is an __optimization algorithm__ for first-order approximation discovery 

  The slope of the function is repeated until the __absolute value of the slope is reached by continuously moving to the lower side.

- Algorithm: repeat until convergence { (for j = 0 and j = 1)
  $$
  \theta_j:=\theta_j-\alpha\frac{\delta}{\delta\theta_j}J(\theta_0,\theta_1)
  $$
  }
  ___a___ (alpha) is a __learning rate__

<br>

- Simultaneous update
  $$
  temp0 := \theta_0 - \alpha\frac{\delta}{\delta\theta_0}J(\theta_0,\theta_1)
  $$

  $$
  temp1 := \theta_1 - \alpha\frac{\delta}{\delta\theta_1}J(\theta_0,\theta_1)
  $$

  $$
  \theta_0 := temp0
  $$

  $$
  \theta_1 := temp1
  $$


<br>

- Parameter ___a___ (alpha)
  $$
  \theta_1 := \theta_1 - \alpha\frac{\delta}{\delta\theta_1}J(\theta_0,\theta_1)
  $$

  ![Screenshot from 2021-01-05 20-26-05](https://user-images.githubusercontent.com/61633137/103641063-7f094480-4f94-11eb-982c-bb85a4441981.png) 
  (_source: Machine Learning by Stanford_)

  - If ___a___ is too small, gradient descent can be slow
  - If ___a___ is too large, gradient descent can overshoot the minimum, it may fail to converge, or even diverge

<br>

- How does gradient descent converge with a fixed step size ___a___?

  - The intuition behind the convergence is that 
    $$
    \frac{d}{d\theta_1}J(\theta_1)
    $$
    approaches __0__ as we approach the bottom of our convex function. At the minimum, the derivative will always be 0 and thus we get
    $$
    \theta_1 := \theta_1 - \alpha * 0
    $$

<br>

## Gradient Descent For Linear Regression

- Gradient descent algorithm repeat until convergence { (for j = 0 and j = 1)
  $$
  \theta_j:=\theta_j-\alpha\frac{\delta}{\delta\theta_j}J(\theta_0,\theta_1)
  $$
  }

<br>

- Linear Regression Model
  $$
  h_\theta(x) = \theta_0 + \theta_1x
  $$
  
  $$
  J(\theta_0,\theta_1) = \frac{1}{2m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})^2
  $$
  

<br>

- Derivation of 

$$
\frac{\delta}{\delta\theta_j}J(\theta_0,\theta_1)
$$

​	   =>
$$
= \frac{\delta}{\delta\theta_j}*\frac{1}{2}(h_\theta(x)-y)^2
$$

$$
= 2 * \frac{1}{2}(h_\theta(x)-y)*\frac{\delta}{\delta\theta_j}(h_0(x)-y)
$$

$$
= (h_\theta(x)-y)*\frac{\delta}{\delta\theta_j}(\sum_{i=0}^n\theta_ix_i-y)
$$

$$
= (h_\theta(x)-y)x_j
$$

<br>

## Summary

- Gradient descent can converge to a __local minimum__ , even with the learning rate ___a___ fixed.

$$
\theta_1 := \theta_1 - \alpha\frac{\delta}{\delta\theta_1}J(\theta_0,\theta_1)
$$

- As we approach a local minimum, gradient descent will automatically take smaller steps.
  So, no need to decrease ___a___ over time.

<br>