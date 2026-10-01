class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [nums[0]]
        f = 1
        b = 1
        for i in range(1,n-1):
            res.append(res[i-1]* nums[i])
        res.append(nums[n-1])
        b = 1
        for i in range(n-1,0,-1 ):
            res[i] = b * res[i-1]
            b *= nums[i]
        res[0] = b
        return res


