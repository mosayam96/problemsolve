#!/usr/bin/env python
# coding: utf-8

# In[23]:


ans = 0

def max_pairwise_product(n,a):
    for i in range(0,n):
        for j in range(i+1,n):
            if a[i]*a[j] > ans:
                ans = a[i]*a[j]
                
                
def max_pairwise_product_fast(n,b):
    ind1 = -1
    for i in range(n):
        if ind1 == -1 or b[i]>b[ind1]:
            ind1 = i
    ind2 = -1
    for j in range(n):
        if j != ind1 and (ind2 == -1 or b[j] > b[ind2]):
            ind2 = j
    
    return b[ind1]*b[ind2]

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(len(a)==n)
    
    print(max_pairwise_product_fast(n,a))

