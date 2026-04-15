"""
Given an integer array nums, move all 0's to the end of it while maintaining
 the relative order of the non-zero elements.

Example 1: Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2: Input: nums = [0]
Output: [0]

"""
class Solution:
    def moveZeroes(self, nums:list[int])-> None:
        slow=0
        fast=0
        while fast < len(nums):
            if nums[fast]!=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                fast+=1
                slow+=1
            else:
                fast+=1
        print(nums)

A=Solution()
A.moveZeroes([0,1,0,3,12])