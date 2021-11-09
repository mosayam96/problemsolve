#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_euclide(a,b):
    assert a>=0 and b>=0 and a+b>=0
    while a>0 and b>0:
        if a>=b:
            a = a%b
        else:
            b= b%a
    return max(a,b)
    

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclide(a, b))


# In[ ]:




