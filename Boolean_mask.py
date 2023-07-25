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

# # Goal:- Explore boolean Mask , .str attribute, Plot data from a Pandas Series
#
#

# ## Boolean Mask

# ### A boolean mask is a binary array or Series that serves as a filter to select specific elements from a data structure (like a Pandas Series or DataFrame) based on a set of conditions.It is a technique used to create a binary array or Series of boolean values (True or False) that is used to filter or subset data in pandas. It is essentially an array of boolean values (True or False) that has the same length as the data structure it is applied to. The True values in the mask indicate the positions of the elements that satisfy the given condition(s), and the False values indicate the positions of the elements that do not satisfy the condition(s). Boolean masks are commonly used in data analysis and manipulation tasks to perform various filtering operations, such as selecting rows that satisfy specific criteria, extracting values that meet certain conditions, or replacing values based on certain rules.

# ### Create a boolean mask 'mask' where each element in the Series greater than 30 will be set to True, and the elements less than or equal to 30 will be set to False. Then, apply this mask to the original Series 'series', resulting in a new Series subset_series that contains only the elements greater than 30.

# +
import pandas as pd

# Sample data
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Create a boolean mask to select elements greater than 30
mask = series > 30

# Applying the mask to the Series
subset_series = series[mask]

print(mask)
# Output: [False False False  True  True]

print(subset_series)
# Output:
# 3    40
# 4    50
# dtype: int64

# -

# ###  The length of the mask should match the length of the Series to ensure that the mask aligns properly with the elements in the Series

# +
# Example of an incorrect mask 
import pandas as pd

data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Incorrect mask with a different length
incorrect_mask = [True, False, True, False]  # here,length is 4 
#Hence, ValueError: boolean index did not match indexed array
#dimension is 5 but corresponding boolean dimension is 4

# Applying the incorrect mask to the Series will raise an error
subset_series = series[incorrect_mask]


# +
#corrected mask with the same length as the Series
import pandas as pd

data = [10, 20, 30, 40, 50]  # Length 5
series = pd.Series(data)

# Correct mask with the same length as the Series
correct_mask = [True, False, True, False, True]  # Length 5

# Applying the correct mask to the Series
subset_series = series[correct_mask]

print(subset_series)

# -

# ## .str attribute 

#
# ### The .str attribute  provides a convenient and powerful way to handle string data in a pandas Series, making it easier to clean, process, and manipulate text-based information.
#
#

#  Some commonly used string methods available through the .str attribute include:
#  
# 1. Lowercase and Uppercase Operations:
#
# .str.lower(): Converts all the characters in the strings to lowercase.
# .str.upper(): Converts all the characters in the strings to uppercase.


# 2.String Length:
#
# .str.len(): Returns the length of each string in the Series.


# 3. String Concatenation:
#
# .str.cat(): Concatenates strings in the Series with a specified separator.


# 4. Substrings and Slicing:
#
# .str.slice(): Extracts a substring from each string based on the provided start and end positions.
# .str.split(): Splits each string into multiple substrings based on a separator.
# .str.extract(): Extracts substrings using regular expressions.


# 5. String Replace:
#
# .str.replace(): Replaces substrings in each string with another substring.


# 6. String Strip:
#
# .str.strip(): Removes leading and trailing whitespace from each string.
# .str.lstrip(): Removes leading whitespace from each string.
# .str.rstrip(): Removes trailing whitespace from each string.


# 7. String Search and Count:
#
# .str.contains(): Checks if a substring is present in each string and returns a boolean mask.
# .str.startswith(): Checks if each string starts with a specified substring and returns a boolean mask.
# .str.endswith(): Checks if each string ends with a specified substring and returns a boolean mask.
# .str.count(): Counts the occurrences of a substring in each string.


# +
#Example to demonstrate some of these string methods
import pandas as pd

# Sample data with strings
data = ['apple', 'banana', 'orange', 'kiwi', 'grape']
series = pd.Series(data)

# String manipulation using the .str attribute
print(series.str.upper())
print(series.str.len())
print(series.str.cat(sep=' | '))
print(series.str.slice(start=1, stop=4))
print(series.str.replace('a', 'X'))
print(series.str.strip())
print(series.str.contains('an'))
print(series.str.count('a'))

# -

# # Plot data from a series

# ### To plot data from a pandas Series, you can use the matplotlib library, which is integrated with pandas for data visualization. Any plot created by pandas is a Matplotlib object.To use different plot types, you would use different functions provided by matplotlib, such as 
# ### plt.plot(), 
# ### plt.bar(), 
# ### plt.pie(), 
# ### plt.scatter() , etc.
#

# ## plt.plot()
#
# ### plt.plot() is used to create line plots in matplotlib. It is one of the most commonly used functions for visualizing one-dimensional data, such as time series or continuous data points. The function takes the x-axis values and y-axis values as its input and plots a line connecting the data points.

# +
#Line Plot example
import pandas as pd
import matplotlib.pyplot as plt

# Sample data for the Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Line Plot
plt.plot(series.index, series.values, marker='o', linestyle='-')
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Line Plot of the Series')
plt.show() # displays the plot


# series.index represents the x-axis values of the plot
# series.values represents the y-axis values of the plot
# marker='o'indicates that the data points will be represented as circles
# linestyle='-' indicates that a solid line will be connecting the data points
# -

# ## plt.bar()
#
# ### plt.bar() is a function in matplotlib used to create bar plots, which are used to display categorical data with rectangular bars of varying heights. Bar plots are commonly used to compare and visualize the distribution or relationship between different categories of data.

# ### plt.bar() Parameters:
#
# #### categories: The categories or labels for the bars. These can be a list of strings or any iterable representing the categorical data.
#
# #### values: The values corresponding to each category. These can be a list, array, or pandas Series representing the numerical data.
#
# #### color: (Optional) Specifies the color of the bars.
#
# #### width: (Optional) Specifies the width of the bars as a fraction of the total width of each group of bars.
#
# #### align: (Optional) Specifies how the bars are aligned relative to the category labels. The default is 'center'.
#
# #### label: (Optional) A label for the data series, useful for creating a legend.
#
#
#

# +
import matplotlib.pyplot as plt

# Sample data for the bar plot
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [20, 35, 30, 25]

# Creating the bar plot
plt.bar(categories, values, color='g', width=0., align='center', label='Data Series')

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')
plt.legend()

# Displaying the plot
plt.show()


#The bars are centered on each category label (align='center')
