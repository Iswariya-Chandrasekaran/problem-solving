'''
Q2 — Easy-Medium
You are given a list of integers nums and an integer target. Return the indices 
of the two numbers that add up to the target. Assume exactly one solution exists.
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]   # nums[0] + nums[1] = 2 + 7 = 9
Input:  nums = [3, 2, 4], target = 6
Output: [1, 2]   # nums[1] + nums[2] = 2 + 4 = 6
'''
given=list(map(int,input().split()))
target=int(input())

mydict={}

for idx,value in enumerate(given):
    needed=target-value
    
    if needed in mydict:
        print(mydict[needed],idx)
    else:
        mydict[value]=idx

#tc= o(n) sc=o(n)

