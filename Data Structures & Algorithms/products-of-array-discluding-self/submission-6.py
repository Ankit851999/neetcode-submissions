class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forword = [1] * len(nums)
        backwords = [1]* len(nums)
        res = []
        for i in range(0,len(nums)):
            if i != 0:
                forword[i] *= forword[i-1] *nums[i-1]
            if i != len(nums) -1:
                backwords[len(nums)-2 -i] = backwords[len(nums)-1 -i ]* nums[len(nums)-1 -i ]
        for i in range(len(nums)):
            res.append(forword[i]* backwords[i])
        return res
            
