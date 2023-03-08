#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for i in range(int(input())):
    n=int(input())
    if n%2==1:
        print("7 "*n)
    else:
        print('2 '*(n-2)+'3 1')

