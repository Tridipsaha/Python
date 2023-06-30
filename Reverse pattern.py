#!/usr/bin/env python
# coding: utf-8

# In[5]:


j=1
for i in range(5,0,-1):
    while i>=j:
        print(i,end=" ")
        i-=1
    print("")

