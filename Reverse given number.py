#!/usr/bin/env python
# coding: utf-8

# In[14]:


num = int(input("Enter the number: "))
rever=0
reminder=0
while num!=0:
    reminder=num%10
    rever= (rever*10)+reminder
    num=num//10
print(rever)


# In[ ]:




