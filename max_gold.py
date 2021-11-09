#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sys
def optimised(W,w,n):
    T = [[0 for i in range(W+1)] for j in range(n+1)]
    for j in range(1,n+1):
        for i in range(1,W+1):
            T[j][i] = T[j-1][i]
            if w[j-1] <= i :
                value = T[j-1][i-w[j-1]] + w[j-1]
                if value > T[j][i] and value<=i:
                    T[j][i] = value
    return T[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimised(W, w, n))


# In[ ]:




