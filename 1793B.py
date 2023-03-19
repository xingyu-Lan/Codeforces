#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for _ in range(int(input())):
    x, y = map(int, input().split())
 
    a = list(range(y, x+1))
    a += a[-2:0:-1]
    print(len(a))
    print(*a)

