#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for _ in range(int(input())):
    n, m = map(int, input().split())
    print("Burenka" if (n+m)%2 !=0 else "Tonya")

