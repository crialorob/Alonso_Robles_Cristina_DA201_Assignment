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

# In[4]:


# Import the necessary libraries.
import pandas as pd
import numpy as np

# Optional - Ignore warnings.
import warnings
warnings.filterwarnings('ignore')


# In[5]:


# Import and sense-check the actual_duration.csv data set as ad.
ad = pd.read_csv('actual_duration.csv')

# View the DataFrame.
ad


# In[12]:


# Determine whether there are missing values.
ad_na = ad[ad.isna().any(axis=1)]
ad_na.shape


# In[27]:


# Determine the sum of missing values in the 'ad' DataFrame.
ad['actual_duration'].isnull().sum()


# There are invalid values in the 'actual_duration' column, identified as'Unknown / Data Quality'.
# 
# Python does not identify them as missing values.

# In[40]:


ad['actual_duration'].isnull().sum()


# In[41]:


# Filter the 'ad' DataFrame according to invalid values.
# There are invalid values in the 'actual_duration' column, identified as'Unknown / Data Quality'.

ad[ad['actual_duration'].str.contains('Unknown / Data Quality')]


# In[24]:


# Determine the metadata of the data set.
print(ad.columns)
print(ad.shape)
print(ad.dtypes)
ad.info()


# In[25]:


# Determine the descriptive statistics of the data set.
ad.describe()


# In[6]:


# Import and sense-check the appointments_regional.csv data set as ar.
ar = pd.read_csv('appointments_regional.csv')

# View the DataFrame.
ar


# In[13]:


# Determine whether there are missing values.
ar_na = ar[ar.isna().any(axis=1)]
ar_na.shape


# In[34]:


# Determine the sum of missing values in the 'ar' DataFrame.
ar['appointments_regional'].isnull().sum()


# There are invalid values in the 'appointment_status' and in the 'hcp_type' columns, identified as 'Unknown'.
# 
# There are also invalid values in the 'time_between_book_and_appointment' column, identified as 'Unknown / Data Quality'.
# 
# Python does not identify them as missing values.

# In[36]:


ar['appointment_status'].isnull().sum()
ar['hcp_type'].isnull().sum()
ar['time_between_book_and_appointment'].isnull().sum()


# In[37]:


# Filter the 'ar' DataFrame according to invalid values 
# This will allow me to better understand the scale of these invalid values.
# There are invalid values in the 'appointment_status' column, identified as 'Unknown'. 

ar[ar['appointment_status'].str.contains("Unknown")]


# In[38]:


# Filter the 'ar' DataFrame according to invalid values.
# There are wrong values in the 'hcp_type' column, identified as 'Unknown'. 

ar[ar['hcp_type'].str.contains("Unknown")]


# In[39]:


# Filter the 'ar' DataFrame according to invalid values.
# There are invalid values in the 'time_between_book_and_appointment' column, identified as 'Unknown / Data Quality'.
ar[ar['time_between_book_and_appointment'].str.contains('Unknown / Data Quality')]


# In[23]:


# Determine the metadata of the data set.
print(ar.columns)
print(ar.shape)
print(ar.dtypes)
ar.info()


# In[26]:


# Determine the descriptive statistics of the data set.
ar.describe()


# In[7]:


# Import and sense-check the national_categories.xlsx data set as nc.
nc = pd.read_excel('national_categories.xlsx')

# View the DataFrame.
nc


# In[14]:


# Determine whether there are missing values.
nc_na = nc[nc.isna().any(axis=1)]
nc_na.shape


# In[35]:


# Determine the sum of missing values in the 'nc' DataFrame.
nc['national_categories'].isnull().sum()


# There are invalid values in the 'service_setting' column, identified as 'Unmapped'.
# 
# There are also invalid values in the 'context_type' and 'national_category' columns, identified as 'Inconsistent Mapping' and 'Unmapped'.
# 
# Python does not identify them as missing values.

# In[44]:


nc['service_setting'].isnull().sum()
nc['context_type'].isnull().sum()
nc['national_category'].isnull().sum()


# In[42]:


# Filter the 'nc' DataFrame according to invalid values.
# There are invalid values in the 'service_setting' column, identified as 'Unmapped'.

nc[nc['service_setting'].str.contains('Unmapped')]


# In[45]:


# Filter the 'nc' DataFrame according to invalid values.
# There are also invalid values in the 'context_type' column, identified as 'Unmapped'.

nc[nc['context_type'].str.contains('Unmapped')]


# In[46]:


# Filter the 'nc' DataFrame according to invalid values.
# There are also invalid values in the 'context_type' column, identified as 'Inconsistent Mapping'.
nc[nc['context_type'].str.contains('Inconsistent Mapping')]


# In[22]:


# Determine the metadata of the data set.
print(nc.columns)
print(nc.shape)
print(nc.dtypes)
nc.info()


# In[21]:


# Determine the descriptive statistics of the data set.
nc.describe()


# ### Explore the data set

# **Question 1:** How many locations are there in the data set?

# In[51]:


# Determine the number of locations.
# Get Unique Count of Locations from the 'ad' DataFrame.
count = ad.sub_icb_location_name.unique().size
print("Count of locations : "+ str(count))


# **Question 2:** What are the five locations with the highest number of records?
# 
# 

# In[54]:


# Sorting the data by 'count_of_appointments' to find the 5 locations with the highest number of records.
nc.sort_values(by=['count_of_appointments'], ascending=False)
nc.head()


# In[57]:


locations_count = nc.groupby(['sub_icb_location_name']).count()
locations_count.head()


# In[58]:


# Determine the top five locations based on record count.
locations_count = pd.DataFrame(nc.groupby(['sub_icb_location_name']).count())
locations_count
locations_count.sort_values(['icb_ons_code'],ascending=False)
top_5_locations = locations_count.sort_values(['icb_ons_code'],ascending=False)
top_5_locations.head()


# **Question 3:** How many service settings, context types, national categories, and appointment statuses are there?

# In[50]:


# Determine the number of service settings.
# Determine the number of service settings from the 'nc' DataFrame.
print(len(nc['service_setting'].unique()))


# In[49]:


# Determine the number of context types from the 'nc' DataFrame.
print(len(nc['context_type'].unique()))


# In[48]:


# Determine the number of national categories from the 'nc' DataFrame.
print(len(nc['national_category'].unique()))


# In[47]:


# Determine the number of appointment statuses from the 'ar' DataFrame.
print(len(ar['appointment_status'].unique()))



# # 

# # Assignment activity 3

# ### Continue to explore the data and search for answers to more specific questions posed by the NHS.

# In[59]:


# Before I move on with the analysis. 
# I would like to search for duplicates values in the ad DataFrame.
# No duplicates were found.
ad.duplicated()


# In[60]:


# Searching for duplicates values in the ar DataFrame.
# 21,604 raws were found to be duplicated.

ar.duplicated()


# In[62]:


# Adding a new column to the ar dataframe that states whether the row is a duplicate.
ar2 = ar.copy()
ar2['duplicated'] = ar2.duplicated()
ar2


# In[66]:


# De-duplicate the data using drop_duplicates().
# I decided to remove the 21,604 raws that were found to be duplicated.
ar = ar.drop_duplicates()
ar.shape


# In[67]:


# The 'ar' DataFrame has now 575,217 rows, containing zero duplicates.

ar.duplicated()


# In[61]:


# Searching for duplicates values in the nc DataFrame.
# No duplicates were found.
nc.duplicated()


# **Question 1:** Between what dates were appointments scheduled?

# In[82]:


# View the ar DataFrame and columns to determine the format of the dates.
print(ar.dtypes)

# View the first five rows of appointment_date for the ad DataFrame to determine the date format.
ar.head()


# In[84]:


# Change the date format of ar['appointment_month'].
ar['appointment_month'] = pd.to_datetime(ar['appointment_month'])

# View the DateFrame.
ar.head()


# In[83]:


# View the ad DataFrame and columns to determine the format of the dates.
# View the first five rows of appointment_date for the nc DataFrame to determine the date format.
ad.head()


# In[75]:


# Change the date format of ad['appointment_date'].
ad['appointment_date'] = pd.to_datetime(ad['appointment_date'])

# View the DateFrame.
ad.head()


# In[85]:


# View the ar DataFrame and columns to determine the format of the dates.
print(ar.dtypes)


# In[86]:


# View the ad DataFrame and columns to determine the format of the dates.
print(ad.dtypes)


# In[87]:


# View the nc DataFrame and columns to determine the format of the dates.
print(nc.dtypes)


# In[89]:


# Change the date format of nc['appointment_month'].
nc['appointment_month'] = pd.to_datetime(nc['appointment_month'])

# View the DateFrame.
nc.head()


# In[90]:


# View the nc DataFrame and columns to determine the format of the dates.
print(nc.dtypes)


# In[95]:


# Determine the minimum and maximum dates in the ad DataFrame.
# Use appropriate docstrings.
# Sort column from low to high to determine. 

print(ad['appointment_month'].sort_values())

# Determine min value (statistical method).
print(ad['appointment_month'].min())
ad.head()


# In[96]:


# Determine the last (e.g. max()) date of scheduled appointments for the ad DataFrame.
# Determine max value (statistical method).
print(ad['appointment_month'].max())
ad.tail()


# In[97]:


# Determine the minimum and maximum dates in the nc DataFrame.
# Use appropriate docstrings.
# Sort column from low to high to determine. 

print(nc['appointment_date'].sort_values())

# Determine min value (statistical method).
print(nc['appointment_date'].min())
nc.head()


# In[98]:


# Determine the last (e.g. max()) date of scheduled appointments for the nc DataFrame.
# Determine max value (statistical method).
print(nc['appointment_date'].max())
nc.tail()


# **Question 2:** Which service setting was the most popular for NHS North West London from 1 January to 1 June 2022?

# In[99]:


# Create a subset of the nc DataFrame.
# Selecting few columns.

nc_subset = pd.read_excel('national_categories.xlsx', 
                            usecols=['sub_icb_location_name', 'service_setting', 'count_of_appointments', 'appointment_date'])

# Print the DataFrame.
nc_subset.head()


# In[100]:


# Use the sub_icb_location code of NHS North West London ICB - W2U3Z.
nc_subset.loc[nc_subset['sub_icb_location_name'].str.contains('NHS North West London ICB - W2U3')]


# In[102]:


# For each of these service settings, determine the number of records available for the period and the location. 

# View the output.


# **Question 3:** Which month had the highest number of appointments?

# Before I can give answers to the following questions, since these questions are not specific to any DataFrame, I assume that these questions refer to the three DataFrames as a whole, so I will merge the three DataFrames.

# To be able to merge the three DataFrames, we should have comparable inputs in terms of 'count of apppointmets', being aggregated to monthly counts.

# In[91]:


# Grouping the ar DataFrame by 'icb_ons_code' and 'appointment_month'.
# And aggregating the 'count of appointments' to monthly counts.

monthly_appointments_count = pd.DataFrame(ar.groupby(['icb_ons_code' ,'appointment_month']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
monthly_appointments_count.sort_values(['total_monthly_appointments'],ascending=False)


# In[92]:


# Grouping the nc DataFrame by 'icb_ons_code' and 'appointment_month'.
# And aggregating the 'count of appointments' to monthly counts.

monthly_appointments_count = pd.DataFrame(nc.groupby(['sub_icb_location_name' ,'appointment_month']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
monthly_appointments_count.sort_values(['total_monthly_appointments'],ascending=False)


# Adding an additional column 'appointment_month' to the ad DataFrame.
# 
# This will allow me to compare the 3 DataFrames by looking at the 'total_monthly_appointments'.

# In[93]:


# Extracting the day/month/year using the to_period function.
# Where 'D', 'M', 'Y' are inputs.
ad['appointment_month'] = pd.to_datetime(ad['appointment_date']).dt.to_period('M')
ad.head()


# In[94]:


# Grouping the ad DataFrame by 'sub_icb_location_name' and 'appointment_month'.
# And aggregating the 'count of appointments' to monthly counts.

monthly_appointments_count = pd.DataFrame(ad.groupby(['sub_icb_location_name' ,'appointment_month']).count_of_appointments.sum().reset_index(name='total_monthly_appointments'))
monthly_appointments_count.sort_values(['total_monthly_appointments'],ascending=False)


# ### Merging the 3 DataFrames.
# 
# # CONTINUE HERE
# 
# # # Merge the nc and the ar DataFrames.
# # nc_ar = pd.merge(nc, ar, how='inner', on = 'icb_ons_code')
# 
# # View the new DataFrame.
# # print(nc_ar.shape)
# # nc_ar.head()
# 

# In[ ]:


# Number of appointments per month == sum of count_of_appointments by month.
# Use the groupby() and sort_values() functions


# **Question 4:** What was the total number of records per month?

# In[ ]:


# Total number of records per month.


# # 

# # Assignment activity 4

# ### Create visualisations and identify possible monthly and seasonal trends in the data.

# In[ ]:


# Import the necessary libraries.
import seaborn as sns
import matplotlib.pyplot as plt

# Set figure size.
sns.set(rc={'figure.figsize':(15, 12)})

# Set the plot style as white.
sns.set_style('white')


# ### Objective 1
# Create three visualisations indicating the number of appointments per month for service settings, context types, and national categories.

# In[ ]:


# Change the data type of the appointment month to string to allow for easier plotting.


# In[ ]:


# Aggregate on monthly level and determine the sum of records per month.


# View output.


# **Service settings:**

# In[ ]:


# Plot the appointments over the available date range, and review the service settings for months.
# Create a lineplot.


# **Context types:**

# In[ ]:


# Create a separate data set that can be used in future weeks. 


# View output.


# In[ ]:


# Plot the appointments over the available date range, and review the context types for months.
# Create a lineplot.


# **National categories:**

# In[ ]:


# Create a separate data set that can be used in future weeks. 


# View output.


# In[ ]:


# Plot the appointments over the available date range, and review the national categories for months.
# Create a lineplot.


# ### Objective 2
# Create four visualisations indicating the number of appointments for service setting per season. The seasons are summer (August 2021), autumn (October 2021), winter (January 2022), and spring (April 2022).

# **Summer (August 2021):**

# In[ ]:


# Create a separate data set that can be used in future weeks. 


# View output.


# In[ ]:


# Look at August 2021 in more detail to allow a closer look.
# Create a lineplot.


# **Autumn (October 2021):**

# In[ ]:


# Look at October 2021 in more detail to allow a closer look.
# Create a lineplot.


# **Winter (January 2022):**

# In[ ]:


# Look at January 2022 in more detail to allow a closer look.
# Create a lineplot.


# **Spring (April 2022):**

# In[ ]:


# Look at April 2022 in more detail to allow a closer look.
# Create a lineplot.


# # 

# # Assignment activity 5

# ### Analyse tweets from Twitter with hashtags related to healthcare in the UK.

# In[ ]:


# Libraries and settings needed for analysis
import pandas as pd
import seaborn as sns

# Set figure size.
sns.set(rc={'figure.figsize':(15, 12)})

# Set the plot style as white.
sns.set_style('white')

# Maximum column width to display
pd.options.display.max_colwidth = 200


# In[ ]:


# Load the data set.


# View the DataFrame.


# In[ ]:


# Explore the metadata.


# In[ ]:


# Explore the data set.


# In[ ]:


# Would it be useful to only look at retweeted and favourite tweet messages?
# Explain your answer.


# In[ ]:


# Create a new DataFrame containing only the text.


# View the DataFrame.


# In[ ]:


# Loop through the messages, and create a list of values containing the # symbol.


# In[ ]:


# Display the first 30 records.


# In[ ]:


# Convert the series to a DataFrame in preparation for visualisation.


# Rename the columns.


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




