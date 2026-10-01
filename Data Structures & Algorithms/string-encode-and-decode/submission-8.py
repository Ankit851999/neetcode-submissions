class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s+= f"{len(i)}\n"
            s+= i
            s += "\n"
        return s

    def decode(self, s: str) -> List[str]:
        arr = []
        if s == "":
            return arr
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "\n":
                j += 1
            # return [f"{i},{j}, {s[i:j]}"]
            length = int(s[i:j])
            i = j + 1
            if length:
                arr.append(s[i: i+ length])
                i += length+1
            else:
                arr.append("")
                i += 1
        return arr
            





