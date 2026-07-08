class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maap = {
            ")": "(", 
            "}": "{", 
            "]": "[",
        }
        for i in s:
            if i not in maap:
                stack.append(i)
            elif not stack or stack.pop() != maap[i]:
                return False                
        return not stack


        