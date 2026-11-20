class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += f"{len(i)},{i}"
        return s



    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            word = ""
            n = i
            while s[i] != ",":
                i += 1
            n = int(s[n:i])
            j= i+1
            while j <= i+n and j < len(s):
                word += s[j]
                j += 1
            res.append(word)
            i = j
        return res

