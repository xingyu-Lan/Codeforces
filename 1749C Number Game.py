#!/usr/bin/env python
# coding: utf-8

# Note that if Bob has increased some element, then Alice can't remove it on the next stages. Obviously, it is more profitable for Bob to "prohibit" the smallest element of the array. Using this fact, we can iterate over the value of 𝑘, and then simulate the game process. To simulate the game, we can maintain the set of elements that Alice can remove. On the 𝑖-th stage, Alice removes the maximum element 𝑥, such that 𝑥≤𝑘−𝑖+1, if there are no such elements, then Alice lost. Bob always removes the minimum element of the set.
# 
# Thus, the complexity of the solution is 𝑂(𝑛2log𝑛)for each test case.
# 
# There is another possible solution: we can notice that, if Alice wins, Bob will "prohibit" the elements on positions 1,2,…,𝑘−1 of the sorted array. So, Alice has to delete the next 𝑘elements. So, if the segment [𝑘…2𝑘−1]of the sorted array can be deleted by Alice during the game phases, she wins with this value of 𝑘.

# In[ ]:


for _ in range(int(input())):
	n = int(input())
	a = sorted(list(map(int, input().split())))
	for k in range(n, -1, -1):
		if all(k - 1 + i < n and a[k - 1 + i] <= i + 1 for i in range(k)):
			print(k)
			break


# In[ ]:


for _ in range (int (input())):
    n = int(input())
    a = sorted(list(map(int,input().split())))
    for k in range (n, -1, -1):
        if all (k - 1 + i < n and a[k -1 +i]<= i+1 for i in range (k)):
            print (k)
            break

