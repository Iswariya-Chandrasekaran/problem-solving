"""
Given an array of integers, remove all occurrences 
of a given value IN PLACE and return the count of 
remaining elements.

The relative order of elements should be kept.
Do not use any extra list or set.

Example 1:
Input:  arr = [3, 2, 2, 3, 4, 3, 5]  val = 3
Output: 4
Array becomes: [2, 2, 4, 5, 3, 3, 5] 
               (first 4 elements matter only)
               
slow = tracks where to WRITE next VALID element
fast = scans everything

When fast finds a NON-VAL element → write it at slow → slow moves
When fast finds VAL → skip it → only fast moves

"""
class Solution:
    def remove_element(self, arr: list[int], val: int) -> int:
        slow=0           # tracks where to write next valid element
        fast=0           # scans every element
        while fast < len(arr):  # fast drives the loop O(n)
            # found valid element O(1)
            if arr[fast]!=val:  #3==3, 2!=3, 2!=3, 3=3, 4!=3
                # write at slow O(1
                arr[slow]=arr[fast]    #[2,2,3]
                fast+=1 #fast[2]=2, fast[3]
                slow+=1 #slow[1]=2, slow[2]
            # found val → skip    
            else:     
                fast+=1  # fast[1]=2, fast[4]
        return slow # count of valid elements

A = Solution()

arr1 = [3, 2, 2, 3, 4, 3, 5]
count = A.remove_element(arr1, 3)
print(count)          # 4
print(arr1[:count])   # [2, 2, 4, 5] ✅

arr2 = [1, 1, 1, 1]
count = A.remove_element(arr2, 1)
print(count)          # 0
print(arr2[:count])   # [] ✅

arr3 = [1, 2, 3, 4, 5]
count = A.remove_element(arr3, 6)
print(count)          # 5
print(arr3[:count])   # [1, 2, 3, 4, 5] ✅
            
    