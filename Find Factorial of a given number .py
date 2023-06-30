#!/usr/bin/env python
# coding: utf-8

# In[4]:


num = input("Enter the factorial number: ")
num = int(num)
fac=1
for i in range(num,0,-1):
    fac*=i
print(num,"!=",fac)


# In[ ]:




