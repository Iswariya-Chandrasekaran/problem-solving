'''
july 5
3. You are given a list of integers. Find all unique triplets that add up to zero.
 No duplicate triplets in result.
Input:  [-1, 0, 1, 2, -1, -4]
Output: [(-1, -1, 2), (-1, 0, 1)]
Input:  [0, 0, 0]
Output: [(0, 0, 0)]
'''
arr=list(map(int, input().split()))

def tripletsumzero(arr):
    if len(arr)<3:
        return "Not enough length"
    arr.sort()
    result=set()

    for i in range(len(arr)-2):
        slow=i+1
        fast=len(arr)-1
        while slow < fast :
            total = arr[i]+arr[slow]+arr[fast]
            if total==0:
                result.add(tuple(sorted((arr[i], arr[slow], arr[fast]))))
                slow+=1
                fast-=1
            elif total > 0:
                fast-=1
            elif total < 0:
                slow+=1
    return list(result)

print(tripletsumzero(arr))            
    
# tc= o(n*n) sc=o(n)