class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = [1] * len(nums)
        pre = 1
        for i in range(n):
            results[i]*= pre
            pre *= nums[i]
        post = 1
        for i in range(n-1, -1 , -1):
            results[i] *= post
            post *= nums[i]  
        return results  