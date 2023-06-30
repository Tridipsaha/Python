#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
numbers=np.random.randint(30,500,(9))

print("List of numbers: ",numbers)
print("List of divisible by 5: ",end="")
for i in numbers:
    if(i%2==0):
        print(i,end=" ")

