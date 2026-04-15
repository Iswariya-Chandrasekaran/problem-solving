class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        
        # Step 1 — build left array
        left = [1] * n
        for i in range(1, n):           # start from 1
            left[i] = left[i-1] * nums[i-1]
        
        # Step 2 — build right array
        right = [1] * n
        for i in range(n-2, -1, -1):    # start from second last
            right[i] = right[i+1] * nums[i+1]
        
        # Step 3 — multiply left × right
        answer = [1] * n
        for i in range(n):
            answer[i] = left[i] * right[i]
        
        return answer
        
        # TC = O(n) — 3 separate passes
        # SC = O(n) — left and right arrays

A = Solution()
print(A.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6] ✅