class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True

            seen.add(nums[i])

            if len(seen) > k:
                seen.remove(nums[i - k])

        return False
A=Solution()
print(A.containsNearbyDuplicate([1,2,3,1], 3))