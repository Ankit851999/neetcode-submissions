class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maap = {}
        output = []
        for i in strs:
            sortedarr = "".join(sorted(i))
            if sortedarr in maap:
                maap[sortedarr].append(i)
            else:
                maap[sortedarr] = [i]
        for i in maap:
            output.append(maap[i])
        return output
            