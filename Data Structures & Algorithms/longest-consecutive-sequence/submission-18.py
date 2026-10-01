class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        s = sorted(list(s))
        seq = 1
        m = 1
        p = s[0]
        for i in range(1, len(s)):
            if s[i] == p+1:
                seq += 1
                p = s[i]
                m = max(seq, m)
            else:
                seq = 1
                p =s[i]
        return m

        # s = set(nums)
        # m= 1
        # small = nums[0]
        # large = nums[0]
        # for i in nums:
        #     if i < small:
        #         small = i
        # for i in nums:
        #     if i > large:
        #         large = i
        # seq = 1
        # while small <= large:
        #     small += 1
        #     if small in s:
        #         seq += 1
        #         m = max(seq, m)
        #     else:
        #         seq = 1
        #         while not small in s and small <= large:
        #             small += 1
        # return m

