class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        right=k-1
        maxi=0
        n=len(nums)
        while left<n-1 and right < n:
            tot=sum(nums[left:right+1])
            avg=tot/k
            maxi=max(avg,maxi)
            left+=1
            right+=1
        return maxi
A=Solution()
print(A.findMaxAverage([1,12,-5,-6,50,3],4))


        