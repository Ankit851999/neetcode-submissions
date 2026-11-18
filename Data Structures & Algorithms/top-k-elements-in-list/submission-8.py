class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
        hasttable = [[]for _ in range(len(nums)+1)]
        for i in count:
            hasttable[count[i]].append(i)
        res = []
        i = len(nums) 
        while len(res) < k and i >=0:
            for j in hasttable[i]:
                res.append(j)
                if len(res) == k:
                    return res
            i -= 1
        return res


