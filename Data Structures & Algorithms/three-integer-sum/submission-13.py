class Solution:
    def threeSum(self, nums):
        res = set()
        for i in range(len(nums)):
            target = 0 - nums[i]
            seen ={}
            for j in range(i+1, len(nums)):
                if nums[j] in seen :
                    if seen[nums[j]]:
                        arr =sorted([nums[i], nums[seen[nums[j]]], nums[j]])
                        arr = tuple(arr)
                        res.add(arr)
                seen[target -nums[j]] = j
        return [ list(l) for l in list(res)] if res else []