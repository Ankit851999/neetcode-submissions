class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        sorted_strs = {}
        for i in strs:
            sorted_s = "".join(sorted(i))
            if sorted_s in sorted_strs:
                sorted_strs[sorted_s].append(i)
            else:
                sorted_strs[sorted_s] = [i]
        return list(sorted_strs.values())

            

            
            