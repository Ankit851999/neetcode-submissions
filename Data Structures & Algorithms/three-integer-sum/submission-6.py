class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            s = i + 1
            t = len(nums) - 1

            while s < t:
                total = nums[i] + nums[s] + nums[t]

                if total == 0:
                    result.append([nums[i], nums[s], nums[t]])

                    s += 1
                    t -= 1

                    while s < t and nums[s] == nums[s - 1]:
                        s += 1

                    while s < t and nums[t] == nums[t + 1]:
                        t -= 1

                elif total < 0:
                    s += 1
                else:
                    t -= 1

        return result