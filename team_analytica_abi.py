#!/usr/bin/env python
# coding: utf-8

# # House Prices- Advanced Regression Techniques

# ### Executive Summary
# 
# Housing Experts and eceonomists are predicting that housing prices will continue to rise in 2022. This dataset summarizes that information.

# ### Import Packages

# In[7]:


import pandas as pd
import seaborn as sb
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# ### Loading train dataset

# In[21]:


train = pd.read_csv ('C:/Users/abiak/Documents/GitHub/team_analytica/train.csv')
train


# ### Loading test dataset

# In[22]:


test = pd.read_csv ('C:/Users/abiak/Documents/GitHub/team_analytica/test.csv')
test


# In[18]:


train.columns


# In[19]:


train.shape


# In[20]:


train.describe()


# In[23]:


test.columns


# In[24]:


test.shape


# In[25]:


test.describe()


# In[ ]:




