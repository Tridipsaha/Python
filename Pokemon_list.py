#!/usr/bin/env python
# coding: utf-8

# In[3]:


print(type(number_list))


# In[ ]:


number_list=number_list.split()
number_list


# In[ ]:


number_list_int=[int(i) for i in number_list]
number_list_int


# In[ ]:





# In[5]:


pokemon_map = {
    1 : "bulbasaur",
    2 : "charmender",
    3 : "pikachu"
}

number_list=input()
print(number_list)


# In[6]:


number_list = number_list.split()
number_list


# In[7]:


number_list_int = [int(i) for i in number_list]
print(number_list_int)


# In[10]:


for i in number_list_int:
    if pokemon_map.get(i) is None:
        print('Pokemon not found!')
    else: 
        print(pokemon_map.get(i))


# In[ ]:




