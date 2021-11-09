#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)
def sequences(n):
    seq = [0]*(n+1)
    path = [0]*(n+1)
    k = 2
    while k<=n:
        m1 = seq[k-1]+1
        if k%2==0:
            m2 = seq[int(k/2)]+1
        else:
            m2 = n
        if k%3== 0:
            m3 = seq[int(k/3)]+1
        else: 
            m3 = n
        minimum = min(m1,m2,m3)
        
        if minimum == m1:
            seq[k] = m1
            path[k] = 1
        elif minimum == m2:
            seq[k] = m2
            path[k] = 2
        else:
            seq[k] = m3
            path[k] = 3
        k = k+1
        
    l = n
    track = [n]
    while l>1:
        if path[l] == 3:
            l = int(l/3)
            track.append(l)
        elif path[l] ==2:
            l = int(l/2)
            track.append(l)
        else:
            l = l - 1
            track.append(l)
    return seq,reversed(track)
        
input = sys.stdin.read()
n = int(input)
sequence = [1]
sequence, track = sequences(n)
print(sequence[-1])
for a in track:
    print(a, end=' ')


# In[ ]:




