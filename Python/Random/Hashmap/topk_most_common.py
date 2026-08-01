'''
july 3
3. You are given a list of integers and a number k.
 Find the top k most frequent elements. Return them in any order.
Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
Input:  nums = [1], k = 1
Output: [1]
'''
from collections import Counter
nums=list(map(int,input().split()))
k=int(input())
counts=Counter(nums)
result=[key for key, _ in counts.most_common(k)]
print(result)

#tc=o(n) sc=o(n)