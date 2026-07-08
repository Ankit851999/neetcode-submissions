class MinStack:

    def __init__(self):
        self.arr = []
        self.minArr = []
        return None

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.minArr or self.minArr[-1] > val:
            self.minArr.append(val)
        else:
            self.minArr.append(self.minArr[-1])
        return None

    def pop(self) -> None:
        self.arr.pop()
        self.minArr.pop()
        return None

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.minArr[-1]