class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        for i in tokens:
            if i == "+":
                second = arr.pop()
                first = arr.pop()
                arr.append(first + second)
            elif i == "-":
                second = arr.pop()
                first = arr.pop()
                arr.append(first - second)
            elif i == "*":
                second = arr.pop()
                first = arr.pop()
                arr.append(first * second)
            elif i == "/":
                second = arr.pop()
                first = arr.pop()
                arr.append(int(first / second))
            else:
                arr.append(int(i))
        return arr[0]