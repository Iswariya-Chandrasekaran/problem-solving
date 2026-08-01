'''
july 1
1. Given a list of integers and a number k, rotate the list to the right by k steps.
 This means the last k elements should move to the front in the same order.
Input:  nums = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]
'''
from collections import deque

mylist=list(map(int,input().split()))
k=2
for i in range(k):
    mylist.insert(0,mylist.pop())
print(mylist)
# pop=o(1) insert=o(n)
# --------------- tc= o(n*k) slow sc = o(1)
d=deque(mylist)
d.rotate(2)
print(list(d))
# deque=o(n) rotate=o(k), convert list=o(n)
# tc=o(n) fast sc=o(n)
