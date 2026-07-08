class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions = [0] * (target + 1)
        for i,val in enumerate(position):
            positions[val] = speed[i]
        last_time = 0
        ans = len(position)
        for i in range(target, -1, -1):
            if positions[i]:
                time = (target - i) / positions[i]
                if last_time and time <= last_time:
                    ans -= 1
                else:
                    last_time = time
        return ans




            