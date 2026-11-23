class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                s =  nums[left] + nums[right] + nums[i]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    res.add(
                            tuple(
                    [nums[i],nums[left],nums[right]]
                                )
                                )
                    left += 1
                    right -= 1
        return [ list(i) for i in res]



