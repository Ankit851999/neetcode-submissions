class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)-1):
            days = 1
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    break
                if len(temperatures) -1 == j:
                    days = 0
                else:
                    days += 1
            res.append(days)
        res.append(0)
        return res
