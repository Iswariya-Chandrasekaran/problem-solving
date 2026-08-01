'''
july 5 — Easy
1.You are given a sorted list of integers. Remove the duplicates in-place and 
return the length of the list with unique elements only. Do not use a set.
Input:  [1, 1, 2, 3, 3, 4]
Output: 4   # unique elements are [1, 2, 3, 4]
Input:  [1, 1, 1, 1]
Output: 1
'''
arr=list(map(int,input().split()))
slow=0
fast=1
count=1
while slow < len(arr) and fast < len(arr):
    if arr[slow] != arr[fast]:
        count+=1
    slow+=1
    fast+=1
print(count)

# tc= o(n) sc=o(1)

