#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys

def get_change(m):
    #write your code here
    n = 0
    n = m//10
    k = m%10
    i = k//5
    j = k%5
    return n+i+j

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))


# In[ ]:




