'''
Q2 — Easy-Medium
You are given a list of integers. Find the first element that appears more than once. 
If no duplicate exists, return -1.
Input:  [3, 5, 2, 3, 7, 5]
Output: 3
Input:  [1, 2, 3, 4]
Output: -1
'''

given=list(map(int,input().split()))
freq={}
def firstdup(given):
    for i in given:
        freq[i]=freq.get(i,0)+1
        if freq[i]==2:
            return i
            break
    return -1
print(firstdup(given))
    
#tc = o(n) Sc = o(n)