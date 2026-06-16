"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.You may assume that each input would
have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
     ExampleInput: nums = [2, 7, 11, 15], target = 9
     Output: [0, 1]
     Explanation: Because nums[0] + nums[1] == 2 + 7 == 9, we return [0, 1].
"""

nums = [2,7,11,15]
target = 13

class solution:
    def twosum(self, nums:list, target:int) ->list:
        lookup={}
        for i,num in enumerate(nums):
            needed=target-num
# If the complement number is already in our dictionary, we found the pair!
            if needed in lookup:
                return [lookup[needed], i]
# Otherwise, save the current number and its index for future matches           
            lookup[num]=i

A=solution()
print(A.twosum(nums,target))        