'''
july 1 — Longest Consecutive Sequence
2. Given an unsorted list of integers, find the length of the longest sequence of 
consecutive numbers. The numbers don't need to be adjacent in the list — they just 
need to form a consecutive chain.
Input:  nums = [100, 4, 200, 1, 3, 2]
Output: 4        # sequence: 1, 2, 3, 4
Input:  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9        # sequence: 0, 1, 2, 3, 4, 5, 6, 7, 8
'''
mylist=list(map(int,input().split()))
unique=sorted(set(mylist))
current_streak=0
max_streak=0
for i in range(len(unique)):
    if i==0 or unique[i] == unique[i-1]+1:
        current_streak+=1
    else:
        max_streak=max(max_streak,current_streak)
        current_streak=1

max_streak=max(max_streak,current_streak)
print(max_streak)
# tc=o(n log n) sc=o(n)
