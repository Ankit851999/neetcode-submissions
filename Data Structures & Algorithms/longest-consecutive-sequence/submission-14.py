class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        store = sorted(set(nums))

        seq = 1
        large = 1

        for i in range(1, len(store)):
            if store[i] - store[i - 1] == 1:
                seq += 1
            else:
                seq = 1

            large = max(large, seq)

        return large