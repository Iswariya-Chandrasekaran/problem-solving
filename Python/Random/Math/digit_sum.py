'''
july 7 — Easy
1. You are given a positive integer. Return the sum of its digits.
Input:  1234
Output: 10

Input:  9876
Output: 30
'''
n=int(input())
sum=0
for i in str(n):
    sum+=int(i)
print(sum)

#tc= o(n) and sc=o(1)
