import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        for i in range(len(nums)):
            nums[i]=1
            res=math.prod(nums)
            answer.append(res)
        return answer
A=Solution()
A.productExceptSelf([1,2,3,4])