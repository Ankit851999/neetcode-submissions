class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1
        counts = [0] * (len(nums) +1)
        for i in count:
            if not counts[count[i]]:
                counts[count[i]] = [i]
            else:
                counts[count[i]].append(i)
        res = []
        for i in range(len(counts)-1, -1, -1):
            if len(res) == k:
                return res
            if not counts[i]:
                continue
            for j in counts[i]:
                if len(res) == k:
                    return res
                res.append(j)
        return res
