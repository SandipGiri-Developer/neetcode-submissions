class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        l=0
        freqchar = 0
        reslen = 0
        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r],0)+1
            freqchar = max(freqchar,charMap[s[r]])
            while (r-l+1)-freqchar>k:
                charMap[s[l]]-=1
                l+=1
            reslen = max(reslen,r-l+1)
        return reslen