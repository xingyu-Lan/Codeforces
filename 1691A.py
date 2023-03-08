#!/usr/bin/env python
# coding: utf-8

# In[1]:


for s in[*open(0)][2::2]:
    a=[0,0]
    for i in s.split():a[int(i)%2]+=1
    print(min(a))

