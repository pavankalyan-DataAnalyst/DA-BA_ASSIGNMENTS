#!/usr/bin/env python
# coding: utf-8

# # <center> Numpy Basics </center>

# In[1]:


#import numpy module with alias np
import numpy as np


# We can create a NumPy ndarray object by using the array() function.
# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:
# 

# In[3]:


# Define a numpy array passing a list with  1,2 and 3 as elements in it
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)


# In[4]:


# print output
print(my_array)


# ## Dimensions in Arrays
# 
# Create arrays of different dimentions.
# 
# a=A numpy array with one single integer 10
# 
# b=A numpy array passing a list having a list= [1,2,3]
# 
# c=A numpy array passing nested list having [[1, 2, 3], [4, 5, 6]] as elements
# 
# d=A numpy array passing nested list having [[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]] as elements

# In[6]:


#define a,b,c and d as instructed above

a = np.array(10)
print("Array a:\n", a)
print("Shape of a:", a.shape)

b = np.array([1, 2, 3])
print("\nArray b:\n", b)
print("Shape of b:", b.shape)

c = np.array([[1, 2, 3], [4, 5, 6]])
print("\nArray c:\n", c)
print("Shape of c:", c.shape)

d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("\nArray d:\n", d)
print("Shape of d:", d.shape)


# Are you ready to check its dimention? Use ndim attribute on each variable to check its dimention

# In[7]:


#print dimentions of a,b, c and d
print("Dimension of array a:", a.ndim)
print("Dimension of array b:", b.ndim)
print("Dimension of array c:", c.ndim)
print("Dimension of array d:", d.ndim)


# Hey hey. Did you see! you have created 0-D,1-DeprecationWarning, 2-D and 3-D arrays.
# 
# Lets print there shape as well. You can check shape using shape attribute
# 
# 

# In[8]:


# print shape of each a,b ,c and d

print("Shape of array a:", a.shape)
print("Shape of array b:", b.shape)
print("Shape of array c:", c.shape)
print("Shape of array d:", d.shape)


# Lets check data type passed in our array. To check data type you can use dtype attribute

# In[9]:


# print data type of c and d
print("Data type of array a:", a.dtype)
print("Data type of array b:", b.dtype)
print("Data type of array c:", c.dtype)
print("Data type of array d:", d.dtype)


# Above output mean our array is having int type elements in it.

# Lets check the type of our variable. To check type of any numpy variable use type() function 

# In[10]:


#print type of a and b variable
print("Type of variable a:", type(a))
print("Type of variable b:", type(b))
print("Type of variable c:", type(c))
print("Type of variable d:", type(d))


# In[11]:


# Lets check length of array b, using len() function
len(b)


# Bravo!You have Defined ndarray i.e numpy array in variable a nd b. Also you have successfully learned how to create numpy. 

# Create two list l1 and l2 where, l1=[10,20,30] and l2=[40,50,60]
# Also define two numpy arrays l3,l4 where l3 has l1 as element and l4 has l2 as element
# 

# In[12]:


# Define l1,l2,l3 and l4 as stated above.
l1 = [10, 20, 30]
l2 = [40, 50, 60]
l3 = np.array(l1)
l4 = np.array(l2)
print("NumPy array l3:", l3)
print("NumPy array l4:", l4)


# Lets multiply each elements of l1 with corresponding elements of l2
# 
# Here use list comprehention to do so. Lets see how much you remember your work in other assignments.
# 
# Note: use %timeit as prefix before your line of code inorder to calculate total time taken to run that line<br>
# eg. %timeit my_code

# In[18]:


#code here as instructed above
get_ipython().run_line_magic('timeit', 'result = [x * y for x, y in zip(l1, l2)]')
result = [x * y for x, y in zip(l1, l2)]
print("Result using list comprehension:", result)


# Lets mulptiply l3 and l4
# 
# Note: use %timeit as prefix before your line of code inorder to calculate total time taken to run that line

# In[20]:


get_ipython().run_line_magic('timeit', 'res = [x * y for x, y in zip(l3, l4)]')
res = [x * y for x, y in zip(l1, l2)]
print("Result using list comprehension:", res)


# Don't worry if still your one line of code is running. Its because your system is calculating total time taken to run your code.
# 
# Did you notice buddy! time taken to multiply two lists takes more time than multiplyimg two numpy array.
# Hence proved that numpy arrays are faster than lists.
# 
# **Fun Fact time!:**
# 
# You know in many data science interviews it is asked that what is the difference between list and array.<br>
# 

# In[21]:


#Create a numpy array using arange with 1 and 11 as parameter in it
arr = np.arange(1, 11)
print("NumPy array created using arange:", arr)


# This means using arrange we get evenly spaced values within a given interval. Interval? Yes you can mention interval as well as third parameter in it.

# In[22]:


# Create an array using arange passing 1,11 and 2 as parameter in iter
arr = np.arange(1, 11, 2)
print("NumPy array created using arange:", arr)


# In[23]:


# create numpy array using eye function with 3 as passed parameter
arr = np.eye(3)
print("NumPy array created using eye function:")
print(arr)


# In[24]:


# Using arange() to generate numpy array x with numbers between 1 to 16
x = np.arange(1, 17)
print("NumPy array x with numbers between 1 to 16:")
print(x)


# In[25]:


# Reshape x with 2 rows and 8 columns
x_reshaped = x.reshape(2, 8)
print("Reshaped array with 2 rows and 8 columns:")
print(x_reshaped)


# As you can see above that our x changed into 2D matrix
# 
# 2. Reshaping 1-D to 3-D array
# 

# In[26]:


# reshape x with dimension that will have 2 arrays that contains 4 arrays, each with 2 elements:
x_reshaped = x.reshape(2, 4, 2)
print("Reshaped array with 2 arrays, each containing 4 arrays, each with 2 elements:")
print(x_reshaped)


# In[27]:


# Use unknown dimention to reshape x into 2-D numpy array with shape 4*4
x_reshaped = x.reshape(4, -1)
print("Reshaped array with shape 4*4:")
print(x_reshaped)




# In[28]:


# Use unknown dimention to  reshape x into 3-D numpy array with 2 arrays that contains 4 arrays
y = x.reshape(2, 4, -1)
print("Reshaped array y with 3-D structure:")
print(y)


# In[29]:


# Flattening y
y_flattened = y.flatten()
print("Flattened array y_flattened:")
print(y_flattened)


# In[30]:


# Create an array a with all even numbers between 1 to 17
a = np.arange(2, 18, 2)
print("Array a with all even numbers between 1 to 17:")
print(a)



# In[31]:


# Get third element in array a
third_element = a[2]
print("Third element in array a:", third_element)


# In[32]:


#Print 3rd, 5th, and 7th element in array a
print("3rd element in array a:", a[2])
print("5th element in array a:", a[4])
print("7th element in array a:", a[6])


# Lets check the same for 2 D array

# In[33]:


# Define an array 2-D a with [[1,2,3],[4,5,6],[7,8,9]] as its elements.
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("2-D array a:")
print(a)


# In[34]:


# print the 3rd element from the 3rd row of a
print("3rd element from the 3rd row of array a:", a[2, 2])


# Well done!
# 
# Now lets check indexing for 3 D array 

# In[35]:


# Define an array b again with [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]] as its elements.
b = np.array([[[1, 2, 3], [4, 5, 6]],
              [[7, 8, 9], [10, 11, 12]]])
print("Array b:")
print(b)


# In[36]:


# Print 3rd element from 2nd list which is 1st list in nested list passed. Confusing right? 'a' have nested array.Understand the braket differences.
print("3rd element from the 2nd list (1st list in nested list passed) in array b:", b[1, 0, 2])


# In[37]:


# Create 1D array
arr = np.array([1, 2, 3, 4, 5])
print("1D array arr:", arr)


# In[38]:


# Slice elements from 1st to 5th element from the following array:
sliced_arr = arr[0:5]
print("Sliced array:", sliced_arr)


# Note: The result includes the start index, but excludes the end index.
# 
# 

# In[41]:


# Slice elements from index 5 to the end of the array:
sliced_arr = arr[5:]
print("Sliced array from index 5 to the end:", sliced_arr)


# In[42]:


# Slice elements from the beginning to index 5 (not included):
sliced_arr = arr[:5]
print("Sliced array from the beginning to index 5 (not included):", sliced_arr)


# **STEP**
# 
# Use the step value to determine the step of the slicing:

# In[43]:


# Print every other element from index 1 to index 7:
every_other = arr[1:8:2]
print("Every other element from index 1 to index 7:", every_other)


# Did you see? using step you were able to get alternate elements within specified index numbers.

# In[44]:


# Return every other element from the entire array arr:
every_other = arr[::2]
print("Every other element from the entire array arr:", every_other)


# well done!
# 
# Lets do some slicing on 2-D array also. We already have 'a' as our 2-D array. We will use it here.
# 
# **Array slicing in 2-D array.**

# In[45]:


# Print array a
print("Array a:", a)


# In[46]:


# From the third element, slice elements from index 1 to index 5 (not included) from array 'a'
sliced_elements = a[2:, 1:5]
print("Sliced elements from index 1 to index 5 (not included) from the third element onward in array 'a':")
print(sliced_elements)


# In[47]:


# In array 'a' print index 2 from all the elements :
print("Index 2 from all elements in array 'a':", a[:, 2])


# In[48]:


# From all the elements in 'a', slice index 1 till end, this will return a 2-D array:
sliced_elements = a[:, 1:]
print("Sliced elements from index 1 till the end from all elements in array 'a':")
print(sliced_elements)


# Hurray! You have learned Slicing in Numpy array. Now you know to access any numpy array.

# ## Numpy copy vs view

# In[50]:


x1 = np.array([1, 2, 3, 4, 5])


# In[51]:


# assign x2 = x1
x2 = x1.copy()


# In[52]:


#print x1 and x2
print("Original array x1:", x1)
print("Modified copy x2:", x2)


# Ok now you have seen that both of them are same 

# In[54]:


# change 1st element of x2 as 10
x2[0] = 10


# In[55]:


#Again print x1 and x2
print("Original array x1:", x1)
print("Modified copy x2:", x2)


# In[56]:


# Check memory share between x1 and x2
if x2.base is x1:
    print("x2 is a view of x1")
else:
    print("x2 is not a view of x1")


# Hey It's True they both share memory
# 
# Shall we try **view()** function also likwise.

# In[57]:


# Create a view of x1 and store it in x3.
x3 = x1.view()


# In[58]:


# Again check memory share between x1 and x3
if x3.base is x1:
    print("x3 is a view of x1")
else:
    print("x3 is not a view of x1")


# Woh! simple assignment is similar to view. That means 
# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
# 
# Don't agree? ok lets change x3 and see if original array i.e. x1 also changes

# In[59]:


#Change 1st element of x3=100
x3[0] = 100
print("Modified x3:", x3)


# In[60]:


#print x1 and x3 to check if changes reflected in both
print("Original x1:", x1)
print("Modified x3:", x3)


# Now its proved.
# 
# Lets see how **Copy()** function works

# In[61]:


# Now create an array x4 which is copy of x1
x4 = x1.copy()


# In[62]:


# Change the last element of x4 as 900
x4[-1] = 900


# In[63]:


# print both x1 and x4 to check if changes reflected in both
print("Original x1:", x1)
print("Modified x4:", x4)


# Hey! such an intresting output. You noticed buddy! your original array didn't get changed on change of its copy ie. x4.
# 
# Still not convinced? Ok lets see if they both share memory or not

# In[64]:


#Check memory share between x1 and x4
if x4.base is None:
    print("x4 is a separate copy of x1 and does not share memory")
else:
    print("x4 shares memory with another array")


# **hstack vs vstack function**
# 
# 
# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
# 
# NumPy provides a helper function: 
# 
# 1. hstack() to stack along rows.
# 2. vstack()  to stack along columns

# In[65]:


# stack x1 and x4 along columns.
stacked_array = np.column_stack((x1, x4))
print("Stacked array along columns:")
print(stacked_array)


# In[66]:


#stack x1 and x4 along rows
stacked_array = np.vstack((x1, x4))
print("Stacked array along rows:")
print(stacked_array)


# We hope now you saw the difference between them.
# 
# Fun fact! you can even use concatenate() function to join 2 arrays along with the axis. If axis is not explicitly passed, it is taken as 0 ie. along column
# 
# Lets try this function as well

# In[67]:


arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])
arr2 = np.array([[7, 8, 9],
                 [10, 11, 12]])
# Join arr1 and arr2 along rows using concatenate() function
joined_array = np.concatenate((arr1, arr2), axis=0)
print("Joined array along rows:")
print(joined_array)


# In[68]:


##join arr1 and arr2 along columns using concatenate() function
joined_array = np.concatenate((arr1, arr2), axis=1)
print("Joined array along columns:")
print(joined_array)


# ## Adding, Insert and delete Numpy array

# You can also add 2 arrays using append() function also. This function appends values to end of array
# 
# Lets see how

# In[69]:


# append arr2 to arr1
appended_array = np.append(arr1, arr2, axis=0)
print("Appended array:")
print(appended_array)


# Lets use insert() function which Inserts values into array before specified index value

# In[70]:


# Inserts values into array x1 before index 4 with elements of x4
x1 = np.array([1, 2, 3, 4, 5])
x4 = np.array([10, 20, 30])


result_array = np.insert(x1, 4, x4)
print("Result array after insertion:")
print(result_array)


# You can see in above output we have inserted all the elements of x4 before index 4 in array x1.

# In[71]:


# delete 2nd element from array x2
x2 = np.array([1, 2, 3, 4, 5])
x2 = np.delete(x2, 1)
print("Updated array x2 after deleting the second element:")
print(x2)


# Did you see? 2 value is deleted from x2 which was at index position 2

# Good Job learner! 
