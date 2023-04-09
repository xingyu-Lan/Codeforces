#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for it in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    for i in range(n-1):
        if b[i]==a[i]:
            b[i],b[i+1]=b[i+1],b[i]
    if n==1:
        b=[-1]
    elif b[-1]==a[-1]:
        b[-1],b[-2]=b[-2],b[-1]
    print(*b)


# The exception is the last two elements. We can always take the smallest available number for each 𝑞𝑖
#  satisfying 𝑖<𝑛−1
# . To do this we maintain an array of bools of already taken numbers, and then iterate over it to find the smallest available number satisfying 𝑝𝑖≠𝑞𝑖
#  which is also not checked in the array, and then check it (we took it).
# 
# Now consider (𝑝𝑛−1,𝑝𝑛)
#  and we want (𝑞𝑛−1,𝑞𝑛)
#  to be lexicographically minimal while satisfying 𝑝𝑛−1≠𝑞𝑛−1
#  and 𝑝𝑛≠𝑞𝑛
# . Let 𝑎
#  and 𝑏
#  be the last two unused numbers in the array of bools with 𝑎<𝑏
# . We try to take (𝑞𝑛−1,𝑞𝑛)=(𝑎,𝑏)
# . If 𝑎=𝑝𝑛−1
#  or 𝑏=𝑝𝑛
# , then we take (𝑞𝑛−1,𝑞𝑛)=(𝑏,𝑎)
# . If (𝑎,𝑏)
#  isn't valid, then (𝑏,𝑎)
#  is. The proof is left as an exercise to the reader.
# 
# This solution runs in 𝑂(𝑛2)
#  and can be optimized to 𝑂(𝑛 𝑙𝑜𝑔 𝑛)
# .
