#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys

def Binarysearch(A,low,high,key):
    if high<low:
        return low-1
    mid = low+(high-low)//2
    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return Binarysearch(A,low,mid-1,key)
    elif key > A[mid]:
        return Binarysearch(A,mid+1,high,key)
    
def BinarysearchIT(A,key):
    low,high = 0,len(A)-1
    while low<=high:
        mid = low+(high-low)//2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(BinarysearchIT(input_keys, q), end=' ')


# 
