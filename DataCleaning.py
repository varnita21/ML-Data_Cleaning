
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


df= pd.read_csv("breast-cancer.csv",encoding="utf8")


# In[6]:


df.head()


# In[7]:


df.columns = df.columns.str.upper()


# In[8]:


df.columns


# In[9]:


df.head()


# In[10]:


df.isnull()


# In[11]:


df.isnull().any()


# In[12]:


df.isnull().any().any()


# In[13]:


df.isnull().sum()


# In[14]:


df.isnull().sum().sum()


# In[17]:


df_with_0 = df.fillna(0)


# In[18]:


df_with_0.head()

