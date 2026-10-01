class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        compli = {}
        for i in range(len(numbers)):
            if numbers[i] in compli:
                return [compli[numbers[i]] +1,i +1]
            compli[target-numbers[i]] = i
