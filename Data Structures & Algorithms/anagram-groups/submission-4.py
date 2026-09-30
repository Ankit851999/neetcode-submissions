class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maap = {}
        res = []
        for i,val in enumerate(strs):
            sr = str(sorted(val))
            maap.setdefault(sr,[]).append(val)
        for i in maap:
            res.append(maap[i])
        return res

            
            
