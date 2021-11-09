#!/usr/bin/env python
# coding: utf-8

# In[30]:


# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10



def fibonacci_sum_fast(n):
    if n <= 1:
        return n
    sum_n_1 = (n+2)%60   #pisano_repeat(10) = 60 and sum of first n th fibonacci= n+2 th fibonacci number - 1

    previous = 0
    current  = 1

    for _ in range(sum_n_1-1):
        previous, current = current, (previous + current)%10
    if current == 0:
        return 9
    else:
        return current-1

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))



# In[ ]:




