#!/usr/bin/env python
# coding: utf-8

# In[36]:


import sys
def majority_naive(a):
    for i in range(len(a)):
        current_element = a[i]
        count = 0 
        for j in range(len(a)):
            if current_element == a[j]:
                count = count+1
            if count>len(a)/2:
                return 0
    return -1

def majority(a,l,m):
    if l == m:
        return -1
    if l+1 == m:
        return a[l]
    left = majority(a,l,(l+m-1)//2+1)
    right = majority(a,(l+m-1)//2+1,m)
    lcount = 0
    rcount = 0
    for i in range(l,m):
        if a[i] == left:
            lcount = lcount+1
    if lcount > (m-l)//2:
        return left
    for i in range(l,m):
        if a[i] == right:
            rcount = rcount+1
    if rcount > (m-l)//2:
        return right
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if majority(a, 0, n) != -1:
        print(1)
    else:
        print(0)


# In[ ]:




