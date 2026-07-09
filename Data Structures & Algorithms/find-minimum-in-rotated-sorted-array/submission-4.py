class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        si = -1
        while left < right:
            m = (left + right) // 2
            if nums[m] > nums[right] :
                left = m + 1
            else:
                right  = m
        si = nums[left]
        return si