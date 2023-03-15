#!/usr/bin/env python
# coding: utf-8

# Hints:
# 1. Try to brute force for 𝑘<50. Do you see anything suspicious?
# 2. Now try to brute force from 𝑘−1 to 0 for large numbers.

# Is 𝑥=𝑘−1 always suitable?
# 
# The answer is yes, as 𝑥!+(𝑥−1)!=(𝑥−1)!×(𝑥+1)=((𝑘−1)−1)!×((𝑘−1)+1)=(𝑘−2)!×(𝑘), which is clearly a multiple of 𝑘.
# 
# Therefore, 𝑥=𝑘−1is the answer.
# 
# Time complexity: O(1)

# In[ ]:


for testcase in range(int(input())):
    print(int(input()) - 1)


# In[ ]:




