#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for _ in range(int(input())):
    n,h,m=map(int,input().split())
    z=min(((x-h)*60+y-m)%1440 
          for x,y in [map(int,input().split()) for i in range(n)])
    print(z//60,z%60)


# In[ ]:




