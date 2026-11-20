class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forword = [1] * len(nums)
        res = []
        for i in range(1,len(nums)):
            forword[i] = forword[i-1]*nums[i-1]
        prod = nums[-1]
        for i in range(len(nums)-2, -1,-1):
            forword[i] = forword[i] * prod
            prod *= nums[i]
        return forword
            
