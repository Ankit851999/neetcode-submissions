class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        sorted_strs = {}
        for i in strs:
            order = [0] * 26
            for j in i:
                order[ord(j)-ord("a")] +=1 
            if tuple(order) in sorted_strs:
                sorted_strs[tuple(order)].append(i)
            else:
                sorted_strs[tuple(order)] = [i]
        return list(sorted_strs.values())

            

            
            