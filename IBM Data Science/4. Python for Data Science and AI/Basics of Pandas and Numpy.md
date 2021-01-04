# Pandas

## Importing Pandas

```python
import pandas as pd

csv_path = 'file1.csv' # road file1.csv file
df = pd.read_csv(csv_path) # convert file1.csv to dataframe
```

<br>

## Dataframes

```python
csv_path = 'file1.csv'
df = pd.read_csv(csv_path)
df.head() # show 0~4 rows in the dataframe
```

<br>

- Example

```Python
member = {'Name':['Kwon', 'Hyukil', 'Il', 'Steve'],
         'Age':[1, 11, 21, 31],
         'Favorite Color':['Red', 'Blue', 'Black', 'White']}

member_frame = pd.DataFrame(member)
member_frame
```

Result
 ![Screenshot from 2020-12-24 20-14-37](https://user-images.githubusercontent.com/61633137/103090326-189b3280-4634-11eb-90be-217e33d0f426.png)

<br>

```py
member_age = member_frame[['Age']]
member_age
```

Result
![Screenshot from 2020-12-24 20-17-16](https://user-images.githubusercontent.com/61633137/103090329-19cc5f80-4634-11eb-97f0-8f8956b5f98f.png)

<br>

## Using loc, iloc and ix

### loc

- __loc__ is __primarily labeled based__ ; when two arguments are used, you use __column headers__ and __row indexes__ to select the data you want.
  __loc__ can also take an integer as a row or column number
- Example

```Python
member = {'Name':['Kwon', 'Hyukil', 'Il', 'Steve'],
         'Age':[1, 11, 21, 31],
         'Favorite Color':['Red', 'Blue', 'Black', 'White']}
member_frame = pd.DataFrame(member)

member_frame.loc[0,'Name'] # Result => 'Kwon'
member_frame.loc[1,'Name'] # Result => 'Hyukil'
member_frame.loc[0,'Age'] # Result => 1
member_frame.loc[1,'Age'] # Result => 11
```

<br>

### iloc

- __iloc__ is __integer-based__. You use __column numbers__ and __row numbers__ to get rows or columns at particular positions in the data frame.
- Example

```Python
member = {'Name':['Kwon', 'Hyukil', 'Il', 'Steve'],
         'Age':[1, 11, 21, 31],
         'Favorite Color':['Red', 'Blue', 'Black', 'White']}
member_frame = pd.DataFrame(member)

member_frame.iloc[0,0] # Result => 'Kwon'
member_frame.iloc[1,0] # Result => 'Hyukil'
member_frame.iloc[0,1] # Result => 1
member_frame.iloc[1,1] # Result => 11
```

<br>

## Save as CSV

```Python
member_frame.to_csv('member_list.csv')
```

<br>

# Numpy

- __Numpy__ is a library for __scientific computing__. It has many useful functions. 

  There are many other advantages like __speed and memory__. 

  __Numpy__ is also the __basis for pandas__.

## One Dimensional Numpy

```Python
import numpy as np
a = np.array([0,1,2,3,4])

type(a) # Result => numpy.ndarray
a.dytpe # Result => dtype('int64')
a.size # number of elements in the array a, Result => 5
a.ndim # number of array dimensions or the rank of the array, Result => 1
a.shape # tuple of integers indicating the size of the array in each dimension, Result => (5,) 
```

<br>

### Indexing and Slicing

```Python
b = np.array([20,1,2,3,4])
b[0] = 100 # b => array([100,1,2,3,4])
b[4] = 0 # b => array([100,1,2,3,0])
b[3:5] = 300, 400 # b => array([100,1,2,300,400])
```

<br>

### Basic Operations

#### Vector Addition and Subtraction

```Python
u = np.array([1,0])
v = np.array([0,1])
z = u + v # z => array([1,1])
z = u - v # z => array([1,-1])
```

<br>

#### Array multiplication with a Scalar

```Python
y = np.array([1,2])
z = 2 * y # z => array([2,4])
```

<br>

#### Product of two numpy arrays

```Python
u = np.array([1,2])
v = np.array([3,2])
z = u * v # z => array([3,4])
```

<br>

#### Dot Product

```Python
u = np.array([1,2])
v = np.arrau([3,1])
z = np.dot(u,v) # z => 5
```

<br>

#### Adding Constant to an numpy array

```Python
u = np.array([1,2,3,-1])
z = u + 1 # z => array([2,3,4,0])
```

<br>

#### Universal Functions

```Python
a = np.array([1,-1,1,-1])
mean_a = a.mean() # mean_a => 0.0

b = np.arrau([1,-2,3,4,5])
max_b = b.max() # max_b => 5

np.pi # π 
x = np.array([0, np.pi/2], np.pi) # x = [0, π/2, π]
y = np.sin(x) # [sin(0), sin(π/2), sin(π)]
			  # y => [0,1,0]
```

<br>

#### Plotting Mathematical Functions

```Python
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

import matplotlib.pyplot as plt
%matplotlib inline
plt.plot(x,y)
```

Result
![Screenshot from 2020-12-24 22-37-13](https://user-images.githubusercontent.com/61633137/103091794-a711b300-4638-11eb-99e3-1b688ba33753.png)

<br>

