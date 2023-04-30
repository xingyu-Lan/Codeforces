#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for _ in range(int(input())):
  n=int(input())
  input()
  print(3*n)
  for i in range(1,n,2):
    for j in [1,2,1,1,2,1]:
      print(j,i,i+1)

