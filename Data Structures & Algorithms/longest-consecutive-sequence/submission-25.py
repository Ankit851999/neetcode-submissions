class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        seen = []
        large = nums[0]
        long = 1

        for i in nums:
            large = max(large, i)

        for i in range(len(nums)):
            num = nums[i]

            is_seen = False
            for arr in seen:
                if num >= arr[0] and num <= arr[1]:
                    is_seen = True
            if is_seen:
                continue
            
            num += 1
            if num in s:
                seen_set = [num -1, num]
                long = max(long, 2)
                while num+1 in s and num+1 <= large:
                    num += 1
                    seen_set[1] = num
                    long = max(long, seen_set[1]- seen_set[0] +1 ) 
                seen.append(seen_set)
        return long

            
