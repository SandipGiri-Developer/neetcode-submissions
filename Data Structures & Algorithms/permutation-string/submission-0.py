from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        fixed = Counter(s1)
        variable = {}
        l=0
        length = len(s1)
        for r in range(len(s2)):
            variable[s2[r]] = variable.get(s2[r],0)+1
            while r-l+1>length:
                variable[s2[l]]-=1
                if variable[s2[l]]<1:
                    del variable[s2[l]]
                l+=1
            if fixed==variable:
                return True
        return False