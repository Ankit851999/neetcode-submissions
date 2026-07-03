class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
        maxcon = 1
        for small in nums:
            con = 1 
            for i in range(len(nums)):
                if small + 1 not in seen:
                    break
                small += 1
                con += 1 
            if con > maxcon:
                maxcon = con
        return maxcon