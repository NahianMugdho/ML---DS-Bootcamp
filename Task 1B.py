#!/usr/bin/env python
# coding: utf-8

# # Read the wine.csv dataset as Pandas DataFrame and show (in another notebook):
# - head()
# - Show the entry of the 7th row, the last column.
# - Save the 1st 10 rows as a Pickle file.

# In[7]:


import pandas as pd
wine = pd.read_csv("F:\ml\ML-DS-Bootcamp\ML-DS-Bootcamp\Course 1. Python for Data Science & Machine Learning\datasets\wine.csv")
wine.head(10)


# Show the entry of the 7th row, the last column.

# In[20]:


wine.iloc[6,-1]


# Save the 1st 10 rows as a Pickle file

# In[23]:


wine.head(10).to_pickle("F:\ml\ML-DS-Bootcamp\ML-DS-Bootcamp\Course 1. Python for Data Science & Machine Learning\datasets\winep")


# In[24]:


wine_p=pd.read_pickle("F:\ml\ML-DS-Bootcamp\ML-DS-Bootcamp\Course 1. Python for Data Science & Machine Learning\datasets\winep")


# In[29]:


wine_p.head(10)


# In[ ]:




