#!/usr/bin/env python
# coding: utf-8

# In[11]:


import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10

def fibonacci_last_digit(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n-1):
        previous,current = current, (previous+current)%10
    return current

def fibonacci_partial_sum_fast(m,n):
    sum_n_1 = (n+2)%60   #pisano_repeat(10) = 60 and sum of first n th fibonacci= n+2 th fibonacci number - 1
    div_m_1 = (m+1)%60
    last_digit_n_1 = fibonacci_last_digit(sum_n_1)
    last_digit_m_1 = fibonacci_last_digit(div_m_1)
    if last_digit_n_1 >= last_digit_m_1 :
        return last_digit_n_1 - last_digit_m_1
    else:
        return last_digit_n_1 + 10 - last_digit_m_1

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))


# In[ ]:




