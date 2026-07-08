class MinStack:

    def __init__(self):
        self.arr = []
        self.minimum = None
        return None

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.minimum == None:
            self.minimum = val
        elif self.minimum > val:
            self.minimum = val
        return None

    def pop(self) -> None:
        val = self.arr.pop()
        if val == self.minimum:
            if self.arr:
                self.minimum = self.arr[0]
                for i in self.arr:
                    if i < self.minimum:
                        self.minimum = i
            else:
                self.minimum = None
        return None

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        if self.minimum != None:
            return self.minimum
        else:
            return self.arr[0]