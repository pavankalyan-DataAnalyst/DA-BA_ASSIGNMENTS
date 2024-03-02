#!/usr/bin/env python
# coding: utf-8

# <a id='1'></a><center> <h3 style="background-color:orange; color:white" ><br>Telecommunication Industry Project<br></h3>

# # Introduction
# This Jupyter notebook is part of your learning experience in the study of applied statistics.
# 
# You will work with a data set that contains mobile phone prices and their specifications.
# 
# **Dataset Columns Information**
# 
# PID = a unique identifier for the phone model
# 
# Blue = whether the phone has bluetooth support or not
# 
# Wi_Fi = whether the phone has wifi support or not
# 
# Tch_Scr = whether the phone has touch screen support or not
# 
# Ext_Mem = whether the phone has external memory support or not
# 
# Px_h = number of pixels in the vertical axis of the phone
# 
# Px_w = number of pixels in the horizontal axis of the phone
# 
# Scr_h = height of the screen of the phone in centimetres (cm)
# 
# Scr_w = width of the screen of the phone in centimetres (cm)
# 
# Int_Mem = internal memory of the phone measured in megabytes (MB)
# 
# Bty_Pwr = maximum energy stored by the phone's battery measured in 
# milli-Ampere-hours (mAh)
# 
# PC = resolution of the primary camera measued in megapixels (MP)
# 
# FC = resolution of the front camera measued in megapixels (MP)
# 
# RAM = random access memory available in the phone measured in gigabytes (GB)
# 
# Depth = depth of the mobile phone measured in centimetres (cm)
# 
# Weight = weight of the mobile phone measured in grams (g)
# 
# Price = selling price of the mobile phone in rupees
# 

# ## Task 1 - Load and study the data

# Import the libraries that will be used in this notebook

# In[1]:


# Load "numpy" and "pandas" for manipulating numbers and data frames
# Load "matplotlib.pyplot" and "seaborn" for data visualisation
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Load the csv file as pandas dataframe. 

# In[3]:


# Read in the "Dataset" file as a Pandas Data Frame
df = pd.read_csv("Telecom Dataset.csv")


# In[4]:


# Take a brief look at the data
df.head()


# In[5]:


# Get the dimensions of the dataframe
df.shape


# In[9]:


# Get the row names of the dataframe
row_names = df.index
print(row_names)


# In[10]:


# Get the column names of the dataframe
column_names = df.columns
print(column_names)


# In[11]:


# Look at basic information about the dataframe
print(df.info())


# Observations:
# 
# There are 50 phones in the data set.
# 
# There are 17 features in the data set including the "PID" feature which is used as the row index labels.
# 
# There are no missing values in the data set.

# In[12]:


df.isnull().sum()


# <center>Let's try some logical operators to filter the data.<center>

# ![](https://th.bing.com/th/id/R.0592084daa6518e4fae97f47217ec69e?rik=vNqmiaTVSSo54w&riu=http%3a%2f%2f2.bp.blogspot.com%2f-ujABms6N-Cg%2fTyYwShdTjnI%2fAAAAAAAAAAs%2fktPbHdifidc%2fs1600%2fLogical%2bOperators.PNG&ehk=ww1gl1HB2PcZwPQNHWRUvcQ631Q3mzyHSxL9G4zUKT4%3d&risl=&pid=ImgRaw&r=0,width=700,height=400)

# ## Task 2 - Obtain the logical conditions for the features "Blue", "Wi_Fi", "Tch_Scr" and "Ext_Mem"

# In[13]:


# Get the feature names of the dataframe
blue_values = df['Blue'].unique()
wifi_values = df['Wi_Fi'].unique()
touchscreen_values = df['Tch_Scr'].unique()
ext_mem_values = df['Ext_Mem'].unique()

print("Unique values for 'Blue':", blue_values)
print("Unique values for 'Wi_Fi':", wifi_values)
print("Unique values for 'Tch_Scr':", touchscreen_values)
print("Unique values for 'Ext_Mem':", ext_mem_values)


# In[9]:


# Let's tackle these features: "Blue", "Wi_Fi", "Tch_Scr", "Ext_Mem"


# In[60]:


# The children want phones that have the following: Bluetooth, WiFi, touch screen and external memory support
# Create a logical condition for this situation and store the logical values as "con1"

con1 = (df['Blue'] == 'yes') & (df['Wi_Fi'] == 'yes') & (df['Tch_Scr'] == 'yes') & (df['Ext_Mem'] == 'yes')

# Filter the DataFrame using the condition
result_df = df[condition]
result_df


# Observations:
# 
# The features "Blue", "Wi_Fi", "Tch_Scr" and "Ext_Mem" are binary in nature.
# 
# The children want all these features, so the logical condition "con1" has been obtained accordingly.

# ## Task 3 - Obtain the logical conditions for the features "Px_h" and "Px_w"

# In[15]:


# Get the feature names of the dataframe
feature_names = df.columns
print("Feature names of the DataFrame:", feature_names)


# In[ ]:


# Let's tackle these features: "Px_h", "Px_w"


# In[17]:


# Create a new feature called "Px" which stores the total resolution of the screen
df['Px'] = df['Px_h'] * df['Px_w']
df.head()


# In[18]:


# Create a histogram of the "Px" feature and also show the mean and the median
plt.hist(df['Px'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Total Resolution of the Screen (Px)')
plt.ylabel('Frequency')
plt.title('Histogram of Screen Resolution')

mean_px = df['Px'].mean()
median_px = df['Px'].median()

plt.axvline(mean_px, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean_px:.2f}')
plt.axvline(median_px, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median_px:.2f}')
plt.legend()

plt.show()


# In[40]:


# The children want phones that have good screen resolutions
# Consider the phones that have screen resolutions greater than or equal to the median value in the data set
# Create a logical condition for this situation and store the logical values as "con2"

median_screen_resolution = df['Px'].median()
con2 = df['Px'] >= median_screen_resolution
df[con2]


# Observations:
# 
# The features "Px_h" and "Px_w" are respectively the number of pixels in the phone screen in the vertical and horizontal axes.
# 
# We created a new feature called "Px" which is the product of the features "Px_h" and "Px_w".
# 
# The median has been selected as a threshold in this case.
# 
# In case it is too strict, we can choose the mean as a threshold.

# # Task 4 - Obtain the logical conditions for the features "Scr_h" and "Scr_w"

# In[ ]:


# Let's tackle these features: "Scr_h", "Scr_w"


# In[23]:


# Create a new feature called "Scr_d" which stores the length of the diagonal of the screen of the phone

df['Scr_d'] = np.sqrt(df['Scr_h']**2 + df['Scr_w']**2)


# In[24]:


# Create a histogram of the "Scr_d" feature and also show the quartiles
plt.hist(df['Scr_d'], bins=10, color='skyblue', edgecolor='black')

plt.xlabel('Screen Diagonal Length')
plt.ylabel('Frequency')
plt.title('Histogram of Screen Diagonal Length')

quartiles = np.percentile(df['Scr_d'], [25, 50, 75])
for q in quartiles:
    plt.axvline(q, color='red', linestyle='--', linewidth=1)

plt.legend(['25th Percentile', 'Median', '75th Percentile'])

plt.show()


# In[41]:


# The children want phones that have very good screen sizes
# Consider the phones that have screen sizes greater than or equal to the upper quartile value in the data set
# Create a logical condition for this situation and store the logical values as "con3"
upper_quartile = np.percentile(df['Scr_d'], 75)
con3 = df['Scr_d'] >= upper_quartile
df[con3]


# Observations:
# 
# The features "Scr_h" and "Scr_w" are respectively the height and the width of the phone screen.
# 
# We created a new feature called "Scr_d" which is essentially the length of the screen diagonal.
# 
# The upper quartile has been selected as a threshold in this case as the children were very particular on this point.
# 
# In case it is too strict, we can choose the mean or the median as a threshold.

# # Task 5 - Obtain the logical conditions for the features "PC" and "FC"

# In[ ]:


# Let's tackle these features: "PC", "FC"


# In[26]:


# Create a histogram of the "PC" feature and also show the mean and the median
con_PC = df['PC'] > df['PC'].median()
con_FC = df['FC'] > df['FC'].median()

plt.figure(figsize=(8, 6))
plt.hist(df['PC'], bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(df['PC'].mean(), color='red', linestyle='dashed', linewidth=1, label='Mean')
plt.axvline(df['PC'].median(), color='green', linestyle='dashed', linewidth=1, label='Median')
plt.xlabel('PC Feature')
plt.ylabel('Frequency')
plt.title('Histogram of PC Feature with Mean and Median')
plt.legend()
plt.show()



# In[27]:


# Create a histogram of the "FC" feature and also show the mean and the median
plt.figure(figsize=(8, 6))
plt.hist(df['FC'], bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(df['FC'].mean(), color='red', linestyle='dashed', linewidth=1, label='Mean')
plt.axvline(df['FC'].median(), color='green', linestyle='dashed', linewidth=1, label='Median')
plt.xlabel('FC Feature')
plt.ylabel('Frequency')
plt.title('Histogram of FC Feature with Mean and Median')
plt.legend()
plt.show()


# In[42]:


# The children want phones that have good primary and front camera resolutions
# Consider the phones that have primary and front camera resolutions greater than or equal to their respective mean values
# Create a logical condition for this situation and store the logical values as "con4"
mean_pc = df['PC'].mean()
mean_fc = df['FC'].mean()
con4_pc = df['PC'] >= mean_pc
con4_fc = df['FC'] >= mean_fc

con4 = con4_pc & con4_fc
df[con4]


# Observations:
# 
# The features "PC" and "FC" are respectively the resolutions of the primary camera and the front camera.
# 
# The respective means have been selected as thresholds in this case.
# 
# In case it is too strict, we can choose the respective medians as thresholds.

# # Task 6 - Obtain the logical conditions for the features "Int_Mem", "Bty_Pwr" and "RAM"

# In[ ]:


# Let's tackle these features: "Int_Mem", "Bty_Pwr", "RAM"


# In[29]:


# Create a histogram of the "Int_Mem" feature and also show the mean and the median
plt.figure(figsize=(8, 6))
plt.hist(df['Int_Mem'], bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Histogram of Internal Memory (Int_Mem)')
plt.xlabel('Internal Memory')
plt.ylabel('Frequency')
plt.grid(True)
mean_int_mem = df['Int_Mem'].mean()
median_int_mem = df['Int_Mem'].median()
plt.axvline(mean_int_mem, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean_int_mem:.2f}')
plt.axvline(median_int_mem, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median_int_mem}')
plt.legend()

plt.show()



# In[30]:


# Create a histogram of the "Bty_Pwr" feature and also show the mean and the median

plt.figure(figsize=(8, 6))
plt.hist(df['Bty_Pwr'], bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Histogram of Battery Power (Bty_Pwr)')
plt.xlabel('Battery Power')
plt.ylabel('Frequency')
plt.grid(True)

mean_bty_pwr = df['Bty_Pwr'].mean()
median_bty_pwr = df['Bty_Pwr'].median()
plt.axvline(mean_bty_pwr, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean_bty_pwr:.2f}')
plt.axvline(median_bty_pwr, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median_bty_pwr}')
plt.legend()

plt.show()


# In[33]:


# Create a histogram of the "RAM" feature and also show the mean and the median

plt.figure(figsize=(8, 6))
plt.hist(df['RAM'], bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Histogram of RAM')
plt.xlabel('RAM')
plt.ylabel('Frequency')
plt.grid(True)

mean_ram = df['RAM'].mean()
median_ram = df['RAM'].median()
plt.axvline(mean_ram, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean_ram:.2f}')
plt.axvline(median_ram, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median_ram}')
plt.legend()

plt.show()



# In[43]:


# The children want phones that have good internal memory, battery power and RAM
# Consider the phones that have internal memory, battery power and RAM greater than or equal to their respective mean values
# Create a logical condition for this situation and store the logical values as "con5"

mean_int_mem = df['Int_Mem'].mean()
mean_bty_pwr = df['Bty_Pwr'].mean()
mean_ram = df['RAM'].mean()

con5 = (df['Int_Mem'] >= mean_int_mem) & (df['Bty_Pwr'] >= mean_bty_pwr) & (df['RAM'] >= mean_ram)

df[con5]


# Observations
# 
# The features "Int_Mem", "Bty_Pwr" and "RAM" are respectively the internal memory, battery power and RAM of the phones.
# 
# The respective means have been selected as thresholds in this case.
# 
# .In case it is too strict, we can choose the respective medians as thresholds

# # Task 7 - Obtain the logical conditions for the features "Depth" and "Weight"

# In[27]:


# Let's tackle these features: "Depth", "Weight"


# In[35]:


# Create a histogram of the "Depth" feature and also show the mean and the median

plt.hist(df['Depth'], bins=10, color='skyblue', edgecolor='black')

mean_depth = df['Depth'].mean()
median_depth = df['Depth'].median()

plt.axvline(mean_depth, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean_depth}')
plt.axvline(median_depth, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median_depth}')

plt.xlabel('Depth')
plt.ylabel('Frequency')
plt.title('Histogram of Depth Feature')
plt.legend()

plt.show()



# In[36]:


# Create a histogram of the "Weight" feature and also show the mean and the median

plt.hist(df['Weight'], bins=10, color='skyblue', edgecolor='black')

mean_weight = df['Weight'].mean()
median_weight = df['Weight'].median()

plt.axvline(mean_weight, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean_weight}')
plt.axvline(median_weight, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median_weight}')
plt.xlabel('Weight')
plt.ylabel('Frequency')
plt.title('Histogram of Weight Feature')
plt.legend()
plt.show()


# In[38]:


# The children want phones that are light weight and slim
# Consider the phones that have depth and weight less than or equal to the respective median values in the data set
# Create a logical condition for this situation and store the logical values as "con6"

median_depth = df['Depth'].median()
median_weight = df['Weight'].median()

con6 = (df['Depth'] <= median_depth) & (df['Weight'] <= median_weight)

df[con6]


# Observations:
# 
# The features "Depth" and "Weight" are respectively the depth of the phone and the weight of the phone.
# 
# The respective medians have been selected as thresholds in this case.
# 
# In case it is too strict, we can choose the respective means as thresholds.

# # Task 8 - Subset the data based on all the logical conditions

# In[62]:


# Subset the dataframe using all the logical conditions that have been stored
# Store the subset of the dataframe as a new dataframe called "df1"
# Subset the dataframe using all the logical condition
# Subset the dataframe using all the logical conditions
df1 = df[con1 & con2 & con3 & con4 & con5 & con6]


# In[63]:


# Get the dimensions of the dataframe
df1.shape


# In[64]:


# Sort the dataframe according to the "Price" feature in ascending order and display it
# Sort the dataframe according to the "Price" feature in ascending order
sorted_df = df1.sort_values(by='Price')
sorted_df


# Observations:
# 
# Based on all the logical conditions obtained through analysis of the features, we are left with three phones.
# 
# The most expensive of these phones is the "TYS938L" model and the least expensive is the "TVF078Y" model.
# 
# We could let the children choose from these three phones as per their preferences.

# # Task 9 - Study the variability of the features in the original data set

# In[67]:


# Calculate the ratio of the standard deviation to the mean for all the numerical features in the dataframe
# Store these values in a new series wherein the rows are the features and the only column is the calculated ratio
# Name the series as "deviations"

data_numeric = df.select_dtypes(include=['float64', 'int64'])

std_dev = data_numeric.std()

mean_vals = data_numeric .mean()

ratios = std_dev / mean_vals

deviations = pd.Series(ratios, name="deviations")
print(deviations)


# In[68]:


# View the "deviations" series after sorting it in descending order

deviations_sorted = deviations.sort_values(ascending=False)
print(deviations_sorted)


# Observations:
# 
# The ratio of the standard deviation to the mean of a feature normalises it in a way.
# 
# This allows for comparison between multiple features.
# 
# The most variable feature in the original data set is the internal memory of the phones.
# 
# The least variable feature in the original data set is the number of screen pixels in the horizontal axis.
# 
# Although most features don't seem so variable, the prices of the phones are quite variable.
# 
# Feel free to investigate what could be the cause of this difference in variability.
# 
# Note: We encourage you to extend this analysis further and see what else you can find.
# 
# Note: Please refer to the official website of Python and its libraries for various Python documentations.

# # Conclusion
# 1. We have used concepts of descriptive statistics to study and work with a data set that contains mobile phone specifications.
# 
# 2. We were able to recommend three phone models to the client which she can then propose to her children.

# In[ ]:




