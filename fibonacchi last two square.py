#!/usr/bin/env python
# coding: utf-8

# In[7]:


from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_last_digit(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n-1):
        previous,current = current, (previous+current)%10
    return current

def fibonacci_sum_squares_fast(n):
    n1 = n%30
    multi = fibonacci_last_digit(n1*2)
    t = (fibonacci_last_digit(n1)*fibonacci_last_digit((n1-1)))%10
    if multi>=t:
        return multi - t
    else:
        return multi+10-t
    
if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_fast(n))


# In[ ]:




