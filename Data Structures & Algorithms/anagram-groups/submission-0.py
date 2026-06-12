class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def isAnagram( w1,w2):
            
            if len(w1) != len(w2):
                return False
            
            return sorted(w1) == sorted(w2)

        res = []
        counted = set()

        for i,a in enumerate(strs):
            
            if a in counted:
                continue

            curr_anagrams = []
            
            for j in strs[i:]:
                if isAnagram(a,j):
                    counted.add(j)
                    curr_anagrams.append(j)
            
            res.append(curr_anagrams)
        
        return res
