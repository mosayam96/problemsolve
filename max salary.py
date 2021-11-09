#!/usr/bin/env python
# coding: utf-8

# In[16]:


import sys

def isequal(digit,max_digit):
    return int(digit+max_digit)>= int(max_digit+digit)

def largest_number(digit):
    answer = []
    while digit:
        max_digit = '0'
        for i in digit:
            if isequal(i,max_digit):
                max_digit = i
        answer.append(max_digit)
        digit.remove(max_digit)
    dig = ''
    for i in answer:
        dig = dig + i
    return dig

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))


# In[ ]:




