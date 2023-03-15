#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    if a[0]!=0:
        ways = 2
    else:
        ways = 1
    for i in range(n-1):
        if a[i]<(i+1) and a[i+1]>=(i+2):
            ways += 1
    print(ways)


# Let's fix the number of people going to the cinema 𝑘 and try to choose a set of this exact size. What happens to people with different 𝑎𝑖?
# 
# If 𝑎𝑖<𝑘, person 𝑖 definitely wants to go.
# If 𝑎𝑖>𝑘, person 𝑖 definitely does not want to go.
# If 𝑎𝑖=𝑘, there is actually no good outcome for person 𝑖. If person 𝑖 goes to the cinema, there are only 𝑘−1 other people going, so person 𝑖 will be sad (since 𝑘−1<𝑎𝑖). If person 𝑖 does not go, there are 𝑘 other people going, so person 𝑖 will be sad too (since 𝑘≥𝑎𝑖).
# 
# Thus, for a set of size 𝑘 to exist, there must be no people with 𝑎𝑖=𝑘, and the number of people with 𝑎𝑖<𝑘 must be exactly 𝑘. We can easily check these conditions if we use an auxiliary array cnt such that cnt[x] is equal to the number of people with 𝑎𝑖=𝑥.
# 
# Alternative solution:
# 
# Notice that if a set of 𝑘 people can go to the cinema, it must always be a set of people with the smallest 𝑎𝑖. Thus, we can start with sorting the array 𝑎 in non-decreasing order.
# 
# Then, for each length 𝑘 of a prefix of this array, we can check whether the first 𝑘 elements are all smaller than 𝑘, and the remaining 𝑛−𝑘 elements are all greater than 𝑘.
# 
# However, since the array is sorted, it is enough to check that the 𝑘-th element is smaller than 𝑘, and the 𝑘+1-th element is greater than 𝑘.
