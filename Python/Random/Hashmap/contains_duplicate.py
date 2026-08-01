'''
july 3
1. You are given a list of integers. Return True if any value appears at least twice, 
else return False.
Input:  [1, 2, 3, 1]
Output: True
'''
given=list(map(int,input().split()))

freq={}
def valuetwice(given):
    for i in given:
        freq[i]=freq.get(i,0)+1
    for value in freq.values():
        if value >=2:
            return True   
    return False 
print(valuetwice(given))
 
#tc=o(n) sc=o(n)