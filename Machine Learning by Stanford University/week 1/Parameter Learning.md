# Parameter Learning

## Gradient Descent

- Gradient descent is an __optimization algorithm__ for first-order approximation discovery 

  The slope of the function is repeated until the __absolute value of the slope is reached by continuously moving to the lower side.

- Algorithm: repeat until convergence { (for j = 0 and j = 1)
  $$
  \theta_j:=\theta_j-\alpha\frac{\delta}{\delta\theta_j}J(\theta_0,\theta_1)
  $$
  }
  alpha is a __learning rate__

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

  