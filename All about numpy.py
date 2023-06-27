#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


np.absolute(-5)
a=np.array([1,4,6,2,9])#convert into array
a.shape #gives the shape or size of the list variable



# In[3]:


b=np.array([[1,7,5],[6,1,3]])# creating 2D array
print(b.T)#transpose the array
np.dot(b,b.T)# dot product between two matri


# In[10]:


array= np.random.randint(3,9,(9))#give you random number(start,end,size)
array
type(array)
matrix=np.random.randint(2,9,(4,4))
matrix


# In[21]:


np.max(matrix)#only highest matrix index value give
np.min(array)

s= np.array([0,1,4,2,1])
np.argmax(s)# give the highest index value 


# In[24]:


np.unique(s)#remove the similar number and arrnage in assending order
np.unique(s,return_counts=True)#??


# In[27]:


matrix[0:3,1:4]

