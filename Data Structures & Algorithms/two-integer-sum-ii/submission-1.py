class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        maap = {}

        for i, num in enumerate(numbers):
            if num in maap:
                return [maap[num] +1 , i +1 ]

            maap[target - num] = i
        return []