'''july 4 — Easy
1. You are given a list of integers. Return the only element that appears an odd number of times.
 It is guaranteed that exactly one such element exists.
Input:  [1, 2, 3, 2, 3, 1, 3]
Output: 3
Input:  [5, 5, 7]
Output: 7
'''
from collections import Counter
nums=list(map(int,input().split()))
counts=Counter(nums)
for key,value in counts.items():
    if value % 2 != 0:
        print(key)

# tc= o(n) sc = o(n)
