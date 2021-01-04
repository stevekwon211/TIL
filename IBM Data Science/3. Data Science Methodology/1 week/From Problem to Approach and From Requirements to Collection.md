![](https://cdn.pixabay.com/photo/2016/02/19/11/19/office-1209640_960_720.jpg)

# From Problem to Approach

## 1. Business Understanding

- What is the problem that you are trying to solve?
- Business Understanding allows you to determine which analytic approach is needed to address the question

## 2. Analytic approach

- How can you use data to answer the question?
- Which __analytic approach__ to pick?
  1. __Descriptive__
     - Current status
  2. __Diagnostic__ (Statistical Analysis)
     - What happened?
     - Why is this happening?
  3. __Predictive__ (Forecasting)
     - What if these trends continue?
     - What will happen next?
  4. __Prescriptive__
     - How do we solve it?
- What are the __types__ of questions? : The correct approach depends on business requirements for the model
  1. If the question is to __determine probabilities of an action__
     - Use a __Predictive model__
  2. If the question is to __show relationships__
     - Use a __Descriptive model__
  3. If the question __requires a yes & no answer__
     - Use a __Classification model__

### Will machine learning be utilized?

- Learning without being explicitly programmed
- Identifies relationships and trends in data that might otherwise not be accessible or identified
- Uses clustering association approaches

# From Requirements to Collection

## 1. Data Requirements

- What are data requirements?

### Examples - Selecting the cohort

- __Define and select cohort__
  - In-patient within health insurance provider's service area
  - Primary diagnosis of __CHF__ in one year
  - Continuous enrollment for at least 6 months prior to primary __CHF__ admission
  - Disqualifying conditions

### Examples - Defining the data

- Content, formats, representations suitable for decision tree classifier
  - One record per patient with column representing variables (dependent variable and predictors)
  - Content covering all aspects of each patient;s clinical history
    - Transactional format
    - Transformations required

## 2. Data Collection

- What occurs during data collection?

### Gathering available data

- Available data sources
  - Corporate data warehouse (single source of medical & claims, eligibility, provider and member information)
  - In-patient record system
  - Claim payment system
  - Disease management program information

### Deferring Inaccessible data

- Data wanted but not available
  - Pharmaceutical records
  - Decided to defer

### Example - Merging data

- Eliminate redundant data

