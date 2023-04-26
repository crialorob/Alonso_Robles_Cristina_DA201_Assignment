#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Import pandas.
import pandas as pd

# Read the Excel file.
# Assign a variable.
# Use the pd.read_excel() function.
# Specify the name of the Excel file.
nc = pd.read_excel('national_categories.xlsx')

# Print the DataFrame.
nc


# In[11]:


# Read the CSV file.
# Assign a variable.
# Use the pd.read_csv() function.
# Specify the name of the CSV file.
ar = pd.read_csv('appointments_regional.csv')

# Print the DataFrame.
ar


# In[12]:


# Read the CSV file.
# Assign a variable.
# Use the pd.read_csv() function.
# Specify the name of the CSV file.
ad = pd.read_csv('actual_duration.csv')

# Print the DataFrame.
ad


# In[13]:


# Print the number of columns of each data set.
print(nc.columns)
print(ar.columns)
print(ad.columns)


# In[18]:


# Determine shape of the national_category data set.
print(nc.shape)
print(nc.dtypes)


# In[19]:


# Determine shape of the appointments regional data set.
print(ar.shape)
print(ar.dtypes)


# In[20]:


# Determine shape of the actual_duration data set.
print(ad.shape)
print(ad.dtypes)


# In[22]:


# Print the entire 'ad' DataFrame to perform a sense-check.
print(ad)


# In[25]:


# Print the entire 'nc' DataFrame to perform a sense-check.
print(nc)


# In[26]:


# Print the entire 'ar' DataFrame to perform a sense-check.
print(ar)


# In[37]:


# Identify the number of missing values in the 'nc' data set.
nc = pd.read_excel('national_categories.xlsx')
nc.head()


# In[41]:


nc_na = nc[nc.isna().any(axis=1)]
nc_na.shape


# In[42]:


# Identify the number of missing values in the 'ad' data set.
ad = pd.read_csv('actual_duration.csv')
ad.head()


# In[43]:


ad_na = ad[ad.isna().any(axis=1)]
ad_na.shape


# In[44]:


# Identify the number of missing values in the 'ar' data set.
ar = pd.read_csv('appointments_regional.csv')
ar.head()


# In[45]:


ar_na = ar[ar.isna().any(axis=1)]
ar_na.shape

