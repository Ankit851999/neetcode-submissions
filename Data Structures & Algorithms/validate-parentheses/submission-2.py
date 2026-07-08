class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = [ "(", "{", "["]
        maap = {
            ")": "(", 
            "}": "{", 
            "]": "[",
        }
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            elif stack and stack[-1] == maap[s[i]]:
                    stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False


        