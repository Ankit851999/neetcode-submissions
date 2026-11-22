class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0
        seen = set(nums)
        small = nums[0]
        lag = nums[0]

        for i in nums:
            small = i if small > i else small
            lag = i if lag < i else lag
        n = 0
        seq = 0
        while n < len(nums):
            num = nums[n]
            left = num
            right = num
            while left - 1 in seen:
                left -= 1
            while right + 1 in seen:
                right += 1

            seq = max(seq, right - left)
            n += right - num + 1
        return seq +1
            
                
                

