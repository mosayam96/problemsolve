#!/usr/bin/env python
# coding: utf-8

# In[3]:


def calc_fib(n):
    if n<=1 :
        return n
    i = 0
    j = 1
    
    for _ in range(2,n+1):
        i,j = j,i+j
    
    return j

n = int(input())
print(calc_fib(n))


# In[ ]:




