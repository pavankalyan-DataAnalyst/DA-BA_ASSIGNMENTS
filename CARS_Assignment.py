#!/usr/bin/env python
# coding: utf-8

# <center> <h1 style="background-color:orange; color:white"><br>Exploratory Data Analysis<br></h1></center>

# # `Problem Statement:`
# We have used Cars dataset from kaggle  with features including make, model, year, engine, and other properties of the car used to predict its price.

# ## `Importing the necessary libraries`
# 
# 
# 
# 

# In[6]:


import pandas as pd
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)
from scipy import stats
import warnings
warnings.filterwarnings("ignore")


# ## `Load the dataset into dataframe`

# In[7]:


## load the csv file 
df = pd.read_csv("Cars_data.csv")


# In[8]:


## print the head of the dataframe
df.head()


# Now we observe the each features present in the dataset.<br>
# 
#  `Make:` The Make feature is the company name of the Car.<br>
# `Model:` The Model feature is the model or different version of Car models.<br>
# `Year:`  The year describes the model has been launched.<br>
# `Engine Fuel Type:` It defines the Fuel type of the car model.<br>
# `Engine HP:` It's say the Horsepower that refers to the power an engine produces.<br>
# `Engine Cylinders:` It define the nos of cylinders in present in the engine.<br>
# `Transmission Type:` It is the type of feature that describe about the car transmission type i.e Mannual or automatic.<br>
# `Driven_Wheels:` The type of wheel drive.<br>
# `No of doors:` It defined nos of doors present in the car.<br>
# `Market Category:` This features tells about the type of car or which category the car belongs. <br>
# `Vehicle Size:` It's say about the about car size.<br>
# `Vehicle Style:` The feature is all about the style that belongs to car.<br>
# `highway MPG:` The average a car will get while driving on an open stretch of road without stopping or starting, typically at a higher speed.<br>
# `city mpg:` City MPG refers to driving with occasional stopping and braking.<br>
# `Popularity:` It can refered to rating of that car or popularity of car.<br>
# `MSRP:` The price of that car.
# 
# 
# 
# 
# 
# 

# ## `Check the datatypes`

# In[11]:


# Get the datatypes of each columns number of records in each column
df.info()
data_types = df.dtypes
num_records = df.count()
data_info = pd.DataFrame({'Data Types': data_types, 'Number of Records': num_records})
print(data_info)


# ## `Dropping irrevalent columns`

# If we consider all columns present in the dataset then unneccessary columns will impact on the model's accuracy.<br>
# Not all the columns are important to us in the given dataframe, and hence we would drop the columns that are irrevalent to us. It would reflect our model's accucary so we need to drop them. Otherwise it will affect our model.
# 
# 
# The list cols_to_drop contains the names of the cols that are irrevalent, drop all these cols from the dataframe.
# 
# 
# `cols_to_drop = ["Engine Fuel Type", "Market Category", "Vehicle Style", "Popularity", "Number of Doors", "Vehicle Size"]`
# 
# These features are not neccessary to obtain the model's accucary. It does not contain any relevant information in the dataset. 

# In[13]:


# initialise cols_to_drop
cols_to_drop = ["Engine Fuel Type", "Market Category", "Vehicle Style", "Popularity", "Number of Doors", "Vehicle Size"]


# In[14]:


# drop the irrevalent cols and print the head of the dataframe
df = df.drop(columns=cols_to_drop)


# print df head
df.head()


# ## `Renaming the columns`

# Now, Its time for renaming the feature to useful feature name. It will help to use them in model training purpose.<br>
# 
# We have already dropped the unneccesary columns, and now we are left with useful columns. One extra thing that we would do is to rename the columns such that the name clearly represents the essence of the column.
# 
# The given dict represents (in key value pair) the previous name, and the new name for the dataframe columns

# In[15]:


# rename cols 
rename_cols = {"Make":"Manfactured_company",
               "Model":"Model",
               "Year":"Manfacture_Year",
               "Engine HP":"Engine_HP",
               "Engine Cylinders":"Engine_Cylinders",
               "Transmission Type":"Transmission_Type",
               "Driven_Wheels":"Driven_Wheels",
               "highway MPG":"highway_MPG",
               "city mpg":"city_mpg",
               "MSRP":"MSR_Price"
}


# In[16]:


# use a pandas function to rename the current columns - 
df = df.rename(columns=rename_cols)


# In[17]:


# Print the head of the dataframe
df.head()


# ## `Dropping the duplicate rows`

# There are many rows in the dataframe which are duplicate, and hence they are just repeating the information. Its better if we remove these rows as they don't add any value to the dataframe. 
# 
# For given data, we would like to see how many rows were duplicates. For this, we will count the number of rows, remove the dublicated rows, and again count the number of rows.

# In[18]:


# number of rows before removing duplicated rows
df.shape[0]


# In[19]:


# drop the duplicated rows
df = df.drop_duplicates()

# print head of df
df.head()


# In[20]:


# Count Number of rows after deleting duplicated rows
df.shape[0]


# ## `Dropping the null or missing values`

# Missing values are usually represented in the form of Nan or null or None in the dataset.
# 
# Finding whether we have null values in the data is by using the isnull() function.
# 
# There are many values which are missing, in pandas dataframe these values are reffered to as np.nan. We want to deal with these values beause we can't use nan values to train models. Either we can remove them to apply some strategy to replace them with other values.
# 
# To keep things simple we will be dropping nan values

# In[21]:


# check for nan values in each columns
df.isnull().sum()


# As we can see that the HP and Cylinders have null values of 69 and 30. As these null values will impact on models' accuracy. So to avoid the impact we will drop the these values. As these values are small camparing with dataset  that will not impact any major affect on model accuracy so we will drop the values.

# In[22]:


# drop missing values
df = df.dropna()
  


# In[24]:


# Make sure that missing values are removed
# check number of nan values in each col again
df.isnull().sum()


# In[28]:


#Describe statistics of df
print(df.describe())
print(df.describe(include = 'object').T)


# ## `Removing outliers`

# Sometimes a dataset can contain extreme values that are outside the range of what is expected and unlike the other data. These are called outliers and often machine learning modeling and model skill in general can be improved by understanding and even removing these outlier values.

# In[36]:


## Plot a boxplot for 'Price' column in dataset.
plt.title('Boxplot of Price')  # title of the plot
sns.boxplot(y= 'MSR_Price',data = df)
plt.grid(True)  # gridlines for better readability
plt.show()  # Display the plot


# ### **`Observation:`**<br>
# 
# Here as you see that we got some values near to 1.5 and 2.0 . So these values are called outliers. Because there are away from the normal values.
# Now we have detect the outliers of the feature of Price. Similarly we will checking of anothers features.

# In[37]:


## PLot a boxplot for 'HP' columns in dataset
plt.title('Boxplot of Engine_HP')  # title of the plot
sns.boxplot(y= 'Engine_HP',data = df) 
plt.grid(True)  # gridlines for better readability
plt.show()  # Display the plot


# ### **`Observation:`**<br>
# Here boxplots show the proper distribution of of 25 percentile and 75 percentile of the feature of HP.

# In[39]:


plt.figure(figsize=(8, 6))  # Set the figure size
plt.boxplot(df['Engine_HP'], vert=False, whis=[25, 75])  # boxplot horizontally
plt.title('Boxplot of HEngine_HP (25th and 75th Percentile)')  # title of the plot
plt.xlabel('Engine_HP')  # Set the label for the x-axis
plt.grid(True)  # gridlines for better readability
plt.show()  # Display the plot


# print all the columns which are of int or float datatype in df. 
# 
# Hint: Use loc with condition

# In[43]:


# print all the columns which are of int or float datatype in df.
#data_numeric = df.select_dtypes(include=['float64', 'int64'])
#print(data_numeric)
numeric_columns = df.loc[:, (df.dtypes == 'int64') | (df.dtypes == 'float64')]


# ### `Save the column names of the above output in variable list named 'l'`
# 

# In[51]:


# save column names of the above output in variable list
l=numeric_columns.columns.tolist()
l


# ## **`Outliers removal techniques - IQR Method`**
#  

# **Here comes cool Fact for you!**
# 
# IQR is the first quartile subtracted from the third quartile; these quartiles can be clearly seen on a box plot on the data.

# - Calculate IQR  and give a suitable threshold to remove the outliers and save this new dataframe into df2.
# 
# Let us help you to decide threshold: Outliers in this case are defined as the observations that are below (Q1 − 1.5x IQR) or above (Q3 + 1.5x IQR)

# In[55]:


numeric_columns = ['Manfacture_Year', 'Engine_HP', 'Engine_Cylinders', 'highway_MPG', 'city_mpg', 'MSR_Price']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

## define Q1 and Q2
Q1 = df[numeric_columns].quantile(0.25)
Q3 = df[numeric_columns].quantile(0.75)

# # define IQR (interquantile range) 
IQR =  Q3 - Q1  
threshold = 1.5 * IQR
outlier_condition = (df[numeric_columns] < (Q1 - threshold)) | (df[numeric_columns] > (Q3 + threshold))

# define df2 after removing outliers
df2 = df[~outlier_condition.any(axis=1)]


# In[56]:


# find the shape of df & df2
print(df.shape)
print(df2.shape)


# In[57]:


# find unique values and there counts in each column in df using value counts function.

for i in df.columns:
   print ("--------------- %s ----------------" % i)
   print(df[i].value_counts())


# ## `Visualising Univariate Distributions`

# We will use seaborn library to visualize eye catchy univariate plots. 
# 
# Do you know? you have just now already explored one univariate plot. guess which one? Yeah its box plot.
# 

# ### `Histogram & Density Plots`
# 
# Histograms and density plots show the frequency of a numeric variable along the y-axis, and the value along the x-axis. The ```sns.distplot()``` function plots a density curve. Notice that this is aesthetically better than vanilla ```matplotlib```.

# In[58]:


#ploting distplot for variable HP

data = df['Engine_HP']

# density plot and histogram
sns.distplot(data, bins=20, kde=True, color='blue', hist_kws={'edgecolor': 'black'})

#labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Plot and Histogram')
plt.show()



# ### **`Observation:`**
# We plot the Histogram of feature HP with help of distplot in seaborn.<br> 
# In this graph we can see that there is max values near at 200. similary we have also the 2nd highest value near 400 and so on. <br>
# It represents the overall distribution of continuous data variables.<br>

# Since seaborn uses matplotlib behind the scenes, the usual matplotlib functions work well with seaborn. For example, you can use subplots to plot multiple univariate distributions.
# - Hint: use matplotlib subplot function

# In[65]:


# plot all the columns present in list l together using subplot of dimention (2,3).


# c=0
# plt.figure(figsize=(15,10))
# for i in l:
#     # code here
# plt.show()

num_rows = 2
num_cols = 3
fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 10))
axes = axes.flatten()
for i, column in enumerate(l):
    sns.distplot(df[column], bins=20, kde=True, ax=axes[i], color='blue', hist_kws={'edgecolor': 'black'})
    axes[i].set_xlabel('Value')
    axes[i].set_ylabel('Density')
    axes[i].set_title(f'Distribution of {column}')

plt.tight_layout()
plt.show()


# ## `Bar Chart Plots`
# 

# Plot a histogram depicting the make in X axis and number of cars in y axis. <br>

# In[72]:


plt.figure(figsize = (12,8))

# use nlargest and then .plot to get bar plot like below output
# Plot Title, X & Y label
top_n = 30  # the number of top makes to consider
top_makes = df['Manfactured_company'].value_counts().nlargest(top_n)
top_makes.plot(kind='bar', color='skyblue')
plt.title('Number of Cars by Make')
plt.xlabel('Manfactured_company')
plt.ylabel('Number of Cars')
plt.xticks(rotation=45, ha='right')
plt.show()


# ### **`Observation:`**
# In this plot we can see that we have plot the bar plot with the cars model and nos. of cars.

# ### `Count Plot`
# A count plot can be thought of as a histogram across a categorical, instead of quantitative, variable.
# 

#  Plot a countplot for a variable Transmission vertically with hue as Drive mode

# In[73]:


plt.figure(figsize=(15,5))

# plot countplot on transmission and drive mode

sns.countplot(data=df, y='Transmission_Type', hue='Driven_Wheels')

# Set plot title and labels
plt.title('Count Plot of Transmission with Drive Mode')
plt.xlabel('Count')
plt.ylabel('Transmission_Type')
plt.show()



# ### **`Observation:`**
# In this count plot, We have plot the feature of Transmission with help of hue.<br>
# We can see that the the nos of count and the transmission type and automated manual is plotted. Drive mode as been given with help of hue.<br>
# 

# # `Visualising Bivariate Distributions`
# 
# 
# Bivariate distributions are simply two univariate distributions plotted on x and y axes respectively. They help you observe the relationship between the two variables.
# 
# 
# 

# ## `Scatter Plots`
# Scatterplots are used to find the correlation between two continuos variables.
# 
# Using scatterplot find the correlation between 'HP' and 'Price' column of the data. 
# 
# 

# In[74]:


fig, ax = plt.subplots(figsize=(10,6))

# plot scatterplot on hp and price

sns.scatterplot(data=df, x='Engine_HP', y='MSR_Price')
plt.title('Scatterplot of HP vs Price')
plt.xlabel('HP')
plt.ylabel('Price')
plt.show()


# ### **`Observation:`**<br>
# It is a type of plot or mathematical diagram using Cartesian coordinates to display values for typically two variables for a set of data.<br>
# We have plot the scatter plot with x axis as HP and y axis as Price.<br>
# The data points between the features should be same either wise it give errors.<br>
# 

# ## `Plotting Aggregated Values across Categories`
# 
# 
# ### `Bar Plots - Mean, Median and Count Plots`
# 
# 
# 
# Bar plots are used to **display aggregated values** of a variable, rather than entire distributions. This is especially useful when you have a lot of data which is difficult to visualise in a single figure. 
# 
# For example, say you want to visualise and *compare the Price across Cylinders*. The ```sns.barplot()``` function can be used to do that.
# 

# In[75]:


# bar plot with default statistic=mean between Cylinder and Price
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Engine_Cylinders', y='MSR_Price')
plt.title('Bar Plot of Price by Cylinder (Mean)')
plt.xlabel('Engine_Cylinders')
plt.ylabel('Price')
plt.show()





# ### **`Observation:`**<br>
# By default, seaborn plots the mean value across categories, though you can plot the count, median, sum etc.<br>
# Also, barplot computes and shows the confidence interval of the mean as well.
# 
# 

# ## `When you want to visualise having a large number of categories, it is helpful to plot the categories across the y-axis.`
# 
# ### `Let's now drill down into Transmission sub categories.`

# In[76]:


# Plotting categorical variable Transmission across the y-axis
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='Transmission_Type')
plt.title('Count Plot of Transmission')
plt.xlabel('Count')
plt.ylabel('Transmission_Type')
plt.show()




# These plots looks beutiful isn't it? In Data Analyst life such charts are there unavoidable friend.:)

# # `Multivariate Plots`
# 
# 

# ## `Heatmaps`
# 
# 
# A heat map is a two-dimensional representation of information with the help of colors. Heat maps can help the user visualize simple or complex information

# Using heatmaps plot the correlation between the features present in the dataset.

# In[79]:


#find the correlation of features of the data 
corr = df.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(12, 10))
sns.heatmap(corr, annot=True)
plt.title('Correlation Heatmap of Features')
plt.show()



# In[80]:


# Using the correlated df, plot the heatmap 
# set cmap = 'BrBG', annot = True - to get the same graph as shown below 
#set size of graph = (12,8)
plt.figure(figsize=(12, 8))
corr = df.select_dtypes(include=['float64', 'int64'])
sns.heatmap(corr,cmap='BrBG', annot=True)
plt.title('Correlation Heatmap of Features')
plt.show()


# ### **`Observation:`**<br>
# A heatmap contains values representing various shades of the same colour for each value to be plotted. Usually the darker shades of the chart represent higher values than the lighter shade. For a very different value a completely different colour can also be used.
# 
# 
# The above heatmap plot shows correlation between various variables in the colored scale of -1 to 1. 
# 

# In[ ]:




