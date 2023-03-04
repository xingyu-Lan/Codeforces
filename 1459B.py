#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())

if n % 2 == 0:
    print ((n//2 + 1)**2)
else:
    print (2 *(n//2+1)*(n//2+2))

