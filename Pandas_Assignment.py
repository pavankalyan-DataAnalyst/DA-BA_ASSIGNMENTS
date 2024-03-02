#!/usr/bin/env python
# coding: utf-8

# # <center>Pandas Assignment</center>

# Import pandas and numpy with their aliases

# In[6]:


import pandas as pd
import numpy as np



# Create a variable a = pd.Series([ 100, 200, 300, 400])

# In[7]:


a = pd.Series([100, 200, 300, 400])
print(a)


# Print a, and data type

# In[8]:


print(a)
print("\nData type of Series 'a':", type(a))


# Using indexing access the element 300 from the series a.

# In[9]:


element_300 = a[2]
print("Element 300 from the Series 'a':", element_300)


# What are the values of index for series a?

# In[10]:


a = pd.Series([100, 200, 300, 400])
print("Index values for Series 'a':", a.index)


# Change the index to  ['c', 'a', 'b', 'd']

# In[11]:


a.index = ['c', 'a', 'b', 'd']
print("Series 'a' with new index:")
print(a)


# Access the value in the series with index 'd'

# In[12]:


value_d = a['d']
print("Value in the Series with index 'd':", value_d)


# Sort the values wrt to the index and print it

# In[13]:


sorted_a = a.sort_index()
print("Sorted Series 'a' with respect to the index:")
print(sorted_a)




# Create a new Pandas Series b having index as 'e', 'f', and 'g' and value 800,450,100 and print it

# In[14]:


b = pd.Series([800, 450, 100], index=['e', 'f', 'g'])

# Printing the Series 'b'
print(b)






# Append b series at the end of a series

# In[15]:


a_appended = pd.concat([a, b])

# Printing the appended Series
print("Appended Series:")
print(a_appended)


# In[16]:


#print a again after appending b into it
print(a_appended)




# Sort the values in descending order of a and print the index of the sorted series

# In[17]:


sorted_a_appended = a_appended.sort_values(ascending=False)

# Print the index of the sorted series
print(sorted_a_appended.index)


# ## Pandas DataFrame

# ### Part 1

# Create a pandas dataframe df from the series 'a' that we used in the last section, print the dataframe

# In[18]:


df = pd.DataFrame(a_appended, columns=['Values'])

print("DataFrame 'df' from Series 'a':")
print(df)


# What is the shape of the datafarme <br>
# (also, what does it imply?)

# In[19]:


print("Shape of the DataFrame 'df':", df.shape)


# Hey! remember shape (7,1) implies dataframe has 7 rows and 1 column. 

# What is the index of the dataframe, is it same as the series 'a' 

# In[20]:


# yep its same as the series.
print("Index of the DataFrame 'df':", df.index)


# print the head and tail of the dataframe. <br>
# Additional - (what does head and tali represent?)

# In[21]:


print("Head of the DataFrame 'df':")
print(df.head())


# In[22]:


print("\nTail of the DataFrame 'df':")
print(df.tail())


# Rename the column of the dataframe as 'points'

# In[23]:


df = df.rename(columns={'Values': 'points'})
print("DataFrame 'df' with column 'points':")
print(df)



# Create another Series 'fruits', which contains random names of fruits from ['orange','mango','apple']. The series should contain 7 elements, randomly selected from ['orange','mango','apple']

# In[24]:


#Create fruits array
import random
fruit_list = ['orange', 'mango', 'apple']
fruits = pd.Series(random.choices(fruit_list, k=7))
print("Series 'fruits' with random fruit names:")
print(fruits)





# In[25]:


#Create series fruits out of fruits array

fruits_array = ['orange', 'mango', 'apple', 'orange', 'mango', 'apple', 'orange']
fruits = pd.Series(fruits_array)
print("Series 'fruits' from the fruits array:")
print(fruits)




# Change the index of fruits to the index of dataframe df

# In[26]:


fruits.index = df.index
print("Series 'fruits' with the index matching DataFrame 'df':")
print(fruits)





# Add this fruits series as a new column to the dataframe df with its column name as 'fruits'
# <br>print the head of the dataframe to verify

# In[27]:


df['fruits'] = fruits


# In[28]:


print("Head of the DataFrame 'df' with the new 'fruits' column:")
print(df.head())


# ## Pandas Concatenation

# Create a dataframe  d1 where the cols are  ‘city’ : [‘Chandigarh’, ‘Delhi’, ‘Kanpur’, ‘Chennai’, ‘Manali’ ] and ‘Temperature’ : [15, 22, 20, 26,-2] 

# In[29]:


data = {
    'city': ['Chandigarh', 'Delhi', 'Kanpur', 'Chennai', 'Manali'],
    'Temperature': [15, 22, 20, 26, -2]
}

d1 = pd.DataFrame(data)


# Print(d1)

# In[30]:


print("DataFrame 'd1' with city and Temperature:")
print(d1)




# What is the shape of d1.

# In[31]:


d1.shape


# Set city = d1['city']

# In[32]:


city = d1['city']


# print city <br>
# What is the type of city.

# In[33]:


# Print the variable 'city'
print("Variable 'city':")
print(city)


# Create another datafeame 'd2' where the columns are <br>
# 'city' - ['Bengalaru','Coimbatore','Srirangam','Pondicherry'] <br>
# 'Temperature' - [24,35,36,39]

# In[34]:


# Creating the data for DataFrame 'd2'
data_d2 = {
    'city': ['Bengaluru', 'Coimbatore', 'Srirangam', 'Pondicherry'],
    'Temperature': [24, 35, 36, 39]
}

# Creating the DataFrame 'd2'
d2 = pd.DataFrame(data_d2)

# Printing the DataFrame 'd2'
print("DataFrame 'd2' with city and Temperature:")
print(d2)


# print the shape of this dataframe

# In[35]:


d2.shape


# merge the two dataframes together, save it in a new dataframe named 'd3'

# In[36]:


# d3 = 
d3 = pd.concat([d1, d2], ignore_index=True)
print("Merged DataFrame 'd3':")
print(d3)



# Select the part of the dataframe such that it contains cities wherer temp is less then or equal to 20 <br>
# How many cities are there? 

# In[37]:


selected_cities = d3[d3['Temperature'] <= 20]
print("Cities where temperature is less than or equal to 20:")
print(selected_cities)
num_cities = len(selected_cities)
print("Number of cities where temperature is less than or equal to 20:", num_cities)




# Select the part of the dataframe such that it contains the cities where tempearature greater than or equal to 35

# In[38]:


selected_cities_high_temp = d3[d3['Temperature'] >= 35]
print("Cities where temperature is greater than or equal to 35:")
print(selected_cities_high_temp)
num_cities_high_temp = len(selected_cities_high_temp)
print("Number of cities where temperature is greater than or equal to 35:", num_cities_high_temp)





# ## Applying functions to columns and creating new columns

# We need to create another column in d3, which contains  a boolean value for each city to indicate whether it's a union territory or not. 
# - HINT: Chandigarh, Pondicherry and Delhi are only 3 union territories here. 
# 

# In[54]:


def is_ut(city):
    union_territories = ['Chandigarh', 'Pondicherry', 'Delhi']
    if city in union_territories:
        return True
    else:
        return False
d3['is_ut'] = d3['city'].apply(is_ut)


# In[55]:


# print d3
print("DataFrame 'd3' with is_ut column:")
print(d3)


# The temperatures mentioned in ‘Temperature’ column are mentioned in Celsius, we need another column which contains the same in Fahrenheit. 

# HINT - 
# - Define a function c_to_f which takes input temp in celsius and returns a value with temperature in Fahrenheit.
# - To check: c_to_f(10) should return 50. 
# 

# In[56]:


# write function here

def c_to_f(celsius_temp):
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    return fahrenheit_temp
d3['Temperature_F'] = d3['Temperature'].apply(c_to_f)
print("DataFrame 'd3' with Temperature_F column (in Fahrenheit):")
print(d3)


# In[57]:


# check function c_to_f(10)
def c_to_f(celsius_temp):
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    return fahrenheit_temp

print("Temperature in Fahrenheit for 10 Celsius:", c_to_f(10))



# In[58]:


# apply function c_to_f to d3 to create a column 'temp_farenhiet'
d3['temp_fahrenheit'] = d3['Temperature'].apply(c_to_f)
print("DataFrame 'd3' with temp_fahrenheit column (in Fahrenheit):")
print(d3)




# ## Indexing and selecting rows in DataFrame

# Select subset of the dataframe d1 such that it contains the cities which are union territories.

# In[61]:


# List of union territories
union_territories = ['Chandigarh', 'Pondicherry', 'Delhi']
subset_d1_ut = d1[d1['city'].isin(union_territories)]
print("Subset of DataFrame d1 with cities that are union territories:")
print(subset_d1_ut)


# Select a subset of the dataframe d1 such that it contains the cities which only have temperature above 90 Farenhiet.

# In[62]:


subset_d1_above_90F = d1[d1['Temperature'] > 90]
print("Subset of DataFrame d1 with cities having temperatures above 90 Fahrenheit:")
print(subset_d1_above_90F)


# Select only the first three rows of the dataframe d1. 
# 

# In[63]:


subset_d1_first_three_rows = d1.iloc[:3]
print("First three rows of DataFrame d1:")
print(subset_d1_first_three_rows)


# Select all the rows and last two columns in the dataframe.
# 
# 
# 

# In[64]:


subset_d1_last_two_columns = d1.iloc[:, -2:]
print("All rows and last two columns of DataFrame d1:")
print(subset_d1_last_two_columns)


# ## Groupby

# In[65]:


# Create a dataframe using dictionary of your choice
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create a DataFrame using the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print("DataFrame created from dictionary:")
print(df)


# In[66]:


# Use Groupby of single column with aggregate sum()
# Sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Value': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)
result = df.groupby('Category').aggregate({'Value': 'sum'})
print(result)



# In[67]:


# Use Groupby of single column with aggregate count()

result = df.groupby('Category').aggregate({'Value': 'count'})
print(result)



# In[68]:


# Use Groupby of single column with aggregate min() and max()
result = df.groupby('Category').aggregate({'Value': ['min', 'max']})
print(result)


# In[69]:


# Use Groupby of any 2 columns with aggregate mean()
data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Subcategory': ['X', 'Y', 'X', 'Y', 'X'],
    'Value': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)
result = df.groupby(['Category', 'Subcategory']).aggregate({'Value': 'mean'})

# Print the result
print(result)


# In[70]:


# Use Groupby of any 2 columns with aggregate min() and max()
data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Subcategory': ['X', 'Y', 'X', 'Y', 'X'],
    'Value': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)
result = df.groupby(['Category', 'Subcategory']).aggregate({'Value': ['min', 'max']})

print(result)



# ## Data Range

# Create a pandas daterange where starting date is 1st of January,2020 and end date is 1st of April 2021, store it in a new variable named 'a'

# In[71]:


a = pd.date_range(start='2020-01-01', end='2021-04-01')


# print a

# In[72]:


print(a)


# What is the len of a?

# In[73]:


length_of_a = len(a)
print("Length of 'a':", length_of_a)


# What is the type of a?

# In[74]:


type_of_a = type(a)
print("Type of 'a':", type_of_a)

