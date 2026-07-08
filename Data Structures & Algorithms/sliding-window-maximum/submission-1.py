class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        arr = []

        left = 0

        for right in range(len(nums)):
            arr.append(nums[right])
            if len(arr) >= k:
                if len(arr) > k:
                    arr.remove(nums[left])
                    left += 1
                res.append(max(arr))
        return res
                

