class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = {"timestamps": []}
        self.keys[key][timestamp] = value
        self.keys[key]["timestamps"].append(timestamp)


    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if  key not in self.keys:
            return ans
        elif len(self.keys[key]["timestamps"]) == 0:
            return ans
        elif timestamp in self.keys[key]:
            return self.keys[key][timestamp]
        left = 0
        right = len(self.keys[key]["timestamps"]) -1

        if self.keys[key]["timestamps"][-1] < timestamp:
            return self.keys[key][self.keys[key]["timestamps"][-1]]
        elif self.keys[key]["timestamps"][0] > timestamp:
            return ans

        while right - left > 1 :
            mid = (left + right) // 2
            if self.keys[key]["timestamps"][mid] > timestamp:
                right  = mid
            else:
                left = mid
        ans = self.keys[key][self.keys[key]["timestamps"][left]]

        return ans