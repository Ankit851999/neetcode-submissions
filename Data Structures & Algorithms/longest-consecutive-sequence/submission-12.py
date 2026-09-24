class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not len(nums):
            return 0
        sorted_array = sorted(nums)
        store = set(sorted_array)
        store = sorted(list(store))
        seq = 0
        large = 0
        for i,n in enumerate(store):
            if len(store) > i+1:
                if abs(store[i+1] - n) == 1:
                    seq += 1
                else:
                    seq = 0
            if seq > large:
                large = seq
        return large + 1