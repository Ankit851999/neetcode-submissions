class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] or target > nums[-1]:
            return -1
        if target == nums[0]:
            return 0
        elif target == nums[-1]:
            return len(nums) -1    
        ans = -1
        left = 0
        right = len(nums) -1
        while True:
            index = (left + right) //2
            if index == left:
                return ans
            if nums[index] == target:
                ans = index
                break
            elif nums[index] < target:
                left = index 
            elif nums[index] > target:
                right = index
        return ans
            

            
