class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        second = 0
        for first in s:
            if second>len(t)-1:
                return False
            while second<len(t):
                if t[second]==first:
                    second+=1
                    break
                else:
                    second+=1
        return True