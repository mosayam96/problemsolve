#!/usr/bin/env python
# coding: utf-8

# In[65]:


import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    value_weight_ratio,dic = value_weight(values,weights)
    for i in range(n):
        if capacity == 0:
            return value
        weight_available = min(capacity,dic[value_weight_ratio[i]])
        value = value + weight_available*value_weight_ratio[i]
        capacity = capacity - weight_available
    return value


def value_weight(values,weights):
    value_weight = []
    dic = {}
    for i in range(n):
        value_weight.append(values[i]/weights[i])
        dic[values[i]/weights[i]] = weights[i]
    value_weight.sort(reverse=True)
    return value_weight,dic

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


# In[ ]:




