class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += f"{len(i)},{i}"
        return s



    def decode(self, s: str) -> List[str]:
        res = []
        left = 0
        while left < len(s):
            word = ""
            right = left
            while s[right] != "," :
                right += 1
            n = int(s[left:right])
            word = s[right + 1: right +n+1]
            res.append(word)
            left =  right +n+1
        return res

