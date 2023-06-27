#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
data={ 'Name': ['jai', 'Tridip', 'Akash', ' Aman'],
       'Age' : [12, 14, 13, 20,],
       'Gender': ['M', 'M', 'F', 'M'],
       'Marks': [ 76, 'NaN', 'NaN', 71] }

dataSet= pd.DataFrame(data)

dataSet


# In[47]:


c = avg = 0
for ele in dataSet['Marks']:
    if str(ele).isnumeric():
        c+=1
        avg+= ele
avg/=c
dataSet= dataSet.replace(to_replace= "NaN", value=avg)
dataSet


# In[48]:


dataSet['Gender']= dataSet['Gender'].map({'M':0, 'F':1,}).astype('int')
dataSet


# In[43]:


dataSet = dataSet[dataSet['Marks'] >= 70].copy()
dataSet


# In[49]:


details = pd.DataFrame({
    'ID': [101, 102, 103, 104],
    'NAME': ['Jagroop', 'Praveen', 'Harjot','Pooja'],
    'BRANCH': ['CSE', 'CSE', 'CSE', 'CSE']})

print(details)


# In[50]:


fees_status = pd.DataFrame({
    'ID': [101, 102, 103, 104],
    'PENDING': ['5000', '250', 'NIL','9000']})

print(fees_status)


# In[51]:


print(pd.merge(details,fees_status, on='ID'))


# In[55]:


car_selling_data = {'Brand': ['Maruti', 'Maruti', 'Maruti',
                            'Maruti', 'Hyundai', 'Hyundai',
                            'Toyota', 'Mahindra', 'Mahindra',
                            'Ford', 'Toyota', 'Ford'],
                    'Year': [2010, 2011, 2009, 2013,
                            2010, 2011, 2011, 2010,
                            2013, 2010, 2010, 2011],
                    'Sold': [6, 7, 9, 8, 3, 5,
                            2, 8, 7, 2, 4, 2]}


dataSet = pd.DataFrame(car_selling_data) 
grouped = dataSet.groupby('Year')
print(grouped.get_group(2010))


# In[56]:


non_duplicate = dataSet[~dataSet.duplicated('Year')] 
print(non_duplicate)


# In[ ]:




