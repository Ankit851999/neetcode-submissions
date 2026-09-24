class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        large = 0
        seq = 0
        last = nums[0]
        for i in nums:
            if i == last +1:
                seq += 1
                if seq > large:
                    large = seq
            elif i > last:
                seq = 0
            last = i
        return large +1
            

