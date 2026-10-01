class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        f = [1] * n
        res = [1] * n
        for i in range(n):
            if i==0:
                f[0] = nums[0]
            else:
                f[i] = nums[i] * f[i-1]
        b = [1]* n
        for i in range(n-1, -1, -1):
            if i==n-1:
                b[i] = nums[i]
            else:
                b[i] = nums[i] * b[i+1]
            
        for i in range(n):
            res[i] =( b[i+1] if i < n-1 else 1) *( f[i-1] if i > 0 else 1)
        return res

