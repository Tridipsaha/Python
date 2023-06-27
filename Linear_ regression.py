#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import seaborn as sns
from sklearn import linear_model
df = pd.read_csv('salary.csv')
df


# In[5]:


sns.lmplot(x='Age',y='Salary', data=df)


# In[6]:


reg = linear_model.LinearRegression()
reg.fit(df[['Age']],df[['Salary']])


# In[7]:


reg.predict([[45]])


# In[8]:


reg.coef_


# In[9]:


reg.intercept_


# In[ ]:




