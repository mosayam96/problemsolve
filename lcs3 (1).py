#!/usr/bin/env python
# coding: utf-8

# In[45]:


import sys
def lcs2(a,b):
    T = [[float('inf')]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)+1):
        T[i][0] = 0
    for j in range(len(b)+1):
        T[0][j] = 0
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1] == b[j-1]:
                T[i][j] = T[i-1][j-1]+1
            else:
                T[i][j] = max(T[i-1][j],T[i][j-1])
    return T[len(a)][len(b)]

def lcs3(a,b,c):
    m = len(a)
    n = len(b)
    o = len(c)
    T = [[[float('inf') ] * (o + 1) for _ in range(n + 1)] for _ in range (m+1)]
    for i in range(m + 1):
        for j in range(n+1):
            for k in range(o+1):
                if i == 0 or j == 0 or k==0:
                    T[i][j][k] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                if a[i - 1] == b[j - 1] and a[i - 1] == c[k - 1]:
                    T[i][j][k] = T[i - 1][j - 1][k - 1] + 1
                else:
                    T[i][j][k] = max(T[i-1][j][k], T[i][j - 1][k], T[i][j][k - 1], T[i - 1][j - 1][k], T[i - 1][j][k - 1], T[i][j - 1][k - 1])
    return T[m][n][o]
            
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))


# In[ ]:




