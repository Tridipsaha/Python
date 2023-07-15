#!/usr/bin/env python
# coding: utf-8

# In[1]:


grid =[
    [7,0,0,0,4,1,0,0,2],
    [8,0,0,0,0,2,5,0,0],
    [2,0,6,5,0,7,1,0,0],
    [0,0,8,2,0,0,0,0,3],
    [0,0,0,3,0,9,0,0,0],
    [1,0,0,0,0,4,2,0,0],
    [0,0,7,4,0,5,9,0,6],
    [0,0,4,0,0,0,0,0,1],
    [9,0,0,1,6,0,0,0,7]
]


# In[2]:


from tabulate import tabulate
import numpy as np




def disp():
    custom_table_format = """
-------------------------
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
-------------------------
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
-------------------------
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
"""
    formatted_data = [[str(value) for value in row] for row in grid]
    table = custom_table_format.format(*[cell for row in formatted_data for cell in row])
    print(table)





def possible(row, col, number):
    global grid
    
    #row cheking
    for i in range(9):
        if grid[row][i] == number:
            return False
    #colum checking
    for i in range(9):
        if grid[i][col] == number:
            return False
    x = (col//3)*3
    y = (row//3)*3
    for i in range(3):
        for j in range(3):
            if grid[y+i][x+j] == number:
                return False
            
    return True

def solve():
    global grid
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row,column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                        
                return
            
    disp()
    
    


# In[3]:


solve()


# In[ ]:




