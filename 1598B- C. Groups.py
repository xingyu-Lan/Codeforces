#!/usr/bin/env python
# coding: utf-8

# In[ ]:


t = int(input())
for i in range(t):
    n = int(input())
    a = [[] for i in range(n)]
    for j in range(n):
        a[j] = list(map(int, input().split()))
    ans = False
    for j in range(5):
        for k in range(5):
            if k != j:
                cnt1 = 0
                cnt2 = 0
                cntno = 0
                for z in range(n):
                    if a[z][j] == 1:
                        cnt1 += 1
                    if a[z][k] == 1:
                        cnt2 += 1
                    if a[z][j] == 0 and a[z][k] == 0:
                        cntno += 1
                if cnt1 >= n // 2 and cnt2 >= n // 2 and cntno == 0:
                    ans = True
    if ans:
        print('YES')
    else:
        print('NO')
                


# Since there are only five days, we can iterate over the two of them that will be the answer.
# 
# Now we have fixed a pair of days 𝑎 and 𝑏 and want to check if it can be the answer.
# 
# All students can be divided into four groups: marked neither of days 𝑎 and 𝑏, marked only day 𝑎, marked only day 𝑏
# and marked both days.
# 
# Obviously, if the first group is non-empty, days 𝑎 and 𝑏 can't be the answer.
# 
# Let's call the number of students, who only marked day 𝑎, cnt𝑎 and the number of students, who only marked day 𝑏, cnt𝑏.
# 
# If either of cnt𝑎 or cnt𝑏 exceed 𝑛/2, then days 𝑎 and 𝑏 can't be the answer as well. Otherwise, we can always choose 𝑛2−cnt𝑎 students from the ones who marked both days and send them to day 𝑎. The rest of the students can go to day 𝑏.
