#!/usr/bin/env python
# coding: utf-8

# In[ ]:


input()
a=[0,0]
for x in input().split():
    a[int(x)-1]+=1
c=min(a)
print(c+(a[0]-c)//3)

