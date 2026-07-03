class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maap = {}
        for i, val in enumerate(nums):
            if target-val in maap:
                return [ maap[target-val], i ]
            maap[val] = i
        return []