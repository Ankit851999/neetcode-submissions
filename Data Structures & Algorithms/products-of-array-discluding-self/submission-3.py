class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        f = 1
        b = [1]* n
        for i in range(n-1, -1, -1):
            if i==n-1:
                b[i] = nums[i]
            else:
                b[i] = nums[i] * b[i+1]
            
        for i in range(0, n-1):
            res.append(f * b[i+1])
            f *= nums[i]
        res.append(f)
        return res

