class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for i in nums:
            if i in count_map:
                count_map[i] = count_map[i] +1
            else:
                count_map[i] = 1
        freq_map = {}

        for (value,count) in count_map.items():
            if count in freq_map:
                if value  not in freq_map[count]:
                    freq_map[count].append(value)
            else:
                freq_map[count] = [value]
        freq_map  = dict(sorted(freq_map.items(), reverse=True))
        result = []
        for i in freq_map:
            for j in freq_map[i]:
                if len(result) == k:
                    return result
                else:
                    result.append(j)
        return result