#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for _ in range(int(input())):
    x = int(input())
    n = input()
    if n[0] == '9':
        print (int('1' * (x+1))-int(n))
    else:
        print (int('9'*x)-int(n))


# In[ ]:




