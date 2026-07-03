class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maap = {}

        for i in nums:
            if i in maap:
                return True

            maap[i] = True

        return False