class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = defaultdict(int)   
        res = 0
        for i in nums:
            if not seen[i]:
                seen[i] = seen[i-1] + seen[i+1] + 1
                seen[i + seen[i+1]] = seen[i]
                seen[i - seen[i-1]] = seen[i]
                res = max(res, seen[i])
        return res
                

