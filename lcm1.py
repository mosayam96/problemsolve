#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_fast(a,b):
    n = a*b
    assert a>=0 and b>=0 
    while a>0 and b>0 :
        if a>=b:
            a = a%b 
        else:
            b = b%a
    return n//max(a,b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

