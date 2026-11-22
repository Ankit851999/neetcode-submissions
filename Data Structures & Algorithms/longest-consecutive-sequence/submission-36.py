class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0
        seen = set(nums)
        seq = 0
        for i in seen:
            if i-1 in seen:
                continue
            l = 1
            while i + l in seen:
                l += 1
            seq = max( seq,l)    
        return seq        
                
                

