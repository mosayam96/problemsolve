#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
c = (1,3,4)
def get_change(m,c):
    #write your code here
    mincon = [float('inf')]*(m+1)
    mincon[0] = 0
    for i in range(1,m+1):
        for f in c:
            if i>=f:
                numcon = mincon[i-f]+1
                if numcon < mincon[i]:
                    mincon[i] = numcon
    return mincon[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m,c))


# In[ ]:




