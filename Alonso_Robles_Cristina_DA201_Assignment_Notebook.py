#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # Course 2: Data Analytics using Python

# ## Assignment: Diagnostic Analysis using Python
# 
# You’ll be working with real-world data to address a problem faced by the National Health Service (NHS). The analysis will require you to utilise Python to explore the available data, create visualisations to identify trends, and extract meaningful insights to inform decision-making. 

# ### A note for students using this template
# This Jupyter Notebook is a template you can use to complete the Course 2 assignment: Diagnostic Analysis using Python. 
# 
# Keep in mind: 
# - You are **not required** to use this template to complete the assignment. 
# - If you decide to use this template for your assignment, make a copy of the notebook and save it using the assignment naming convention: **LastName_FirstName_DA201_Assignment_Notebook.ipynb**.
# - The workflow suggested in this template follows the Assignment Activities throughout the course.
# - Refer to the guidance on the Assignment Activity pages for specific details. 
# - The markup and comments in this template identify the key elements you need to complete before submitting the assignment.
# - Make this notebook your own by adding your process notes and rationale using markdown, add links, screenshots, or images to support your analysis, refine or clarify the comments, and change the workflow to suit your process.
# - All elements should be functional and visible in your Notebook. 
# - Be sure to push your notebook to GitHub after completing each Assignment Activity.
# 
#  > ***Markdown*** Remember to change cell types to `Markdown`. You can review [Markdown basics](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) to find out how to add formatted text, links, and images to your notebook.

# # 

# # Assignment activity 1

# ### Insert proof of your GitHub repository. This can be a link or screenshot showing your repo.

# In[1]:


# My GitHub repository.
https://github.com/crialorob/Alonso_Robles_Cristina_DA201_Assignment


# # 

# # Assignment activity 2

# ### Prepare your workstation

# In[106]:


# Import the necessary libraries.
import pandas as pd
import numpy as np

# Optional - Ignore warnings.
import warnings
warnings.filterwarnings('ignore')


# In[107]:


# Import and sense-check the actual_duration.csv data set as ad.
ad = pd.read_csv('actual_duration.csv')

# View the DataFrame.
ad


# In[108]:


# Determine whether there are missing values.
ad_na = ad[ad.isna().any(axis=1)]
ad_na.shape


# In[109]:


# Determine the sum of missing values in the 'ad' DataFrame.
ad['actual_duration'].isnull().sum()


# There are invalid values in the 'actual_duration' column, identified as'Unknown / Data Quality'.
# 
# Python does not identify them as missing values.

# In[5]:


ad['actual_duration'].isnull().sum()


# In[6]:


# Filter the 'ad' DataFrame according to invalid values.
# There are invalid values in the 'actual_duration' column, identified as'Unknown / Data Quality'.
ad[ad['actual_duration'].str.contains('Unknown / Data Quality')]


# In[7]:


# Determine the metadata of the data set.
print(ad.columns)
print(ad.shape)
print(ad.dtypes)
ad.info()


# In[8]:


# Determine the descriptive statistics of the ad data set.
ad.describe()


# In[9]:


# Import and sense-check the appointments_regional.csv data set as ar.
ar = pd.read_csv('appointments_regional.csv')

# View the DataFrame.
ar


# In[10]:


# Determine whether there are missing values.
ar_na = ar[ar.isna().any(axis=1)]
ar_na.shape


# There are invalid/erroneous values in the 'appointment_status' and in the 'hcp_type' columns, identified as 'Unknown'.
# 
# There are also invalid values in the 'time_between_book_and_appointment' column, identified as 'Unknown / Data Quality'.
# 
# Python does not identify them as missing values.

# In[11]:


# Determine the sum of missing values.
ar['appointment_status'].isnull().sum()
ar['hcp_type'].isnull().sum()
ar['time_between_book_and_appointment'].isnull().sum()


# In[12]:


# Filter the 'ar' DataFrame according to invalid values 
# This will allow me to better understand the scale of these invalid values.
# There are invalid values in the 'appointment_status' column, identified as 'Unknown'. 
ar[ar['appointment_status'].str.contains("Unknown")]


# In[13]:


# Filter the 'ar' DataFrame according to invalid values.
# There are wrong values in the 'hcp_type' column, identified as 'Unknown'. 
ar[ar['hcp_type'].str.contains("Unknown")]


# In[14]:


# Filter the 'ar' DataFrame according to invalid values.
# There are invalid values in the 'time_between_book_and_appointment' column, identified as 'Unknown / Data Quality'.
ar[ar['time_between_book_and_appointment'].str.contains('Unknown / Data Quality')]


# In[15]:


# Determine the metadata of the data set.
print(ar.columns)
print(ar.shape)
print(ar.dtypes)
ar.info()


# In[16]:


# Determine the descriptive statistics of the ar data set.
ar.describe()


# In[17]:


# Import and sense-check the national_categories.xlsx data set as nc.
nc = pd.read_excel('national_categories.xlsx')

# View the DataFrame.
nc


# In[18]:


# Determine whether there are missing values.
nc_na = nc[nc.isna().any(axis=1)]
nc_na.shape


# There are invalid values in the 'service_setting' column, identified as 'Unmapped'.
# 
# There are also invalid values in the 'context_type' and 'national_category' columns, identified as 'Inconsistent Mapping' and 'Unmapped'.
# 
# Python does not identify them as missing values.

# In[19]:


# Determine the sum of missing values in the 'ar' DataFrame.
nc['service_setting'].isnull().sum()
nc['context_type'].isnull().sum()
nc['national_category'].isnull().sum()


# In[20]:


# Filter the 'nc' DataFrame according to invalid values.
# There are invalid values in the 'service_setting' column, identified as 'Unmapped'.

nc[nc['service_setting'].str.contains('Unmapped')]


# In[21]:


# Filter the 'nc' DataFrame according to invalid values.
# There are also invalid values in the 'context_type' column, identified as 'Unmapped'.

nc[nc['context_type'].str.contains('Unmapped')]


# In[22]:


# Filter the 'nc' DataFrame according to invalid values.
# There are also invalid values in the 'context_type' column, identified as 'Inconsistent Mapping'.
nc[nc['context_type'].str.contains('Inconsistent Mapping')]


# In[23]:


# Filter the 'nc' DataFrame according to invalid values.
# There are also invalid values in the 'national_category' column, identified as 'Inconsistent Mapping'.
nc[nc['national_category'].str.contains('Inconsistent Mapping')]


# In[24]:


# Filter the 'nc' DataFrame according to invalid values.
# There are also invalid values in the 'national_category' column, identified as 'Unmapped'.

nc[nc['national_category'].str.contains('Unmapped')]


# In[25]:


# Determine the metadata of the data set.
print(nc.columns)
print(nc.shape)
print(nc.dtypes)
nc.info()


# In[26]:


# Determine the descriptive statistics of the data set.
nc.describe()


# ### Explore the data set

# **Question 1:** How many locations are there in the data set?

# In[27]:


# Determine the number of locations.
# Get Unique Count of Locations from the 'ad' DataFrame.
count = ad.sub_icb_location_name.unique().size
print("Count of locations : "+ str(count))


# **Question 2:** What are the five locations with the highest number of records?
# 
# 

# In[28]:


# Sorting the data by 'count_of_appointments' to find the 5 locations with the highest number of records.
nc.sort_values(by=['count_of_appointments'], ascending=False)
nc.head()


# In[29]:


# Grouping the nc DataFrame by 'sub_icb_location_name' and counting the number of rows for each location.
locations_count = pd.DataFrame(nc.groupby(['sub_icb_location_name']).count())
locations_count


# In[30]:


# Sorting the nc DataFrame by 'icb_ons_code' in descending order. 
# (Any of the columns could be chosen, since all of them have the same count of records).
locations_count.sort_values(['icb_ons_code'],ascending=False)


# In[31]:


# Determine the top five locations based on record count.
top_5_locations = locations_count.sort_values(['icb_ons_code'],ascending=False)
top_5_locations.head()


# **Question 3:** How many service settings, context types, national categories, and appointment statuses are there?

# In[32]:


# Determine the number of service settings.
# Determine the number of service settings from the 'nc' DataFrame.
print(len(nc['service_setting'].unique()))


# In[33]:


# Determine the number of context types from the 'nc' DataFrame.
print(len(nc['context_type'].unique()))


# In[34]:


# Determine the number of national categories from the 'nc' DataFrame.
print(len(nc['national_category'].unique()))


# In[35]:


# Determine the number of appointment statuses from the 'ar' DataFrame.
print(len(ar['appointment_status'].unique()))


# # 

# # Assignment activity 3

# ### Continue to explore the data and search for answers to more specific questions posed by the NHS.

# In[36]:


# Before I move on with the analysis. 
# I would like to search for duplicates values in the ad DataFrame.
# No duplicates were found in the ad DataFrame.
ad.duplicated()


# In[37]:


# Searching for duplicates values in the ar DataFrame.
# 21,604 raws were found to be duplicated.
ar.duplicated()


# In[38]:


# Adding a new column to the ar dataframe that states whether the row is a duplicate.
ar2 = ar.copy()
ar2['duplicated'] = ar2.duplicated()
ar2


# In[39]:


# De-duplicate the ar DataFrame using drop_duplicates().
# I decided to remove the 21,604 raws that were found to be duplicated in the ar DataFrame.
ar = ar.drop_duplicates()
ar.shape


# In[40]:


# The 'ar' DataFrame has now 575,217 rows, containing zero duplicates.
ar.duplicated()


# In[41]:


# Searching for duplicates values in the nc DataFrame.
# No duplicates were found.
nc.duplicated()


# **Question 1:** Between what dates were appointments scheduled?

# In[42]:


# Importing the nessesary modules.
import pandas as pd
import numpy as np
import datetime


# In[43]:


# View the ar DataFrame and columns to determine the format of the dates.
print(ar.dtypes)

# View the first five rows of appointment_date for the ad DataFrame to determine the date format.
ar.head()


# In[44]:


# Change the date format of ar['appointment_month'].
ar['appointment_month'] = pd.to_datetime(ar['appointment_month'])

# View the ar DataFrame and columns to determine the format of the dates.
print(ar.dtypes)


# In[45]:


# View the ad DataFrame and columns to determine the format of the dates.
print(ad.dtypes)

# View the first five rows of appointment_date for the nc DataFrame to determine the date format.
ad.head()


# In[46]:


# Change the date format of ad['appointment_date'].
ad['appointment_date'] = pd.to_datetime(ad['appointment_date'])

# View the data types of the ad DateFrame.
print(ad.dtypes)


# In[47]:


# View the nc DataFrame and columns to determine the format of the dates.
print(nc.dtypes)


# In[48]:


# Change the date format of nc['appointment_month'].
nc['appointment_month'] = pd.to_datetime(nc['appointment_month'])

# View the data type of the nc DateFrame.
print(nc.dtypes)
nc.head()


# #### Adding an additional column 'appointment_month' to the ad DataFrame.
# #### This will allow me to compare the 3 DataFrames by looking at the 'total_monthly_appointments'.

# In[49]:


#Extracting the year from string format date.
ad['year'] = pd.DatetimeIndex(ad['appointment_date']).year
ad.head()


# In[50]:


# Creating a new column with month of date field 'appointment_date'.
ad['month'] = pd.DatetimeIndex(ad['appointment_date']).month
ad.head()


# In[51]:


# Extracting the day/month/year using the to_period function.
# Where 'D', 'M', 'Y' are inputs.
ad['appointment_month'] = pd.to_datetime(ad['appointment_date']).dt.to_period('M')
ad.head()


# In[52]:


ad['appointment_month'] = pd.to_datetime(ad['appointment_date'])
ad.head()


# In[53]:


# View the ad DataFrame and columns to determine the format of the dates.
print(ad.dtypes)


# In[54]:


# Determine the minimum and maximum dates in the ad DataFrame.
# Use appropriate docstrings.
# Sort column from low to high to determine. 
print(ad['appointment_month'].sort_values())

# Determine min value (statistical method).
print(ad['appointment_month'].min())
ad.head()


# In[55]:


# Determine the last (e.g. max()) date of scheduled appointments for the ad DataFrame.
# Determine max value (statistical method).
print(ad['appointment_month'].max())
ad.tail()


# In[56]:


# Determine the minimum and maximum dates in the nc DataFrame.
# Use appropriate docstrings.
# Sort column from low to high to determine. 

print(nc['appointment_date'].sort_values())

# Determine min value (statistical method).
print(nc['appointment_date'].min())
nc.head()


# In[57]:


# Determine the last (e.g. max()) date of scheduled appointments for the nc DataFrame.
# Determine max value (statistical method).
print(nc['appointment_date'].max())
nc.tail()


# In[58]:


# Determine the minimum and maximum dates in the ar DataFrame.
# Use appropriate docstrings.
# Sort column from low to high to determine. 

print(ar['appointment_month'].sort_values())

# Determine min value (statistical method).
print(ar['appointment_month'].min())
ar.head()


# In[59]:


# Determine the last (e.g. max()) date of scheduled appointments for the nc DataFrame.
# Determine max value (statistical method).
print(ar['appointment_month'].max())
ar.tail()


# **Question 2:** Which service setting was the most popular for NHS North West London from 1 January to 1 June 2022?

# In[60]:


# Create a subset of the nc DataFrame.
# Selecting few columns.
nc_subset = pd.read_excel('national_categories.xlsx', 
                            usecols=['sub_icb_location_name', 'service_setting', 'count_of_appointments', 'appointment_date'])

# Print the DataFrame.
nc_subset.head()


# In[62]:


# View the nc DataFrame and columns to determine the format of the dates.
print(nc_subset.dtypes)


# In[63]:


# Filtering the DataFrame by the specific dates, from 1 January to 1 June 2022.
nc_subset[(nc_subset['appointment_date'] > '2022-01-01') & (nc_subset['appointment_date'] < '2022-06-01')]


# In[64]:


# Sorting the data by ''NHS North West London ICB - W2U3'.
nc_subset.loc[nc_subset['sub_icb_location_name'].str.contains('NHS North West London ICB - W2U3')]


# In[71]:


# For each of these service settings, determine the number of records available for the period and the location. 
# Count the number of records per service_setting.
ss_count = nc_subset.loc[nc_subset['sub_icb_location_name'].str.contains('NHS North West London ICB - W2U3')].groupby(['service_setting']).count()
ss_count.sort_values(['count_of_appointments'],ascending=False)
most_popular_ss = ss_count.sort_values(['count_of_appointments'],ascending=False)

# View the output.
most_popular_ss


# **Question 3:** Which month had the highest number of appointments?

# Before I can give answers to the following questions, since these questions are not specific to any DataFrame, I assume that these questions refer to the three DataFrames as a whole, so I will merge the three DataFrames.

# To be able to merge the three DataFrames, we should have comparable inputs in terms of 'count of apppointmets', being aggregated to monthly counts and the same number of rows in all the DataFrames to be merged.

# ##### Q: I grouped the ar DataFrame
# #### I want to create a subset of the ar DataFrame that includes this new column of total_monthly_appointments
# #### Come back and add all the columns I want to have in the merged DataFrame.
#     

# In[72]:


# Grouping the ar DataFrame by 'icb_ons_code' and 'appointment_month'.
# And aggregating the 'count of appointments' to total monthly appointments.
total_m_apt_ar = pd.DataFrame(ar.groupby(['icb_ons_code' ,'appointment_status', 'hcp_type', 'appointment_mode', 'appointment_month']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
total_m_apt_ar.sort_values(['total_monthly_appointments'],ascending=False)


# In[73]:


# Grouping the nc DataFrame by 'icb_ons_code' and 'appointment_month'.
# And aggregating the 'count of appointments' to total monthly appointments.
total_m_apt_nc = pd.DataFrame(nc.groupby(['icb_ons_code' ,'service_setting', 'context_type', 'national_category']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
total_m_apt_nc.sort_values(['total_monthly_appointments'],ascending=False)


# In[74]:


# Grouping the ad DataFrame by 'icb_ons_code' and 'appointment_month'.
# And aggregating the 'count of appointments' to total monthly appointments.
total_m_apt_ad = pd.DataFrame(ad.groupby(['icb_ons_code' ,'sub_icb_location_name', 'actual_duration']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
total_m_apt_ad.sort_values(['total_monthly_appointments'],ascending=False)


# In[75]:


# Merging the nc and the ar DataFrames.
total_m_apt_nc_ar = pd.merge(total_m_apt_nc, total_m_apt_ar, how='inner', on ='icb_ons_code')

# View the new DataFrame.
total_m_apt_nc_ar.head()


# In[76]:


# Drop the total 'total_monthly_appointments_x'.
new_total_m_apt_nc_ar = total_m_apt_nc_ar.drop(columns=total_m_apt_nc_ar.columns[4])

# Print the modified dataframe.
new_total_m_apt_nc_ar.head()


# In[77]:


# Print the shape of the dataframe.
new_total_m_apt_nc_ar.shape


# In[78]:


# Searching for duplicates values in the ar DataFrame.
# No duplicates were found to be duplicated.
new_total_m_apt_nc_ar.duplicated()


# In[79]:


# Merging the 'new_total_m_apt_nc_ar' and the 'total_m_apt_ad' DataFrames.
total_m_apt_nc_ar_ad = pd.merge(new_total_m_apt_nc_ar, total_m_apt_ad, how='inner', on ='icb_ons_code')
total_m_apt_nc_ar_ad.head()


# In[80]:


# Print the shape of the dataframe.
total_m_apt_nc_ar_ad.shape


# In[81]:


# Drop the total 'total_monthly_appointments_y'.
new_total_m_apt_nc_ar_ad = total_m_apt_nc_ar_ad.drop(columns=total_m_apt_nc_ar.columns[9])

# Print the modified dataframe.
new_total_m_apt_nc_ar_ad.head()


# In[82]:


# Searching for duplicates values in the ar DataFrame.
# No duplicates were found to be duplicated.
new_total_m_apt_nc_ar_ad.duplicated()


# #### Even though I already gave answers to the following questions by looking at each DataFrame individually.
# #### I want to see the outputs generated from the new merged DataFrame.

# #### 2. Between what dates were appointments scheduled?

# In[83]:


# Determine the minimum and maximum dates in the ar DataFrame.
# Use appropriate docstrings.
# Sort column from low to high to determine. 
print(new_total_m_apt_nc_ar_ad['appointment_month'].sort_values())

# Determine min value (statistical method).
print(new_total_m_apt_nc_ar_ad['appointment_month'].min())
new_total_m_apt_nc_ar_ad.head()


# In[84]:


# Determine the last (e.g. max()) date of scheduled appointments for the nc DataFrame.
# Determine max value (statistical method).
print(new_total_m_apt_nc_ar_ad['appointment_month'].max())
print(new_total_m_apt_nc_ar_ad.dtypes)
new_total_m_apt_nc_ar_ad.tail()


# In[85]:


# Sorting the data by ''NHS North West London ICB - W2U3'.
new_total_m_apt_nc_ar_ad.loc[new_total_m_apt_nc_ar_ad['sub_icb_location_name'].str.contains('NHS North West London ICB - W2U3')]


# In[86]:


# For each of these service settings, determine the number of records available for the period and the location. 
# Count the number of records per service_setting.
new_ss_count = new_total_m_apt_nc_ar_ad.loc[new_total_m_apt_nc_ar_ad['sub_icb_location_name'].str.contains('NHS North West London ICB - W2U3')].groupby(['service_setting']).count()
new_ss_count.sort_values(['total_monthly_appointments'],ascending=False)
new_most_popular_ss = new_ss_count.sort_values(['total_monthly_appointments'],ascending=False)

# View the output.
new_most_popular_ss


# #### 3. Which month had the highest number of appointments?

# In[95]:


new_total_m_apt_nc_ar_ad.head()
month_highest_appt.sort_values(['total_monthly_appointments'],ascending=False)


# In[99]:


month_highest_appt = pd.DataFrame(new_total_m_apt_nc_ar_ad.groupby(['appointment_month', 'total_monthly_appointments']))
month_highest_appt.sort_values(['total_monthly_appointments'],ascending=False)
month_highest_appt.head()


# In[ ]:


# Grouping the nc DataFrame by 'icb_ons_code' and 'appointment_month'.
# And aggregating the 'count of appointments' to total monthly appointments.
month_highest_appt = pd.DataFrame(new_total_m_apt_nc_ar_ad.groupby(['appointment_month', 'total_monthly_appointments']))
month_highest_appt.sort_values(['total_monthly_appointments'],ascending=False)


# In[ ]:


new_total_m_apt_nc_ar_ad.sort_values(by=['appointments_month'], ascending=False)


# In[ ]:


# For each of these service settings, determine the number of records available for the period and the location. 
# Count the number of records per service_setting.
new_ss_count = new_total_m_apt_nc_ar_ad.loc[new_total_m_apt_nc_ar_ad['sub_icb_location_name'].str.contains('NHS North West London ICB - W2U3')].groupby(['service_setting']).count()
new_ss_count.sort_values(['total_monthly_appointments'],ascending=False)
new_most_popular_ss = new_ss_count.sort_values(['total_monthly_appointments'],ascending=False)

# View the output.
new_most_popular_ss


new_total_m_apt_nc_ar_ad.sort_values(by=['total_monthly_appointments'], ascending=False)


# #### 4. What was the total number of records per month?

# In[153]:


# Grouping the nc DataFrame by ''sub_icb_location_name' and 'appointment_month'.
# And aggregating the 'count of appointments' to monthly counts.

monthly_appointments_count = pd.DataFrame(nc.groupby(['sub_icb_location_name' ,'appointment_month']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
monthly_appointments_count.sort_values(['total_monthly_appointments'],ascending=False)


# In[25]:


# Grouping the ad DataFrame by 'sub_icb_location_name' and 'appointment_month'.
# And aggregating the 'count of appointments' to monthly counts.

ad_total_monthly_appointments_count = pd.DataFrame(ad.groupby(['sub_icb_location_name' ,'appointment_month']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
monthly_appointments_count.sort_values(['total_monthly_appointments'],ascending=False)


# In[ ]:


# Number of appointments per month == sum of count_of_appointments by month.
# Use the groupby() and sort_values() functions

* # For each of these service settings, determine the number of records available for the period and the location. 
# Count the number of records per service_setting.
ss_count = nc_subset.loc[nc_subset['sub_icb_location_name'].str.contains('NHS North West London ICB - W2U3')].groupby(['service_setting']).count()
ss_count.sort_values(['count_of_appointments'],ascending=False)
most_popular_ss = ss_count.sort_values(['count_of_appointments'],ascending=False)

# View the output.
most_popular_ss


# In[105]:


# Grouping the merged DataFrame by 'appointment_month'.
# And aggregating the 'total_monthly_appointments' to 'TOTAL_Monthly Appointments'.

TOTAL_m_apt = pd.DataFrame(new_total_m_apt_nc_ar_ad.groupby(['appointment_month', 'total_monthly_appointments']))
TOTAL_m_apt.sort_values(['total_monthly_appointments'],ascending=False)


# **Question 4:** What was the total number of records per month?

# In[ ]:


# Total number of records per month.
new_total_m_apt_nc_ar_ad.sort_values(['appointment_month'],ascending=False)


# # 

# # Assignment activity 4

# ### Create visualisations and identify possible monthly and seasonal trends in the data.

# In[4]:


# Import the necessary Libraries.
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import *

# Set figure size.
sns.set(rc={'figure.figsize':(15, 12)})

# Set the plot style as white.
sns.set_style('white')


# In[5]:


# Read the Excel file.
# Assign a variable.
# Use the pd.read_excel() function.
# Specify the name of the Excel file.
nc = pd.read_excel('national_categories.xlsx')

# Print the top 5 raws of the nc DataFrame.
nc.head()


# In[6]:


# Determine shape and data types of the national_category data set.
print(nc.shape)
print(nc.dtypes)


# ### Objective 1
# Create three visualisations indicating the number of appointments per month for service settings, context types, and national categories.

# In[7]:


# Change the data type of the appointment month to string to allow for easier plotting.
import datetime


# In[8]:


# Create a subset of the nc DataFrame.

# Selecting few columns.
nc_ss_subset = pd.read_excel('national_categories.xlsx', 
                            usecols=['service_setting', 'count_of_appointments', 'appointment_date','appointment_month'])

# Print the DataFrame.
nc_ss_subset.head()


# In[9]:


# Extracting the year from string format date.
nc_ss_subset['year'] = pd.DatetimeIndex(nc_ss_subset['appointment_date']).year
nc_ss_subset.head()


# In[10]:


# Creating a new column with month of date field 'appointment_date'.
nc_ss_subset['month'] = pd.DatetimeIndex(nc_ss_subset['appointment_date']).month
nc_ss_subset.head()


# In[11]:


# Aggregate on monthly level and determine the sum of records per month.
# Grouping the nc DataFrame by 'service_setting', 'year' and 'month'.
# And aggregating the 'count of appointments' to monthly counts.

nc_ss_subset= pd.DataFrame(nc_ss_subset.groupby(['service_setting','year','month', 'appointment_month', 'appointment_date',]).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
nc_ss_subset.sort_values(['total_monthly_appointments'],ascending=False)

# Create a new nc DataFrame that can be used in future weeks.
nc_ss = nc_ss_subset.sort_values(['total_monthly_appointments'],ascending=False)

# View the output.
nc_ss


# **Service settings:**

# In[13]:


# Plot the appointments over the available date range, and review the service settings for months.

# Create a lineplot.
total_monthly_appointments_ss = nc_ss['total_monthly_appointments']
sns.lineplot(x='month', y='total_monthly_appointments', hue= 'service_setting', data=nc_ss)


# **Context types:**

# In[14]:


# Create a subset of the nc DataFrame to look at context type.
# Selecting few columns.

nc_ct_subset = pd.read_excel('national_categories.xlsx', 
                            usecols=['context_type', 'count_of_appointments', 'appointment_date','appointment_month'])

# Print the DataFrame.
nc_ct_subset.head()


# In[15]:


# Extracting the year from string format date.
nc_ct_subset['year'] = pd.DatetimeIndex(nc_ct_subset['appointment_date']).year
nc_ct_subset.head()


# In[16]:


# Creating a new column with month of date field 'appointment_date'.
nc_ct_subset['month'] = pd.DatetimeIndex(nc_ct_subset['appointment_date']).month
nc_ct_subset.head()


# In[17]:


# Aggregate on monthly level and determine the sum of records per month.
# Grouping the nc DataFrame by 'service_setting', 'year' and 'month'.
# And aggregating the 'count of appointments' to monthly counts.

nc_ct_subset= pd.DataFrame(nc_ct_subset.groupby(['context_type','year','month', 'appointment_month', 'appointment_date',]).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
nc_ct_subset.sort_values(['total_monthly_appointments'],ascending=False)

# Create a new nc DataFrame that can be used in future weeks.
nc_ct = nc_ct_subset.sort_values(['total_monthly_appointments'],ascending=False)

# View the output.
nc_ct


# In[19]:


# Plot the appointments over the available date range, and review the context types for months.
# Create a lineplot.
total_monthly_appointments_ct = nc_ct['total_monthly_appointments']
sns.lineplot(x='month', y='total_monthly_appointments', hue= 'context_type', data=nc_ct, ci=0)


# **National categories:**

# In[20]:


# Create a subset of the nc DataFrame to look at the national categories.
# Selecting few columns.

nc_nc_subset = pd.read_excel('national_categories.xlsx', 
                            usecols=['national_category', 'count_of_appointments', 'appointment_date','appointment_month'])

# Print the DataFrame.
nc_nc_subset.head()


# In[21]:


# Extracting the year from string format date.
nc_nc_subset['year'] = pd.DatetimeIndex(nc_nc_subset['appointment_date']).year
nc_nc_subset.head()


# In[22]:


# Creating a new column with month of date field 'appointment_date'.
nc_nc_subset['month'] = pd.DatetimeIndex(nc_nc_subset['appointment_date']).month
nc_nc_subset.head()


# In[23]:


# Aggregate on monthly level and determine the sum of records per month.
# Grouping the nc DataFrame by 'national_category', 'year' and 'month'.
# And aggregating the 'count of appointments' to monthly counts.

nc_nc_subset= pd.DataFrame(nc_nc_subset.groupby(['national_category','year','month', 'appointment_month', 'appointment_date',]).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
nc_nc_subset.sort_values(['total_monthly_appointments'],ascending=False)

# Create a new nc DataFrame that can be used in future weeks.
nc_nc = nc_nc_subset.sort_values(['total_monthly_appointments'],ascending=False)

# View the output.
nc_nc


# In[24]:


# Plot the appointments over the available date range, and review the national categories for months.
# Create a lineplot.
total_monthly_appointments_nc = nc_nc['total_monthly_appointments']
sns.lineplot(x='month', y='total_monthly_appointments', hue= 'national_category', data=nc_nc, ci=0)


# ### Objective 2
# Create four visualisations indicating the number of appointments for service setting per season. The seasons are summer (August 2021), autumn (October 2021), winter (January 2022), and spring (April 2022).

# **Summer (August 2021):**

# In[70]:


# View the output.
nc_ss
print(nc_ss.dtypes)
nc_ss


# In[76]:


# Look at August 2021 in more detail to allow a closer look.
# Create a lineplot.
summer = nc_ss.query("appointment_month =='2021-08'")
sns.lineplot(data=summer, x="appointment_date", y="total_monthly_appointments", hue='service_setting', errorbar=('ci', 0)).set_title("Summer 2021 - Appointments")


# **Autumn (October 2021):**

# In[75]:


# Look at October 2021 in more detail to allow a closer look.
# Create a lineplot.
autumn = nc_ss.query("appointment_month =='2021-10'")
sns.lineplot(data=autumn, x="appointment_date", y="total_monthly_appointments", hue= 'service_setting', errorbar=('ci', 0)).set_title("Autumn 2021 - Appointments")


# **Winter (January 2022):**

# In[74]:


# Look at January 2022 in more detail to allow a closer look.
# Create a lineplot.
winter = nc_ss.query("appointment_month =='2022-01'")
sns.lineplot(data=winter, x="appointment_date", y="total_monthly_appointments", hue='service_setting', errorbar=('ci', 0)).set_title("Winter 2022 - Appointments")


# **Spring (April 2022):**

# In[77]:


# Look at April 2022 in more detail to allow a closer look.
# Create a lineplot.
spring = nc_ss.query("appointment_month =='2022-04'")
sns.lineplot(data=spring, x="appointment_date", y="total_monthly_appointments", hue='service_setting', errorbar=('ci', 0)).set_title("Spring 2022 - Appointments")


# # Assignment activity 5

# ### Analyse tweets from Twitter with hashtags related to healthcare in the UK.

# In[1]:


# Libraries and settings needed for analysis
import pandas as pd
import seaborn as sns

# Set figure size.
sns.set(rc={'figure.figsize':(15, 12)})

# Set the plot style as white.
sns.set_style('white')

# Maximum column width to display
pd.options.display.max_colwidth = 200


# In[2]:


# Load the data set.
tweets = pd.read_csv('tweets.csv')

# View the DataFrame.
tweets.head()


# In[3]:


# Explore the metadata.
print(tweets.columns)
print(tweets.shape)
print(tweets.dtypes)
tweets.info()


# In[4]:


# Determine the descriptive statistics of the tweets data set. Explore the data set.
tweets.describe()


# In[5]:


# Searching for duplicates values in the ar DataFrame.
# No duplicates were found to be duplicated.
tweets.duplicated()


# In[6]:


# Adding a new column to the ar dataframe that states whether the row is a duplicate.
tweets2 = tweets.copy()
tweets2['duplicated'] = tweets2.duplicated()
tweets2


# In[7]:


# De-duplicate the tweets DataFrame using drop_duplicates().
# I decided to remove the 205 raws that were found to be duplicated in the tweets DataFrame.
tweets = tweets.drop_duplicates()
tweets.shape


# In[8]:


# Would it be useful to only look at retweeted and favourite tweet messages?
# Explain your answer.
# I think that sorting these two columns by the higuest number of retweets and the most favourite tweets will enable me to identify the most popular tweets by number of retweets and number of times that people marked them as favorites. 
# Afterwards, we will be able to look at the full text and hashtags used.


# In[9]:


# Sorting the data by 'tweet_retweet_count' to find the tweets with the highest number of retweets.
tweets.sort_values(by=['tweet_retweet_count'], ascending=False)


# In[10]:


# Sorting the data by 'tweet_favorite_count' to find the tweets that were marked the most as favorite.
tweets.sort_values(by=['tweet_favorite_count'], ascending=False)


# In[11]:


# Create a new DataFrame containing only the text, selecting only 'tweet_full_text'.
tweets_text = pd.read_csv('tweets.csv', 
                            usecols=['tweet_full_text'])

# Print the first 5 raws of the DataFrame.
tweets_text.head()


# In[40]:


# Loop through the messages, and create a list of values containing the # symbol.
tags = list()
for y in [x.split(' ') for x in tweets['tweet_full_text'].values]:
    for z in y:
        if '#' in z:
            # Change to lowercase.
            tags.append(z.lower())
            
# View the output.
top_trending_hashtags = tags
top_trending_hashtags


# In[57]:


# Create a Pandas Series to count the values in the list. Set the Series equal to tags.
tags = pd.Series(top_trending_hashtags)
print(tags)
tags.head(30)


# In[26]:


# Create a Pandas Series to count the values in the list. Set the Series equal to tags.                                 
tags = pd.DataFrame(tweets_text.groupby(['tweet_full_text']).count())
tags.head(30)


# In[33]:


# Determine the number of service settings from the 'nc' DataFrame.
print(len(tweets_text['tweet_full_text'].unique()))


# In[36]:


# Create a user-defined function using the def keyword.
# Name the function as contains_healthcare.
# Specify the named parameter as (x).
# Specify what the function should do. For example, does the product contain the word matches in their description?. 
# The triple quotation marks (""" """) indicates to Python it is a docstring.
# The second line of code indicates that y is testing the parameter (x.lower()). 
# For example, identify whether the lower case word healthcare is in the function x. 
# Specify the return keyword to execute the function. For example, does the lower case word matches appear in y?.

def contains_healthcare(x):
    """ does the tweet full text contain #healthcare? """
    y = x.lower()
    return "#healthcare" in y

# Print the function by testing various options of the word matches. 
# For example, matches and Matches.
# View the output.
print(contains_healthcare(x="#healthcare"))
print(contains_healthcare(x="#Healthcare"))


# In[38]:


# Use the apply() function.
tags_healthcare = tweets_text["tweet_full_text"].apply(contains_healthcare)

# View the DataFrame.
print(tags_healthcare)

# Filter the DataFrame.
tweets_text[tags_healthcare]
tweets_text[tags_healthcare].shape


# ### A total of 842 hashtags contain the word 'healthcare'. Originally there were 961 unique comments in the tweet_full_text column. Therefore, 87.6% of the tweets contain the word 'healthcare.

# In[61]:


# Create a Pandas Series to count the values in the list. Set the Series equal to tags.
tags = pd.Series(top_trending_hashtags)
print(tags)
tags.head(30)


# In[63]:


print(type(tags))


# In[72]:


# Convert the series to a DataFrame in preparation for visualisation.
# Creating two lists.

import numpy as np

word = ['#healthcare', '#premisehealth', '#hiring', '#healthcare', '🚨#new:🚨', 'look!\n\n#blogs', 
        '#digitaltransformation', '#cybersecurity', '#accounting', '#finance', '#healthcare', 
        '#firstcoastcna', '#cnaexam', '#cnaexampreparation','#jacksonville', '#cnatraining', '#nurse', 
        '#nursing', '#nurselife', '#nursepractitioner','#nurseproblems', '#nursingschool','#healthcare', 
        '🚨#new:🚨', '#disparities','@karahartnett\n#healthcare','#alert', '#insurance', '#data', '#healthcare']

count = []

# Creating two series by passing lists.
word_series = pd.Series(word)
count_series = pd.Series(dtype=np.int64)

# Creating a dictionary by passing Series objects as values.
frame = {'Word': word_series,
         'Count': count_series}

# Creating DataFrame by passing Dictionary.
top_trending_hashtags = pd.DataFrame(frame)
 
# Printing elements of Dataframe
print(top_trending_hashtags)


# In[88]:


# Count the number of hashtags per tweet_full_text.
top_trending_hashtags = top_trending_hashtags.groupby(['Word']).count()

top_trending_hashtags.sort_values(['Count'],ascending=False)
top_trending_hashtags = top_trending_hashtags.sort_values(['Count'],ascending=False)

# View the output.
top_trending_hashtags


# In[91]:


# Convert the series to a DataFrame in preparation for visualisation.
# Creating two lists.

import numpy as np

word = [tags]

count = []

# Creating two series by passing lists.
word_series = pd.Series(word)
count_series = pd.Series(dtype=np.int64)

# Creating a dictionary by passing Series objects as values.
frame = {'Word': tags,
         'Count': count_series}

# Creating DataFrame by passing Dictionary.
top_trending_hashtags = pd.DataFrame(frame)
 
# Printing elements of Dataframe
print(top_trending_hashtags)


# In[104]:


# Count the number of unique hashtags.
top_trending_unique_hashtags = top_trending_hashtags.groupby(['Word']).count()
top_trending_unique_hashtags.sort_values(['Count'],ascending=False)

# View the output.
top_trending_unique_hashtags


# In[110]:


top_trending_unique_hashtags = pd.DataFrame(top_trending_hashtags.groupby(['Word' ,'Count']).Count.sum().reset_index(name='total_#'))
top_trending_unique_hashtags.head(50)


# In[122]:


top_trending_unique_hashtags = top_trending_hashtags.groupby(['Word']).count()
top_trending_unique_hashtags.sort_values(['Count'],ascending=False)


# In[123]:


# View the output.
top_trending_unique_hashtags
print(len(top_trending_unique_hashtags['Word'].nunique()))


# In[105]:


# Ensure the count data type is an integer for data analysis.
print(top_trending_unique_hashtags.dtypes)


# In[ ]:


# Fix the count datatype.


# View the result.


# In[ ]:


# Display records where the count is larger than 10.


# In[ ]:


# Create a Seaborn barplot indicating records with a count >10 records.


# In[ ]:


# Create the plot.


# View the barplot.


# # 

# # Assignment activity 6

# ### Investigate the main cencerns posed by the NHS. 

# In[ ]:


# Prepare your workstation.
# Load the appointments_regional.csv file.


# View the DataFrame.


# In[ ]:


# Print the min and max dates.


# In[ ]:


# Filter the data set to only look at data from 2021-08 onwards.


# **Question 1:** Should the NHS start looking at increasing staff levels? 

# In[ ]:


# Create an aggregated data set to review the different features.


# View the DataFrame.


# In[ ]:


# Determine the total number of appointments per month.


# Add a new column to indicate the average utilisation of services.
# Monthly aggregate / 30 to get to a daily value.


# View the DataFrame.


# In[ ]:


# Plot sum of count of monthly visits.
# Convert the appointment_month to string data type for ease of visualisation.


# Create a lineplot with Seaborn.


# In[ ]:


# Plot monthly capacity utilisation.


# Create a lineplot.


# **Question 2:** How do the healthcare professional types differ over time?

# In[ ]:


# Create a line plot to answer the question.


# **Question 3:** Are there significant changes in whether or not visits are attended?

# In[ ]:


# Create a line plot to answer the question.


# **Question 4:** Are there changes in terms of appointment type and the busiest months?

# In[ ]:


# Create a line plot to answer the question.


# **Question 5:** Are there any trends in time between booking an appointment?

# In[ ]:


# Create a line plot to answer the question.


# **Question 6:** How do the spread of service settings compare?

# In[ ]:


# Let's go back to the national category DataFrame you created in an earlier assignment activity.


# In[ ]:


# Create a new DataFrame consisting of the month of appointment and the number of appointments.

# View the DataFrame.


# In[1]:


# Create a boxplot to investigate spread of service settings.


# In[ ]:


# Create a boxplot to investigate the service settings without GP.


# # 

# ### Provide a summary of your findings and recommendations based on the analysis.

# > Double click to insert your summary.

# In[ ]:




