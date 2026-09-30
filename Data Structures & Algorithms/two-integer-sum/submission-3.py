class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maap = {}
        for i, val in enumerate(nums):
            if val in maap:
                return [ maap[val], i]
            else:
                maap[target-val] = i
        return []