class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first=0
        n1,n2=len(word1),len(word2)
        res = ""
        while first<n1 and first < n2:
            res+=word1[first]
            res+=word2[first]
            first+=1
        res+=word1[first:] if first<n1 else ""
        res+=word2[first:] if first<n2 else ""
        return res