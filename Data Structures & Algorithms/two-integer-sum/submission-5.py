class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complemntary = {}
        for i in range(len(nums)):
            if nums[i] in complemntary:
                return [complemntary[nums[i]], i]
            complemntary[target-nums[i]] = i
