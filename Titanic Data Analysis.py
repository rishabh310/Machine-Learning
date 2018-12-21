
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

titanic_data= pd.read_csv("train_data.csv")


# In[33]:


titanic_data.head(10)


# In[16]:


print("Number of passengers in original data:" +str(len(titanic_data)))


# ## Analyzing Data

# In[17]:


sns.countplot(x="Survived", data=titanic_data)


# In[18]:


sns.countplot(x="Survived", hue="Sex", data=titanic_data)


# In[41]:


titanic_data["Age"].plot.hist()


# In[42]:


titanic_data["Fare"].plot.hist()


# In[43]:


titanic_data.info()


# ## Data Cleaning

# In[44]:


titanic_data.isnull()

