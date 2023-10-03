#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the required modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


# import the dataset
df = pd.read_csv("FoodBalanceSheets_E_Africa_NOFLAG.csv", encoding='latin-1' )


# In[15]:


# print the first five records
df.head()


# In[16]:


# check the shape of the dataset
df.shape


# In[17]:


# 2: What is the total Protein supply quantity in Madagascar in 2015?
df.groupby(["Item"])["Y2015"].sum()


# In[18]:


# 6: What is the total number of the sum of Processing in 2017?
df.groupby(['Element'])['Y2017'].sum()


# In[19]:


# 7: What year has the highest sum of Stock Variation?
df.groupby(['Element']).sum()


# In[20]:


# 8: What is the total sum of Wine produced in 2015 and 2018 respectively?
df.groupby(['Item']).sum()


# In[21]:


#  Which of these Areas had the 7th lowest sum in 2017?
df.groupby(['Area'])['Y2017'].sum()


# In[22]:


# What is the total number and percentage of missing data in 2014 to 3 decimal places?
result = df["Y2014"].isnull().sum() * 100 / len(df)
print(round(result, 3))


# In[23]:


# Which of these Areas had the highest sum in 2017?
df.groupby(['Area'])['Y2017'].sum()


# In[34]:


# 20: What is the mean and standard deviation across the whole dataset for the year 2017 to 2 decimal places?
df.describe()['Y2017'].sum()
print(round(result, 2))


# In[39]:


get_ipython().run_line_magic('pinfo', 'dataset')
df.groupby(['Area']).sum()


# In[ ]:




