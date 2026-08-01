'''
july 7 — Medium
3. You are given a list of integers from 1 to n but one number is missing. 
Find the missing number.
Input:  [1, 2, 4, 5, 6], n=6
Output: 3

Input:  [1, 3, 4], n=4
Output: 2
'''
mylist=list(map(int,input().split()))
n=int(input())

expected=n*(n+1) // 2
actual=sum(mylist)
print(expected-actual)
# tc=o(n) sc=o(1)