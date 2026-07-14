'''
Q3 — Medium
Given a list of numbers, find all pairs that sum up to a given target. Return list of pairs (avoid duplicate pairs).
Input: nums = [2, 7, 11, 15, 1, 6], target = 9
Output: [(2, 7), (1, 8)]  -- wait, fix example below 
''' 
mylist=list(map(int, input().split()))
target=9

lookup=set()
result=set()

for i in range(len(mylist)):
    needed=target - mylist[i]

    if needed in lookup:
        pair=tuple(sorted((needed,mylist[i])))
        result.add(pair)

    lookup.add(mylist[i])
        
print(list(result))