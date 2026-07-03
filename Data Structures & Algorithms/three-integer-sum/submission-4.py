class Solution:
    def threeSum(self, nums):
        nums.sort()
        resuts = set()
        for i in range(len(nums)-2):
            s = i+1
            t = len(nums)-1
            while s < t:
                if nums[i] + nums[s] + nums[t] == 0:
                    resuts.add((nums[i] , nums[s] ,nums[t]))
                    t -= 1
                    s += 1
                elif nums[i] + nums[s] + nums[t] > 0:
                    t -= 1
                else:
                    s += 1


        return [list(i) for i in resuts]