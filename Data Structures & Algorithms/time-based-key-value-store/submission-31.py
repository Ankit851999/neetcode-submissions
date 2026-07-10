class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        from bisect import bisect_right
        if key not in self.keys:
            return ""
        arr= self.keys[key]
        index = bisect_right(arr, timestamp, key =lambda x: x[0]) -1
        if index >= 0:
            return arr[index][1]
        return ""

