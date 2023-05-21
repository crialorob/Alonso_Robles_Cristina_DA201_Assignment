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

# In[1]:


# Import the necessary libraries.
import pandas as pd
import numpy as np
import datetime

# Optional - Ignore warnings.
import warnings
warnings.filterwarnings('ignore')


# In[2]:


# Import and sense-check the actual_duration.csv data set as ad.
ad = pd.read_csv('actual_duration.csv')

# View the DataFrame.
ad.head()


# In[3]:


# Determine whether there are missing values.
ad_na = ad[ad.isna().any(axis=1)]
ad_na.shape


# In[4]:


# Determine the sum of missing values in the 'ad' DataFrame.
ad['actual_duration'].isnull().sum()


# There are invalid/erroneous values in the 'actual_duration' column, identified as'Unknown / Data Quality'.
# 
# Python does not identify them as missing values, however I will take a look at the scale of these erroneous values for my awareness and better understanding of the quality of the data.

# In[5]:


# Filter the 'ad' DataFrame according to invalid values.
# There are invalid values in the 'actual_duration' column, identified as 'Unknown / Data Quality'.
ad[ad['actual_duration'].str.contains('Unknown / Data Quality')]


# #### 20,161 (14.6%) rows from the ad DataFrame  were identified as 'Unknown / Data Quality' as the actual duration of the appointment.

# In[6]:


# Determine the metadata of the data set.
print(ad.columns)
print(ad.shape)
print(ad.dtypes)
ad.info()


# In[7]:


# Determine the descriptive statistics of the data set.
ad.describe()


# In[8]:


# Import and sense-check the appointments_regional.csv data set as ar.
ar = pd.read_csv('appointments_regional.csv')

# View the DataFrame.
ar.head()


# In[9]:


# Determine whether there are missing values.
ar_na = ar[ar.isna().any(axis=1)]
ar_na.shape


# In[10]:


# Determine the sum of missing values.
ar['appointment_status'].isnull().sum()
ar['hcp_type'].isnull().sum()
ar['time_between_book_and_appointment'].isnull().sum()


# There are invalid/erroneous values in the 'appointment_status' and in the 'hcp_type' columns, identified as 'Unknown'. There are also invalid values in the 'time_between_book_and_appointment' column, identified as 'Unknown / Data Quality'. Python does not identify them as missing values, however I will take a look at the scale of these erroneous values for my awareness and better understanding of the quality of the data.

# In[11]:


# Filter the 'ar' DataFrame according to invalid values.
# There are invalid values in the 'appointment_status' column, identified as 'Unknown'. 
ar[ar['appointment_status'].str.contains("Unknown")]


# #### 201,324 (33.7%) rows from the ar DataFrame were identified as having an 'Unknown' appointment status.

# In[12]:


# Filter the 'ar' DataFrame according to invalid values.
# There are wrong values in the 'hcp_type' column, identified as 'Unknown'. 
ar[ar['hcp_type'].str.contains("Unknown")]


# #### 129,228 (21.6%) rows from the ar DataFrame were identified as having an 'Unknown' Healthcare Professional Type.

# In[13]:


# Filter the 'ar' DataFrame according to invalid values.
# There are invalid values in the 'time_between_book_and_appointment' column, identified as 'Unknown / Data Quality'.
ar[ar['time_between_book_and_appointment'].str.contains('Unknown / Data Quality')]


# #### 29,687(4.9%) rows from the ar DataFrame were identified as having an 'Unknown / Data Quality' as the Time Between Book and Appointment.

# In[14]:


# Determine the metadata of the ar data set.
# Determine the metadata of the data set.
print(ar.columns)
print(ar.shape)
print(ar.dtypes)
ar.info()


# In[15]:


# Determine the descriptive statistics of the ar data set.
ar.describe()


# In[16]:


# Import and sense-check the national_categories.xlsx data set as nc.
nc = pd.read_excel('national_categories.xlsx')

# View the DataFrame.
nc.head()


# In[17]:


# Determine whether there are missing values.
nc_na = nc[nc.isna().any(axis=1)]
nc_na.shape


# In[18]:


# Determine the sum of missing values in the 'ar' DataFrame.
nc['service_setting'].isnull().sum()
nc['context_type'].isnull().sum()
nc['national_category'].isnull().sum()


# There are invalid values in the 'service_setting' column, identified as 'Unmapped'. There are also invalid values in the 'context_type' and 'national_category' columns, identified as 'Inconsistent Mapping' and 'Unmapped'. Python does not identify them as missing values, however I will take a look at the scale of these erroneous values for my awareness and better understanding of the quality of the data.

# In[19]:


# Filter the 'nc' DataFrame according to invalid values.
# There are invalid values in the 'service_setting' column, identified as 'Unmapped'.
nc[nc['service_setting'].str.contains('Unmapped')]


# #### 27,419(3.4%) rows from the nc DataFrame were identified as having an 'Unmapped'as the Service Setting of the Appointment.

# In[20]:


# Filter the 'nc' DataFrame according to invalid values.
# There are also invalid values in the 'context_type' column, identified as 'Unmapped'.
nc[nc['context_type'].str.contains('Unmapped')]


# #### 27,419 (3.4%) rows from the nc DataFrame were identified as having an 'Unmapped'as the Context Type of the Appointment. These coincide with the number of rows that have an unmapped Service Setting too.

# In[21]:


# Filter the 'nc' DataFrame according to invalid values.
# There are also invalid values in the 'context_type' column, identified as 'Inconsistent Mapping'.
nc[nc['context_type'].str.contains('Inconsistent Mapping')]


# #### 89,494 (10.9%) rows from the nc DataFrame were identified as having an 'Unmapped'as the Context Type of the Appointment.

# In[22]:


# Filter the 'nc' DataFrame according to invalid values.
# There are also invalid values in the 'national_category' column, identified as 'Inconsistent Mapping'.
nc[nc['national_category'].str.contains('Inconsistent Mapping')]


# #### 89,494 (10.9%) rows from the nc DataFrame were identified as having an 'Inconsistent Mapping'as the National Category of the Appointment. These coincide with the number of rows that have an unmapped Context Type too.

# In[23]:


# Filter the 'nc' DataFrame according to invalid values.
# There are also invalid values in the 'national_category' column, identified as 'Unmapped'.
nc[nc['national_category'].str.contains('Unmapped')]


# 27,419(3.4%) rows from the nc DataFrame were identified as having an 'Unmapped'National Category of the Appointment. These coincide with the number of rows that have an unmapped Service Setting and unmapped Context Type too.

# #### It might be worth further investigating these issues in the future and indentifying the ICB and Sub ICB Locations linked to these mapping errors. For the purpose of this analysis, I will continue to work with the entire data sets that contain these mapping errors to give insights to the stakeholders on the scale of the issue.

# In[24]:


# Determine the metadata of the nc data set.
print(nc.columns)
print(nc.shape)
print(nc.dtypes)
nc.info()


# In[25]:


# Determine the descriptive statistics of the nc data set.
nc.describe()


# ### Explore the data set

# **Question 1:** How many locations are there in the data set?

# In[26]:


# Determine the number of locations.
# Get Unique Count of Locations from the 'ad' DataFrame. 
# I checked the count of Locations in the other 2 data sets and it coincides.
count = ad.sub_icb_location_name.unique().size
print("Count of locations : "+ str(count))


# **Question 2:** What are the five locations with the highest number of records?
# 
# 

# In[27]:


# Determine the top five locations based on record count.
# Sorting the nc data set by 'count_of_appointments' to find the 5 locations with the highest number of records.
nc.sort_values(by=['count_of_appointments'], ascending=False)
nc.head()

# Grouping the nc DataFrame by 'sub_icb_location_name' and counting the number of rows for each location.
locations_count = pd.DataFrame(nc.groupby(['sub_icb_location_name']).count())
locations_count

# Sorting the nc DataFrame by 'icb_ons_code' in descending order. 
# (Any of the columns could be chosen, since all of them have the same count of records).
locations_count.sort_values(['icb_ons_code'],ascending=False)

# Determine the top five locations based on record count.
top_5_locations = locations_count.sort_values(['icb_ons_code'],ascending=False)
top_5_locations.head()


# **Question 3:** How many service settings, context types, national categories, and appointment statuses are there?

# In[28]:


# Determine the number of service settings from the 'nc' DataFrame.
print(len(nc['service_setting'].unique()))


# In[29]:


# Determine the number of context types from the 'nc' DataFrame.
print(len(nc['context_type'].unique()))


# In[30]:


# Determine the number of national categories from the 'nc' DataFrame.
print(len(nc['national_category'].unique()))


# In[31]:


# Determine the number of appointment status.
# Determine the number of appointment statuses from the 'ar' DataFrame.
print(len(ar['appointment_status'].unique()))


# # 

# # Assignment activity 3

# ### Continue to explore the data and search for answers to more specific questions posed by the NHS.

# **Question 1:** Between what dates were appointments scheduled? 

# In[32]:


# View the first five rows of appointment_date for the ad DataFrame to determine the date format.
print(ad.dtypes)
ad.head()


# In[33]:


# Change the date format of ad['appointment_date'].
ad['appointment_date'] = pd.to_datetime(ad['appointment_date'])

# View the ar DataFrame and columns to determine the format of the dates.
print(ad.dtypes)

# View the DateFrame.
ad.head()


# In[34]:


# Determine the minimum date in the ad DataFrame.
# Use appropriate docstrings.
# Sort column from low to high to determine. 
print(ad['appointment_date'].sort_values())

# Determine min value (statistical method).
print(ad['appointment_date'].min())
ad.head()


# In[35]:


# Determine the last date of scheduled appointments for the ad DataFrame.
# Determine max value (statistical method).
print(ad['appointment_date'].max())
ad.tail()


# In[36]:


# View the first five rows of appointment_date for the nc DataFrame to determine the date format.
print(nc.dtypes)
nc.head()


# In[37]:


# Change the date format of nc['appointment_month'].
nc['appointment_month'] = pd.to_datetime(nc['appointment_month'])

# View the ar DataFrame and columns to determine the format of the dates.
print(nc.dtypes)

# View the DateFrame.
nc.head()


# In[38]:


# Determine the minimum date in the nc DataFrame.
# Use appropriate docstrings.
# Sort column from low to high to determine. 
print(nc['appointment_date'].sort_values())

# Determine min value (statistical method).
print(nc['appointment_date'].min())


# In[39]:


# Determine the maximum date in the nc DataFrame.
# Use appropriate docstrings.
# Determine max value (statistical method).
print(nc['appointment_date'].max())
nc.tail()


# In[40]:


# View the first five rows of appointment_date for the ar DataFrame to determine the date format.
print(ar.dtypes)
ar.head()


# In[41]:


# Change the date format of ar['appointment_month'].
ar['appointment_month'] = pd.to_datetime(ar['appointment_month'])

# View the ar DataFrame and columns to determine the format of the dates.
print(ar.dtypes)

# View the DateFrame.
ar.head()


# There are not 'appointment_date' column in the ar DataFrame, hence the day populated under the appointmenth_month column is not correct. 
# I will use only the month and the year to confirm the minimum and maximum dates in the ar DataFrame.

# In[42]:


# Determine the minimum date in the ar DataFrame.
# Use appropriate docstrings.
# Sort column from low to high to determine. 
print(ar['appointment_month'].sort_values())

# Determine min value (statistical method).
print(ar['appointment_month'].min())


# In[43]:


# Determine the maximum date in the ar DataFrame.
# Use appropriate docstrings.
# Determine max value (statistical method).
print(ar['appointment_month'].max())
ar.tail()


# Before I can give answers to the following questions, since these questions are not specific to any DataFrame, I assume that these questions refer to the three DataFrames as a whole, so I will merge the three DataFrames.
# 
# To be able to merge the three DataFrames, we should have comparable inputs in terms of 'count of apppointmets' aggregated to monthly counts, and zero duplicate values.
# 
# Before I merge the three DataFrames, I will create a subset of each DataFrame so that I can include a new column of total_monthly_appointments.

# Date of appointment (appointment_date): The date the appointment was made for by the patient.
# 
# Month of appointment (appointment_month): The month in which the appointment is.
# 
# Based on the above notes from the metadata, I would use only the appointment_month column from the nc DataFrame, since this column reflects the month in which the appointment is. However, when I search for duplicates, Ptyhon will identify duplicates when the appointment_date is not included in the DataFrame, and I do not feel confident removing any duplicates from the nc DataFrame. So, I will include the appointment_date column.

# In[44]:


# Create a subset of the nc DataFrame.
# Selecting few columns.
nc_subset = pd.read_excel('national_categories.xlsx', 
                            usecols=['icb_ons_code','sub_icb_location_name', 'service_setting', 'context_type','national_category','count_of_appointments', 'appointment_date','appointment_month'])

# Print the DataFrame.
nc_subset.head()


# In[45]:


# Searching for duplicates values in the nc_subset DataFrame before merging the DataFrames.
# No duplicates were found in the ad DataFrame.
nc_subset.duplicated()


# In[46]:


# View the nc_subset DataFrame and columns to determine the format of the dates.
print(nc_subset.dtypes)

# View the first five rows of appointment_date for the nc DataFrame to determine the date format.
nc_subset.head()


# In[47]:


# Change the date format of the 'appointment_month'.
nc_subset['appointment_month'] = pd.to_datetime(nc_subset['appointment_month'])

# View the nc_subset DataFrame and columns to determine the format of the dates.
print(nc_subset.dtypes)


# In[48]:


# Aggregating the 'count of appointments' of the nc_subset DataFrame to total monthly appointments.
t_m_appt_nc_subset = pd.DataFrame(nc_subset.groupby(['icb_ons_code', 'sub_icb_location_name' ,'service_setting', 'context_type', 'national_category','appointment_month']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
t_m_appt_nc_subset.sort_values(['total_monthly_appointments'],ascending=False)


# I will do the same process with the ar DataFrame and finally I will merge the ad_subset DataFrame.

# In[49]:


# Create a subset of the ar DataFrame.
# Selecting few columns.
ar_subset = pd.read_excel('appointments_regional.xlsx', 
                            usecols=['icb_ons_code', 'appointment_status', 'hcp_type','appointment_mode', 'time_between_book_and_appointment', 'count_of_appointments', 'appointment_month'])

# Print the DataFrame.
ar_subset.head()


# In[50]:


# Searching for duplicates values in the ar_subset DataFrame before merging the DataFrames.
# Duplicates were found.
ar_subset.duplicated()


# In[51]:


# De-duplicate the ar DataFrame using drop_duplicates().
# I decided to remove the 21,604 raws that were found to be duplicated in the ar DataFrame.
ar_subset = ar_subset.drop_duplicates()
ar_subset.shape


# In[52]:


# View the ar_subset DataFrame and columns to determine the format of the dates.
print(ar_subset.dtypes)

# View the first five rows of appointment_date for the nc DataFrame to determine the date format.
ar_subset.head()


# In[53]:


# Change the date format of the 'appointment_month'.
ar_subset['appointment_month'] = pd.to_datetime(ar_subset['appointment_month'])

# View the ar DataFrame and columns to determine the format of the dates.
print(ar_subset.dtypes)


# In[54]:


# Aggregating the 'count of appointments' of the ar_subset DataFrame to total monthly appointments.
t_m_appt_ar_subset = pd.DataFrame(ar_subset.groupby(['icb_ons_code','appointment_status' ,'hcp_type', 'appointment_mode', 'time_between_book_and_appointment', 'appointment_month']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
t_m_appt_ar_subset.sort_values(['total_monthly_appointments'],ascending=False)


# In[55]:


# Aggregating the 'count of appointments' of the ar_subset DataFrame to total monthly appointments.
t_m_appt_ar_subset = pd.DataFrame(ar_subset.groupby(['icb_ons_code','appointment_status' ,'hcp_type', 'appointment_mode', 'time_between_book_and_appointment']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
t_m_appt_ar_subset.sort_values(['total_monthly_appointments'],ascending=False)


# In[56]:


# Aggregating the 'count of appointments' of the nc_subset DataFrame to total monthly appointments and removing the appointment_month column.
t_m_appt_nc_subset = pd.DataFrame(nc_subset.groupby(['icb_ons_code', 'sub_icb_location_name' ,'service_setting', 'context_type', 'national_category']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
t_m_appt_nc_subset.sort_values(['total_monthly_appointments'],ascending=False)


# In[57]:


# Merging the nc_subset and the ar_subset DataFrames first.
total_m_appt_nc_ar = pd.merge(t_m_appt_nc_subset, t_m_appt_ar_subset, how='inner', on ='icb_ons_code')

# View the new DataFrame.
total_m_appt_nc_ar.head()


# In[58]:


# Drop the total 'total_monthly_appointments_x'.
# Otherwise, Python will not allow me to merge the total_m_appt_nc_ar DataFrame with a third column with the same name.
# This column seems to reflect the count of records with the same values in that row, and we have the total monthly appointments number in the 'total_monthly_appointments_y'.
new_total_m_appt_nc_ar = total_m_appt_nc_ar.drop(columns=total_m_appt_nc_ar.columns[5])

# Print the modified dataframe.
new_total_m_appt_nc_ar.head()


# The Kernel died when I tried to merge the DataFrames with the appointment_month columns, hence I decided to group the DataFrames without these columns. 
# 
# However, after spending a lot of time trying to merge the three DataFrames, I decided to move on with the analysis without the merge, since I was not felling confident with the outcome that I got, since I could not see the appointment_month, which is the month in which the appointment took place.
# 

# To give answer to the next questions, I will use the nc DataFrame.

# **Question 2:** Which service setting was the most popular for NHS North West London from 1 January to 1 June 2022?

# In[60]:


# View the nc DataFrame and columns to determine the format of the dates.
print(nc.dtypes)


# In[62]:


# Filtering the nc DataFrame by the specific dates, from 1 January to 1 June 2022.
nc[(nc['appointment_date'] > '2022-01-01') & (nc['appointment_date'] < '2022-06-01')]


# In[63]:


# Sorting the nc DataFrame by ''NHS North West London ICB - W2U3'.
nc_subset.loc[nc_subset['sub_icb_location_name'].str.contains('NHS North West London ICB - W2U3')]


# In[64]:


# For each of these service settings, determine the number of records available for the period and the location. 
# Count the number of records per service_setting.
ss_count = nc.loc[nc['sub_icb_location_name'].str.contains('NHS North West London ICB - W2U3')].groupby(['service_setting']).count()
ss_count.sort_values(['count_of_appointments'],ascending=False)
most_popular_ss = ss_count.sort_values(['count_of_appointments'],ascending=False)

# View the output.
most_popular_ss


# **Question 3:** Which month had the highest number of appointments?

# In[65]:


# Grouping the nc DataFrame by 'appointment_month' to determine the appointments by month.
# And aggregating the 'count of appointments' to total monthly appointments.
nc = pd.DataFrame(nc.groupby(['appointment_month']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
nc.sort_values(['total_monthly_appointments'],ascending=False)


# **Question 4:** What was the total number of records per month?

# In[66]:


# I will use the nc_subset DataFrame.
nc_subset.head()


# In[76]:


# Total number of records per month.
records_count = nc_subset.groupby(['appointment_month'])['sub_icb_location_name'].count().reset_index(name='Count')
records_count.sort_values(by=['Count'], ascending=False)


# # 

# # Assignment activity 4

# ### Create visualisations and identify possible monthly and seasonal trends in the data.

# In[77]:


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


# In[78]:


# Read the Excel file.
# Assign a variable.
# Use the pd.read_excel() function.
# Specify the name of the Excel file.
nc = pd.read_excel('national_categories.xlsx')

# Print the top 5 raws of the nc DataFrame.
nc.head()


# In[79]:


# Determine shape and data types of the national_category data set.
print(nc.shape)
print(nc.dtypes)


# ### Objective 1
# Create three visualisations indicating the number of appointments per month for service settings, context types, and national categories.

# In[115]:


# Aggregate on monthly level and determine the sum of records per month.
import datetime

# Create a subset of the nc DataFrame.

# Selecting few columns.
nc_ss_subset = pd.read_excel('national_categories.xlsx', 
                            usecols=['service_setting', 'count_of_appointments', 'appointment_date','appointment_month'])

# Print the DataFrame.
nc_ss_subset.head()


# In[116]:


# Extracting the year from string format date.
nc_ss_subset['year'] = pd.DatetimeIndex(nc_ss_subset['appointment_date']).year
nc_ss_subset.head()


# In[117]:


# Creating a new column with month of date field 'appointment_date'.
nc_ss_subset['month'] = pd.DatetimeIndex(nc_ss_subset['appointment_date']).month
nc_ss_subset.head()


# In[118]:


# Grouping the nc DataFrame by 'service_setting', 'year' and 'month'.
# And aggregating the 'count of appointments' to monthly counts.

nc_ss_subset= pd.DataFrame(nc_ss_subset.groupby(['service_setting','year','month', 'appointment_month', 'appointment_date',]).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
nc_ss_subset.sort_values(['total_monthly_appointments'],ascending=False)

# Create a new nc DataFrame that can be used in future weeks.
nc_ss = nc_ss_subset.sort_values(['total_monthly_appointments'],ascending=False)

# View the output.
nc_ss


# In[119]:


# Aggregate on monthly level and determine the sum of records per month and per service setting.
records_count_nc_ss = nc_ss.groupby(['service_setting'])['appointment_month'].count().reset_index(name='Count')
records_count_nc_ss.sort_values(by=['Count'], ascending=False)


# **Service settings:**

# In[120]:


# Plot the appointments over the available date range, and review the service settings for months.

# Create a lineplot.
total_monthly_appointments_ss = nc_ss['total_monthly_appointments']
sns.lineplot(x='month', y='total_monthly_appointments', hue= 'service_setting', 
             data=nc_ss, ci=None).set_title("Monthly Appointments by Service Setting", fontsize=16)


# **Context types:**

# In[121]:


# Create a subset of the nc DataFrame to look at context type.
# Selecting few columns.

nc_ct_subset = pd.read_excel('national_categories.xlsx', 
                            usecols=['context_type', 'count_of_appointments', 'appointment_date','appointment_month'])

# Print the DataFrame.
nc_ct_subset.head()


# In[122]:


# Extracting the year from string format date.
nc_ct_subset['year'] = pd.DatetimeIndex(nc_ct_subset['appointment_date']).year
nc_ct_subset.head()


# In[123]:


# Creating a new column with month of date field 'appointment_date'.
nc_ct_subset['month'] = pd.DatetimeIndex(nc_ct_subset['appointment_date']).month
nc_ct_subset.head()


# In[124]:


# Aggregate on monthly level and determine the sum of records per month.
# Grouping the nc DataFrame by 'service_setting', 'year' and 'month'.
# And aggregating the 'count of appointments' to monthly counts.

nc_ct_subset= pd.DataFrame(nc_ct_subset.groupby(['context_type','year','month', 'appointment_month', 'appointment_date',]).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
nc_ct_subset.sort_values(['total_monthly_appointments'],ascending=False)

# Create a new nc DataFrame that can be used in future weeks.
nc_ct = nc_ct_subset.sort_values(['total_monthly_appointments'],ascending=False)

# View the output.
nc_ct


# In[125]:


# Plot the appointments over the available date range, and review the context types for months.
# Create a lineplot.
total_monthly_appointments_ct = nc_ct['total_monthly_appointments']
sns.lineplot(x='month', y='total_monthly_appointments', hue= 'context_type', 
             data=nc_ct, ci=0).set_title("Monthly Appointments by Context Type", fontsize=16)


# **National categories:**

# In[126]:


# Create a subset of the nc DataFrame to look at the national categories.
# Selecting few columns.

nc_nc_subset = pd.read_excel('national_categories.xlsx', 
                            usecols=['national_category', 'count_of_appointments', 'appointment_date','appointment_month'])

# Print the DataFrame.
nc_nc_subset.head()


# In[127]:


# Extracting the year from string format date.
nc_nc_subset['year'] = pd.DatetimeIndex(nc_nc_subset['appointment_date']).year
nc_nc_subset.head()


# In[128]:


# Creating a new column with month of date field 'appointment_date'.
nc_nc_subset['month'] = pd.DatetimeIndex(nc_nc_subset['appointment_date']).month
nc_nc_subset.head()


# In[129]:


# Aggregate on monthly level and determine the sum of records per month.
# Grouping the nc DataFrame by 'national_category', 'year' and 'month'.
# And aggregating the 'count of appointments' to monthly counts.

nc_nc_subset= pd.DataFrame(nc_nc_subset.groupby(['national_category','year','month', 'appointment_month', 'appointment_date',]).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
nc_nc_subset.sort_values(['total_monthly_appointments'],ascending=False)

# Create a new nc DataFrame that can be used in future weeks.
nc_nc = nc_nc_subset.sort_values(['total_monthly_appointments'],ascending=False)

# View the output.
nc_nc


# In[131]:


# Plot the appointments over the available date range, and review the national categories for months.
# Create a lineplot.
total_monthly_appointments_nc = nc_nc['total_monthly_appointments']
sns.lineplot(x='month', y='total_monthly_appointments', hue= 'national_category', 
             data=nc_nc, ci=0).set_title("Monthly Appointments by National Category", fontsize=16)


# ### Objective 2
# Create four visualisations indicating the number of appointments for service setting per season. The seasons are summer (August 2021), autumn (October 2021), winter (January 2022), and spring (April 2022).

# **Summer (August 2021):**

# In[132]:


# View the output.
nc_ss
print(nc_ss.dtypes)
nc_ss


# In[139]:


# Look at August 2021 in more detail to allow a closer look.
# Create a lineplot.
summer = nc_ss.query("appointment_month =='2021-08'")
sns.lineplot(data=summer, x="appointment_date", y="total_monthly_appointments", 
             hue='service_setting', errorbar=('ci', 0)).set_title("Summer 2021 - Appointments", fontsize=16)


# **Autumn (October 2021):**

# In[140]:


# Look at October 2021 in more detail to allow a closer look.
# Create a lineplot.
autumn = nc_ss.query("appointment_month =='2021-10'")
sns.lineplot(data=autumn, x="appointment_date", y="total_monthly_appointments", 
             hue= 'service_setting', errorbar=('ci', 0)).set_title("Autumn 2021 - Appointments", fontsize=16)


# **Winter (January 2022):**

# In[142]:


# Look at January 2022 in more detail to allow a closer look.
# Create a lineplot.
winter = nc_ss.query("appointment_month =='2022-01'")
sns.lineplot(data=winter, x="appointment_date", y="total_monthly_appointments", 
             hue='service_setting', errorbar=('ci', 0)).set_title("Winter 2022 - Appointments", fontsize=16)


# **Spring (April 2022):**

# In[143]:


# Look at April 2022 in more detail to allow a closer look.
# Create a lineplot.
spring = nc_ss.query("appointment_month =='2022-04'")
sns.lineplot(data=spring, x="appointment_date", y="total_monthly_appointments", hue='service_setting', 
             errorbar=('ci', 0)).set_title("Spring 2022 - Appointments", fontsize=16)


# # 

# # Assignment activity 5

# ### Analyse tweets from Twitter with hashtags related to healthcare in the UK.

# In[144]:


# Libraries and settings needed for analysis
import pandas as pd
import seaborn as sns

# Set figure size.
sns.set(rc={'figure.figsize':(15, 12)})

# Set the plot style as white.
sns.set_style('white')

# Maximum column width to display
pd.options.display.max_colwidth = 200


# In[145]:


# Load the data set.
tweets = pd.read_csv('tweets.csv')

# View the DataFrame.
tweets.head()


# In[146]:


# Explore the metadata.
print(tweets.columns)
print(tweets.shape)
print(tweets.dtypes)
tweets.info()


# In[147]:


# Determine the descriptive statistics of the tweets data set. Explore the data set.
tweets.describe()


# In[148]:


# Searching for duplicates values in the ar DataFrame.
# No duplicates were found to be duplicated.
tweets.duplicated()


# In[149]:


# De-duplicate the tweets DataFrame using drop_duplicates().
# I decided to remove the 205 raws that were found to be duplicated in the tweets DataFrame.
tweets = tweets.drop_duplicates()
tweets.shape


# **Would it be useful to only look at retweeted and favourite tweet messages? Explain your answer.**
# 
# I think that sorting these two columns by the higuest number of retweets and the most favourite tweets will enable me to identify the most popular tweets by number of retweets and number of times that people marked them as favorites.
# 
# Afterwards, we will be able to look at the full text and hashtags used.

# In[150]:


# Sorting the data by 'tweet_retweet_count' to find the tweets with the highest number of retweets.
tweets.sort_values(by=['tweet_retweet_count'], ascending=False)


# In[151]:


# Sorting the data by 'tweet_favorite_count' to find the tweets that were marked the most as favorite.
tweets.sort_values(by=['tweet_favorite_count'], ascending=False)


# In[152]:


# Create a new DataFrame containing only the text, selecting only 'tweet_full_text'.
tweets_text = pd.read_csv('tweets.csv', 
                            usecols=['tweet_full_text'])

# Print the first 5 raws of the DataFrame.
tweets_text.head()


# In[153]:


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


# In[154]:


# Create a Pandas Series to count the values in the list. Set the Series equal to tags.
tags = pd.Series(top_trending_hashtags)
print(tags)
tags.head(30)


# In[157]:


# Create a Pandas Series to count the values in the list. Set the Series equal to tags.                                 
tags = pd.DataFrame(tweets_text.groupby(['tweet_full_text']).count())

#Display the first 30 records.
tags.head(30)


# In[158]:


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


# In[159]:


# Use the apply() function.
tags_healthcare = tweets_text["tweet_full_text"].apply(contains_healthcare)

# View the DataFrame.
print(tags_healthcare)

# Filter the DataFrame.
tweets_text[tags_healthcare]
tweets_text[tags_healthcare].shape


# #### A total of 842 hashtags contain the word 'healthcare'. Originally there were 961 unique comments in the tweet_full_text column. Therefore, 87.6% of the tweets contain the word 'healthcare.

# In[160]:


# Create a Pandas Series to count the values in the list. Set the Series equal to tags.
tags = pd.Series(top_trending_hashtags)
print(tags)
tags.head()


# In[161]:


# Print the data type.
print(type(tags))


# In[162]:


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


# In[163]:


# Count the number of hashtags per tweet_full_text.
top_trending_hashtags = top_trending_hashtags.groupby(['Word']).count()

top_trending_hashtags.sort_values(['Count'],ascending=False)
top_trending_hashtags = top_trending_hashtags.sort_values(['Count'],ascending=False)

# View the output.
top_trending_hashtags


# In[164]:


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


# In[165]:


# Convert the series to a DataFrame in preparation for visualisation.
# Creating two lists.

import numpy as np

word = [tags]

# Creating two series by passing lists.
word_series = pd.Series(word)

# Creating a dictionary by passing Series objects as values.
frame = {'Word': tags}

# Creating DataFrame by passing Dictionary.
top_trending_hashtags = pd.DataFrame(frame)
 
# Printing elements of Dataframe
print(top_trending_hashtags)


# In[166]:


# Count the number of unique hashtags.
top_trending_unique_hashtags = top_trending_hashtags.groupby(['Word']).value_counts().reset_index(name='Count')
top_trending_unique_hashtags.sort_values(by=['Count'], ascending=False)


# In[167]:


# Ensure the count data type is an integer for data analysis.
print(top_trending_unique_hashtags.dtypes)


# In[168]:


# Display records where the count is larger than 10.
top_trending_unique_hashtags = top_trending_unique_hashtags[top_trending_unique_hashtags['Count'] >10]

# Sort the data by asceinding order.
top_trending_unique_hashtags = top_trending_unique_hashtags.sort_values(['Count'],ascending=False)
top_trending_unique_hashtags


# In[169]:


# Import Matplotlib, Seaborn, and Pandas.
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import *


# In[174]:


# Create a Seaborn barplot indicating records with a count >10 records.
fig, ax = plt.subplots()

sns.barplot(x='Word', y='Count', 
            data=top_trending_unique_hashtags).set_title("Twitter - Top Trending Hashtags", fontsize=16, y=0.92)

x_labels = top_trending_unique_hashtags['Word']

ax.set_xticklabels(x_labels, rotation=90)

plt.show()


# # 

# # Assignment activity 6

# ### Investigate the main cencerns posed by the NHS. 

# In[175]:


# Prepare your workstation.
# Load the appointments_regional.csv file.
ar = pd.read_csv('appointments_regional.csv')

# View the first five rows of the DataFrame.
ar.head(5)


# In[176]:


# Print the min date.
print(ar['appointment_month'].min())
ar.head()


# In[177]:


# Print the min date.
print(ar['appointment_month'].max())
ar.tail()


# In[178]:


# View the data type of the ar DateFrame.
print(ar.dtypes)


# In[179]:


# Change the date format of ar['appointment_month'].
ar['appointment_month'] = pd.to_datetime(ar['appointment_month'])

# View the ar DataFrame and columns to determine the format of the dates.
print(ar.dtypes)


# In[180]:


# Filter the data set to only look at data from 2021-08 onwards.
ar = ar.loc[(ar['appointment_month'] >= '2021-08')]
                    
# View the filtered DataFrame.
ar


# **Question 1:** Should the NHS start looking at increasing staff levels? 

# In[181]:


# Create an aggregated data set to review the different features.
# Determine the total number of appointments per month.

ar_agg = pd.DataFrame(ar.groupby(['appointment_month','hcp_type', 'appointment_status','appointment_mode', 'time_between_book_and_appointment']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
ar_agg.sort_values(['total_monthly_appointments'],ascending=False)

# View the new aggregated DataFrame.
ar_agg


# In[182]:


# Create a new DataFrame (e.g. ar_df) to determine the total number of appointments per month.
ar_df = pd.DataFrame(ar.groupby(['appointment_month']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
ar_df.sort_values(['total_monthly_appointments'],ascending=False)

# View the DataFrame.
ar_df


# In[183]:


# View the data type of the ar DateFrame.
print(ar_df.dtypes)


# In[184]:


# Add a new column to indicate the average utilisation of services.
# Monthly aggregate / 30 to get to a daily value.
ar_ut = ar_df['utilisation'] = ar_df['total_monthly_appointments']/30
ar_ut


# In[185]:


# Rounding the utilisation column.
ar_ut = ar_df[['appointment_month', 'total_monthly_appointments', 'utilisation']].round()
ar_ut


# #### Important to note! The NHS can accommodate a maximum of 1,200,000 appointments per day.

# In[186]:


# View the data type of the ar DateFrame.
print(ar_df.dtypes)

# View the DataFrame.
ar_df


# In[187]:


# Convert the appointment_month to string data type for ease of visualisation.
from datetime import datetime

date_columns = ar_df.select_dtypes(include=['datetime64']).columns.tolist()
ar_df[date_columns] = ar_df[date_columns].astype(str)


# In[188]:


# View the data type of the ar DateFrame.
print(ar_df.dtypes)


# In[189]:


# Plot sum of count of monthly visits.
# Create a lineplot with Seaborn.

sns.lineplot(x='appointment_month', y='total_monthly_appointments', 
             data=ar_df).set_title("Total Appointments by Month", fontsize=16, y=0.92)


# In[190]:


# View the DataFrame.
ar_ut


# In[191]:


# Plot monthly capacity utilisation.

# Create a lineplot.
sns.lineplot(x='appointment_month', y='utilisation', 
             data=ar_ut).set_title("Monthly Capacity Utilisation", fontsize=16, y=0.92)


# **Question 2:** How do the healthcare professional types differ over time?

# In[192]:


# View the new aggregated DataFrame.
ar_agg


# In[193]:


# View the data type of the ar DateFrame.
print(ar_agg.dtypes)


# In[194]:


# Convert the appointment_month to string data type for ease of visualisation.

date_columns = ar_agg.select_dtypes(include=['datetime64']).columns.tolist()
ar_agg[date_columns] = ar_agg[date_columns].astype(str)


# In[195]:


# View the data type of the ar DateFrame.
print(ar_agg.dtypes)


# In[196]:


# Create a line plot to answer the question.

sns.lineplot(x='appointment_month', y='total_monthly_appointments', hue='hcp_type', errorbar=None,
             data=ar_agg).set_title("Healthcare Professional Types Performance Over Time", fontsize=16, y=1)


# **Question 3:** Are there significant changes in whether or not visits are attended?

# In[197]:


# Create a line plot to answer the question.
sns.lineplot(x='appointment_month', y='total_monthly_appointments', hue='appointment_status', errorbar=None,
             data=ar_agg).set_title("Appointments Status Over Time", fontsize=16, y=1)


# **Question 4:** Are there changes in terms of appointment type and the busiest months?

# In[202]:


# Create a line plot to answer the question.
sns.lineplot(x='appointment_month', y='total_monthly_appointments', hue='appointment_mode', errorbar=None,
             data=ar_agg).set_title("Monthly Appointments by Appointment Mode", fontsize=16, y=1)


# **Question 5:** Are there any trends in time between booking an appointment?

# In[204]:


# Create a line plot to answer the question.
sns.lineplot(x='appointment_month', y='total_monthly_appointments', hue='time_between_book_and_appointment', errorbar=None,
             data=ar_agg).set_title("Monthly Appointments by Time Between Booking & Appointment", fontsize=16, y=1)


# **Question 6:** How do the spread of service settings compare?

# In[205]:


# Specify the name of the Excel file.
nc = pd.read_excel('national_categories.xlsx')

# Print the top 5 raws of the nc DataFrame.
nc.head()


# In[206]:


# Let's go back to the national category DataFrame you created in an earlier assignment activity.
# To determine the total number of appointments per month per service setting.
nc_ss = pd.DataFrame(nc.groupby(['appointment_month','service_setting']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
nc_ss.sort_values(['total_monthly_appointments'],ascending=False)

# View the DataFrame.
nc_ss


# In[208]:


# Create a boxplot to investigate spread of service settings.

sns.lineplot(x='appointment_month', y='total_monthly_appointments', hue='service_setting', errorbar=None,
             data=nc_ss).set_title("Monthly Appointments by Spread Of Service Settings Over Time", fontsize=16, y=1)


# In[209]:


# Create a boxplot to investigate the service settings without GP.
nc_ss_without_GP = nc_ss[nc_ss['service_setting'] != 'General Practice']
nc_ss_without_GP


# In[213]:


# Create a boxplot based on the order of variables.
sns.lineplot(x='appointment_month', y='total_monthly_appointments', 
             hue='service_setting', errorbar=None,
             data=nc_ss_without_GP).set_title("Monthly Appointments Spread Of Service Settings Over Time - Without GP", 
                                              fontsize=16, y=1)


# # 

# ### Provide a summary of your findings and recommendations based on the analysis.

# > Double click to insert your summary.

# In[ ]:




