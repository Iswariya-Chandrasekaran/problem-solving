"""
Given an array height where each element represents the height of a vertical line,
find two lines that together with the x-axis form a container such that the container
holds the maximum amount of water.

Return the maximum area of water a container can store.

Area = (right - left) * min(height[left], height[right])
"""
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=1
        n=len(height)
        maxi=0
        while left < n and right < n:
            area= (right-left)*min(height[left],(height[right]))
            right+=1
            maxi=max(maxi,area)
            if right == n:
                left+=1
                right=left+1
        return maxi
A=Solution()
print(A.maxArea([1,8,6,2,5,4,8,3,7])) # 49

# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75        