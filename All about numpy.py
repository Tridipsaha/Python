#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


np.absolute(-5)
a=np.array([1,4,6,2,9])#convert into array
a.shape #gives the shape or size of the list variable



# In[4]:


b=np.array([[1,7,5],[6,1,3]])# creating 2D array
print(b.T)#transpose the array
np.dot(b,b.T)# dot product between two matri


# In[5]:


array= np.random.randint(3,9,(9))#give you random number(start,end,size)
array
type(array)
matrix=np.random.randint(2,9,(4,4))
matrix


# In[6]:


np.max(matrix)#only highest matrix index value give
np.min(array)

s= np.array([0,1,4,2,1])
np.argmax(s)# give the highest index value 


# In[7]:


np.unique(s)#remove the similar number and arrnage in assending order
np.unique(s,return_counts=True)#??


# In[8]:


matrix[0:3,1:4]


# In[27]:


a=np.random.randint(4,9,(9))
print(a)

Sum=sum(a)
print("Sum of a=",Sum)

Minimum=min(a)
print("Minimum of a=",Minimum)

Maximum = max(a)
print("Maximum of a=",Maximum)

Absolute= abs(a[0]-a[1])
print("Absolute value of ",a[0],"-",a[1], "=",Absolute)

Mean=np.mean(a)
print("Mean of a=",Mean)

Standard=np.std(a)
print("Standard of a=",Standard)

Product= np.prod(a)
print("Product of a=",Product)

