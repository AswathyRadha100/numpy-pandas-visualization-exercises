# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # NUMPY: 
# ### NumPy is a very powerful library in Python that provides support for large, multi-dimensional arrays and matrices. NumPy enables vectorized operations, which means that you can apply operations on entire arrays at once, instead of using explicit loops. By using NumPy's vectorized operations, you can perform complex mathematical computations efficiently, making it a popular choice for scientific computing, data analysis, and machine learning tasks in Python. This efficiency and ease of use have made NumPy a fundamental building block for many other libraries and frameworks within the Python ecosystem.
#
#

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# #### 1. How many negative numbers are there?

negative_numbers = a < 0
len(a[negative_numbers])


# #### 2.How many positive numbers are there?

positive_numbers = a > 0
len(a[positive_numbers])

# #### 3.How many even positive numbers are there?

even_positive_numbers = (a > 0) & ( a % 2 == 0)
len(a[even_positive_numbers]) 

# #### 4. If you were to add 3 to each data point, how many positive numbers would there be?

positive_numbers = (a + 3) > 0
len(a[positive_numbers])


# #### 5.If you squared each number, what would the new mean and standard deviation be?

a.mean() ** 2

a.std() ** 2

# #### 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.

a - a.mean()

# #### 7. Calculate the z-score for each data point. Recall that the z-score is given by:
#
# #### Z=(x−μ)/σ
#

(a - a.mean()) / a.std()


# #### 8.Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

# +

Numpy introduction
## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# +
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])




# +
# Use python's built in functionality/operators to determine the followin
# -

# #### Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
#

def sum_of_a(nums):
    sum_list = 0
    for num in nums:
        sum_list = sum_list + num
    return sum_list
print(sum_of_a(a))

sum(a)


# #### Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
#

# +

def min_of_a(nums):
    num_list = []
    for num in nums:
        num_list.append(num)
    return min(num_list)
print(min_of_a(a))
        
# -

min(a)


# #### Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

def max_of_a(nums):
    num_list = []
    for num in nums:
        num_list.append(num)
    return max(num_list)
print(max_of_a(a))


max(a)


# #### Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
#

def mean_of_a(nums):
    sum_num = 0
    for num in nums:
        sum_num = sum_num + num           
        avg = sum_num / len(nums)
    return avg
print(mean_of_a(a))


# #### Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
#

def product_of_a(nums):
    aggregate = 1
    for num in nums:
        aggregate *= num
    return (aggregate)  
print(product_of_a(a))


# #### Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

def squares_of_a(nums):
    squares_list = []
    for num in nums:
        squares_list.append(num**2)
    return (squares_list)
print(squares_of_a(a))

[i**2 for i in a]


# #### Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
#

def odds_in_a(nums):
    num_list = []
    for num in nums:
        if num % 2 != 0:
            num_list.append(num)
    return (num_list)
print(odds_in_a(a))


[i for i in a if i% 2 ==1]


# #### Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
#

def even_in_a(nums):
    num_list = []
    for num in nums:
        if num % 2 == 0:
            num_list.append(num)
    return (num_list) 
print(even_in_a(a))


[i for i in a if i% 2 ==0]

# ### Two dimensions array

# #### What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
# #### Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
# b = [
#     [3, 4, 5],
#     [6, 7, 8]
# ]
#

# +



b = np.array([
    [3, 4, 5],
    [6, 7, 8]
])



# +
# or

b = np.array(b)
# -

# #### Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)
#

sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
print(sum_of_b)

b.sum()

# #### Exercise 2 - refactor the following to use numpy. 
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
#

min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
print(min_of_b)

b.min() 


# #### Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
#

max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
print(max_of_b)

b.max()  

# #### Exercise 4 - refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
#

mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
print(mean_of_b)

b.mean()  

# #### Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)
#

# +


sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
print(sum_of_b)


# -

b.sum()


# #### Exercise 2 - refactor the following to use numpy. 
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])
print(min_of_b)

b.min() 


#  #### Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
#

max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
print(max_of_b)

b.max()

#  #### Exercise 4 - refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
#

mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
print(mean_of_b)

b.mean()

# #### Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number

product_of_b = 1 
for row in b: 
    for number in row:
        product_of_b *= number
print(product_of_b)

b.prod()  


# #### Exercise 6 - refactor the following to use numpy to find the list of squares 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)
#
#

# +
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
        
print(squares_of_b)        

# +

b**2 

# -

# #### Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)
#

odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
print(odds_in_b)            

# +

b[b % 2 == 1]   
# -

# #### Exercise 8 - refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)
#

evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
print(evens_in_b)            

b[b % 2 == 0]


# #### Exercise 9 - print out the shape of the array b.
#

b.shape

# #### Exercise 10 - transpose the array b.
#

b.transpose()

#or
np.transpose(b)

#or
b.T

# #### Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b.reshape(1,6)


#or
np.reshape(b,(1,6))

#or
np.reshape(b,(6))

# #### Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
#

b.reshape((6,1)) 

# #### Setup 3
#
# c = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#

c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# #### HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
#

# #### Exercise 1 - Find the min, max, sum, and product of c.
#

c.min()

c.max()

c.sum()

c.prod()

# #### Exercise 2 - Determine the standard deviation of c.
#

c.std()

# #### Exercise 3 - Determine the variance of c.

np.var(c)

c.var()

sum(sum((c - c.mean())**2 / 9))

# #### Exercise 4 - Print out the shape of the array c

c.shape

# #### Exercise 5 - Transpose c and print out transposed result.

c.transpose() 

# ####  Exercise 6 - Get the dot product of the array c with c. 
#

np.dot(c,c)

# #### Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
#

#linear algebra concept
sum(sum(c * c.transpose()))

# #### Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
#

c.prod() * c.transpose().prod()

# ### Setup 4
# d = [
#     [90, 30, 45, 0, 120, 180],
#     [45, -90, -30, 270, 90, 0],
#     [60, 45, -45, 90, -45, 180]
# ]
#
#
#
#

d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])


# #### Exercise 1 - Find the sine of all the numbers in d
#

np.sin(d)

# #### Exercise 2 - Find the cosine of all the numbers in d

np.cos(d)

# #### Exercise 3 - Find the tangent of all the numbers in d

np.tan(d)

# #### Exercise 4 - Find all the negative numbers in d

negative_numbers = d < 0
(d[negative_numbers])


# #### Exercise 5 - Find all the positive numbers in d

positive_numbers = d > 0
(d[positive_numbers])


# #### Exercise 6 - Return an array of only the unique numbers in d.

np.unique(d)

# #### Exercise 7 - Determine how many unique numbers there are in d.

len(np.unique(d))

# #### Exercise 8 - Print out the shape of d.

d.shape

# #### Exercise 9 - Transpose and then print out the shape of d.

d.transpose().shape

#or
d.T.shape

# #### Exercise 10 - Reshape d into an array of 9 x 2

d.reshape(9,2)
