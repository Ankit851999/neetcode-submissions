class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        long = 1


        for i in range(len(nums)):
            num = nums[i]
            if num-1 in s:
                continue
            while num +1 in s:
                num += 1
                long = max(long, num - nums[i] +1)
        return long

            
