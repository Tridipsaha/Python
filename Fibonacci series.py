#!/usr/bin/env python
# coding: utf-8

# In[6]:


num1,num2=0,1
num = input("Enter the number of series: ")
num = int(num)
fib=0
for i in range(num+1):
    print(num1,end=" ")
    fib=num1+num2
    num1=num2
    num2=fib


# In[ ]:




