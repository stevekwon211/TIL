

![Screenshot from 2021-01-04 22-17-42](https://user-images.githubusercontent.com/61633137/103539188-f37fad00-4eda-11eb-9385-09b973531a6a.png)

# Definition

- __Arthur Samuel__ (1959) : _Machine Learning_

> Field of study that gives computers the ability to learn without being explicitly programmed

<br>

- __Tom Mitchell__ (1998) : _Well-posed Learning Problem_

> A computer program is said to learn from experience __E__ with respect to some task __T__ and some performance measure __P__, 
> if its performance on __T__ , as measured by __P__ , improves with experience __F__

- _Example_
  - "Classifying as spam or not spam" => __T__
  - "Watching someone label emails as spam or not spam" => __E__
  - "The number (or fraction) of emails correctly classified as spam/not spam" => __P__

<br>

# Machine Learning Algorithms

## __Supervised learning__

-  Given the __"right answers"__ for each example data
- __Regression__ predict __continuous__ valued output
- __Classification__ gives __discrete__ valued output (0 or 1)
- _Example_
  - Predict how many of items will sell over the next 3 months => __Regression__
  - Given a picture of a person, we have to predict their age on the basis of the given picture => __Regression__
  - Examine individual customer accounts, and decide if it has been hacked or compromised => __Classification__
  - Given a patient with a tumor, we have to predict whether the tumor is malignant or benign => __Classification__

<br>

## __Unsupervised learning__

- It allows us to approach problems with no idea what the result will look like.
- Unsupervised learning is used for such as __organize computing clusters__, __social network analysis__, __market segmentation, astronomical data analysis__.
- __Clustering Example__

  - Take a collection of 1,000,000 different genes, and find a way to automatically group these genes into groups that are somehow similar or related by different variables, such as lifespan, location, roles, and so on.
- __Non-clustering Example__
- The "Cocktail Party Algorithm", allows you to find structure in a chaotic environment.
- _Example_

  - Given a set of news articles found on the web, group them into set of articles about the same story
  - Given a database to customer data, automatically discover market segments and group customers into different market segments

<br>