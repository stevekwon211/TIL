![](https://cdn.pixabay.com/photo/2016/10/09/08/32/digital-marketing-1725340_960_720.jpg)

# From Understanding to Preparation

## 1. Data Understanding

- What does it mean to "prepare" or "clean" data?

### Understanding the data

- __Descriptive statistics__
  - _Univariate statistics_
  - _Pairwise correlations_
  - _Histogram_
    - Histograms are a good way to understand how values or a variable are distributed, and what sorts of data preparation may be needed to make the variable more useful in a model

### Looking at data quality

- __Data quality__
  - _Missing values_
  - _Invalid or misleading values_

### Iterative process

- Iterative data collection and understanding
  - Refined definition of "CHF admission"

## 2. Data Preparation

- What are ways in which data is prepared?

### Cleansing data

- Data preparation is __the most time consuming stage__ in a data science project
- Typically __70% or even 90%__ of the total project time is spent
- Automating some data collection and preparation processes in the database can reduce this time by as much as 50%.

### Transforming data

- Handle __missing or incorrect data__ and __eliminate duplication__
- Using __domain knowledge__ of data to build machine learning algorithms

### Using domain knowledge

- Feature engineering is the process of using domain knowledge of the data to create features that make the machine learning algorithms work
- Feature engineering is critical when machine learning tools are being applied to analyze the data

# From Modeling to Evaluation

## 1. Modeling

- In What way can the data be visualized to get to the answer that is required?
- Modeling is a step in data science methodology where data scientists can sample sources to determine if there are enough samples or more samples are needed

### Using Predictive or Descriptive?

- What is the purpose of data modeling?
  - Data modeling focuses on __developing technical__ or __predictable models__
- What are the characteristics of this process?
  - The prediction model wants to produce _Yes/No_ or _Stop/Move_ type results.
  - These models are based on __analytical approaches__ that are statistically driven or driven by machine learning.

### Using training / test sets

- Data scientists use __training sets__ for predictive modeling. A training set is a historical dataset that __already knows the results__ 
- The training set acts like a gauge that determines whether the model should be calibrated
- The data scientist will use __different algorithms__ to determine if a variable that is actually running is needed 
- The success of data compilation, preparation, and modeling depends on the understanding of the problem at hand and the appropriate approach to analysis

### Understanding the question

1. Understand the question at hard
2. Select an analytic approach or method to solve the problem
3. Obtain, understand, prepare, and model the data

## 2. Evaluation

- Does the model used really answer the initial question or does it need to be adjusted?

### Evaluating the model

- Model assessment is linked to __model construction__ , so modeling and evaluation steps are __repeated__
- Model evaluations are performed __during model development__ and __before the model is deployed__
- You can evaluate the quality of your model through evaluation, but you can also ensure that it meets your initial request

### When and how to adjust the model?

- __Diagnostic measures__
  - _Predictive Model_
    - You can use the __decision tree__ to assess whether the answers that can be output from the model are aligned in the initial design
    - It can be used to determine if there are areas that need to be adjusted
  - _Descriptive Model_
    - You can apply a test set with __known results__ and adjust the model as needed
- __Statistical Significance__
  - You can apply this type of assessment to the model to ensure that the data is processed and interpreted correctly within the model
  - This is to avoid unnecessary second guess when the correct answer is revealed