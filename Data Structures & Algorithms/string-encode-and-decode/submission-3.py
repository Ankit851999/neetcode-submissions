class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        encoded = str(len(strs)) + "\n"
        for i in strs:
            for j in list(i):
                encoded += chr(ord(j) + 5)
            encoded += '\n'
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        length = int(s.split('\n')[0]) + 1
        ns = s.split('\n')
        for i in range(1, length ):
            strr = ns[i]
            decoded = ''
            for j in list(strr):
                decoded += chr(ord(j) -5)
            result.append(decoded)
        return result


