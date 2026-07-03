class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for i in nums:
            if i in count_map:
                count_map[i] = count_map[i] +1
            else:
                count_map[i] = 1
        bucket = [ [] for _ in range(len(nums)+ 1)]
        for value, freq in count_map.items():
            bucket[freq].append(value)
        results = []
        for i in range(len(bucket)-1, 0 ,-1):
            for j in bucket[i]:
                results.append(j)
                if len(results) == k:
                    return results
        return results