#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solve():
    n, m = [int(i) for i in input().split()]
    cnt2, cnt5 = 0,0 
    n1 = n 
    res = 1 
    while n1%2 == 0:
        n1 = n1//2
        cnt2 += 1
    while n1%5 == 0:
        n1 = n1//5
        cnt5 += 1
    if cnt5 < cnt2:
        while res * 5 <= m:
            cnt5 += 1 
            res *= 5
            if cnt2 == cnt5: break 
    if cnt2 < cnt5:
        while res * 2 <= m:
            cnt2 += 1
            res *= 2
            if cnt2 == cnt5: break 
    if cnt2 == cnt5:
        while res * 10 <= m:
            res *= 10
    if res == 1:
        return n * m 
    else:
        res *= (m//res)
        return n * res
    
 
t = int(input())
while t:
  t -= 1
  print(solve())
  

