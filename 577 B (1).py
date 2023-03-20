#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n, m = map (int,input().split())
a = list(map(int,input().split()))

d = set()
for i in a:
    w = { (i + y) % m for y in d}
    d |= w
    d.add(i%m)
    if 0 in d:
        print("YES")
        exit()
print("NO")

