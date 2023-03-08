#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for _ in range(int(input())):
    n,l,r,k=map(int,input().split())
    a=sorted(list(map(int,input().split())))
    p=0
    for i in range(n):
        if a[i]>=l and a[i]<=r and k-a[i]>=0:
            p+=1
            k-=a[i]
    print(p)

