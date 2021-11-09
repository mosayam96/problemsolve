#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


def compute_min_refills(distance, tank, stops):
    if distance<tank:
        return 0
    curr_fuel = tank
    cur_distance = 0
    num_stops = 0
    stops.append(distance)
    stops.insert(0,0)
    for i in range(len(stops)-1):
        if (stops[i+1] - stops[i]) > tank:
            return -1
        elif (stops[i+1] - stops[i]) > curr_fuel:
            num_stops+=1
            curr_fuel = tank
            curr_fuel-=(stops[i+1] - stops[i])
        else:
            curr_fuel-=(stops[i+1] - stops[i])
    return num_stops

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))


# In[ ]:




