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


# In[6]:


# Import the necessary packages.
import pandas as pd

# Read the Excel file.
# Assign a variable.
# Use the pd.read_excel() function.
# Specify the name of the Excel file.
nc = pd.read_excel('national_categories.xlsx')

# Print the DataFrame.
nc


# In[7]:


# Read the CSV file.
# Assign a variable.
# Use the pd.read_csv() function.
# Specify the name of the CSV file.
ar = pd.read_csv('appointments_regional.csv')

# Print the DataFrame.
ar


# In[19]:


# Read the CSV file.
# Assign a variable.
# Use the pd.read_csv() function.
# Specify the name of the CSV file.
ad = pd.read_csv('actual_duration.csv')

# Print the DataFrame.
ad


# In[9]:


# Determine the sum of missing values in the 'ad' DataFrame.
# There are wrong values in the 'actual_duration' column, identified as: 'Unknown / Data Quality'.
# Python does not identify them as missing values.
# I will use some filters later on in my analysis to filter these wrong values out of my analysis.

ad['actual_duration'].isnull().sum()


# In[29]:


# Determine the sum of missing values in the 'nc' DataFrame.
# There are wrong values in the 'service_setting' column, identified as 'Unmapped'.
# There are also wrong values in the 'context_type' and 'national_category' columns, identified as 'Inconsistent Mapping' and 'Unmapped'.
# Python does not identify them as missing values because they are the same data type.
# I will use some filters later on in my analysis to filter these wrong values out of my analysis.

nc['service_setting'].isnull().sum()
nc['context_type'].isnull().sum()
nc['national_category'].isnull().sum()


# In[16]:


# Determine the sum of missing values in the 'ar' DataFrame.
# There are wrong values in the 'appointment_status' and in the 'hcp_type' columns, identified as 'Unknown'. 
# There are also wrong values in the 'time_between_book_and_appointment' column, identified as 'Unknown / Data Quality'.
# Python does not identify them as missing values.
# I will use some filters later on in my analysis to filter these wrong values out of my analysis.

ar['appointment_status'].isnull().sum()
ar['hcp_type'].isnull().sum()
ar['time_between_book_and_appointment'].isnull().sum()


# In[24]:


# Filter the 'ar' DataFrame according to wrong values.
# There are wrong values in the 'appointment_status', identified as 'Unknown'. 

ar[ar['appointment_status'].str.contains("Unknown")]


# In[25]:


# Filter the 'ar' DataFrame according to wrong values.
# There are wrong values in the 'hcp_type', identified as 'Unknown'. 

ar[ar['hcp_type'].str.contains("Unknown")]


# In[26]:


# Filter the 'ar' DataFrame according to wrong values.
# There are wrong values in the 'time_between_book_and_appointment' column, identified as 'Unknown / Data Quality'.
ar[ar['time_between_book_and_appointment'].str.contains('Unknown / Data Quality')]


# In[27]:


# Filter the 'ad' DataFrame according to wrong values.
# There are wrong values in the 'actual_duration' column, identified as'Unknown / Data Quality'.


ad[ad['actual_duration'].str.contains('Unknown / Data Quality')]




# In[30]:


# Filter the 'nc' DataFrame according to wrong values.
# There are wrong values in the 'service_setting' column, identified as 'Unmapped'.


nc[nc['service_setting'].str.contains('Unmapped')]


# In[37]:


# Filter the 'nc' DataFrame according to wrong values.
# There are also wrong values in the 'context_type' column, identified as 'Inconsistent Mapping' and 'Unmapped'.

nc[nc['context_type'].str.contains('Unmapped')]


# In[38]:


nc[nc['context_type'].str.contains('Inconsistent Mapping')]


# In[39]:


# Filter the 'nc' DataFrame according to wrong values.
# There are wrong values in the 'national_category' column, identified as 'Inconsistent Mapping' and 'Unmapped'.

nc[nc['context_type'].str.contains('Unmapped')]


# In[41]:


nc[nc['context_type'].str.contains('Inconsistent Mapping')]


# In[44]:


# Determine the descriptive statistics of the 'nc' DataFrame.
nc.describe()


# In[47]:


# Determine the metadata of the 'nc' DataFrame.
nc.info()


# In[46]:


# Determine the descriptive statistics of the 'ar' DataFrame.
ar.describe()


# In[49]:


# Determine the metadata of the 'ar' DataFrame.
ar.info()


# In[50]:


# Determine the descriptive statistics of the 'ad' DataFrame.
ad.describe()


# In[51]:


# Determine the metadata of the 'ad' DataFrame.
ad.info()


# In[1]:


# Import the necessary packages.
import pandas as pd

# Read the Excel file.
# Assign a variable.
# Use the pd.read_excel() function.
# Specify the name of the Excel file.
nc = pd.read_excel('national_categories.xlsx')

# Print the DataFrame.
nc


# In[2]:


# Read the CSV file.
# Assign a variable.
# Use the pd.read_csv() function.
# Specify the name of the CSV file.
ar = pd.read_csv('appointments_regional.csv')

# Print the DataFrame.
ar


# In[3]:


# Read the CSV file.
# Assign a variable.
# Use the pd.read_csv() function.
# Specify the name of the CSV file.
ad = pd.read_csv('actual_duration.csv')

# Print the DataFrame.
ad


# In[36]:


# Get Unique Count of Locations from the 'nc' DataFrame.
count = nc.sub_icb_location_name.unique().size
print("Count of locations : "+ str(count))


# In[37]:


# Get Unique Count of Locations from the 'ad' DataFrame.
count = ad.sub_icb_location_name.unique().size
print("Count of locations : "+ str(count))


# In[39]:


# Determine the 5 locations with the highest number of records.
print(len(ad['sub_icb_location_name'].unique()))


# In[40]:


# Determine the number of service settings from the 'nc' DataFrame.
print(len(nc['service_setting'].unique()))


# In[43]:


# Determine the number of context types from the 'nc' DataFrame.
print(len(nc['context_type'].unique()))


# In[42]:


# Determine the number of national categories from the 'nc' DataFrame.
print(len(nc['national_category'].unique()))


# In[41]:


# Determine the number of appointment statuses from the 'ar' DataFrame.
print(len(ar['appointment_status'].unique()))


# In[69]:


# Sorting the data by 'count_of_appointments' to find the 5 locations with the highest number of records.
nc.sort_values(by=['count_of_appointments'], ascending=False)


# In[77]:


nc[['sub_icb_location_name', 'count_of_appointments']].value_counts().reset_index(name='count')


# In[85]:


nc[['sub_icb_location_name', 'count_of_appointments']].value_counts()


# In[ ]:


nc.sort_values(by=['count_of_appointments'], ascending=False)


# In[1]:


# Import pandas.
import pandas as pd

# Read the Excel file.
# Assign a variable.
# Use the pd.read_excel() function.
# Specify the name of the Excel file.
nc = pd.read_excel('national_categories.xlsx')

# Print the DataFrame.
nc


# In[2]:


nc.shape


# In[18]:


nc.groupby(['sub_icb_location_name']).value_counts().reset_index(name='count')


# In[29]:


locations_count = nc.groupby(['sub_icb_location_name']).count()
locations_count


# In[45]:


# Determine the five locations with the highest number of records.
locations_count = pd.DataFrame(nc.groupby(['sub_icb_location_name']).count())
locations_count
locations_count.sort_values(['icb_ons_code'],ascending=False)
top_5_locations = locations_count.sort_values(['icb_ons_code'],ascending=False)
top_5_locations.head()


# In[ ]:




