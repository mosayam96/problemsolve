#!/usr/bin/env python
# coding: utf-8

# In[10]:



import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def pattern_count(m):
    p = 0
    c = 1
    for i in range(m*m+1):
        p,c = c,(p+c)%m
        if p == 0 and c== 1:
            return i+1
def calc_fib(n):
    if n<=1 :
        return n
    i = 0
    j = 1
    
    for _ in range(n-1):
        i,j = j,i+j
    
    return j

def get_fibonacci_fast_huge(n,m):
    frac = n%pattern_count(m)
    return calc_fib(frac)%m


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_fast_huge(n, m))


# In[ ]:




