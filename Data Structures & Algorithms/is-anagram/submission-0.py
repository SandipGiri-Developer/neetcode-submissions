class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDic = {}
        tDic = {}

        # Count characters in `s`
        for c in s:
            sDic[c] = sDic.get(c, 0) + 1

        # Count characters in `t`
        for c in t:
            tDic[c] = tDic.get(c, 0) + 1

        # Compare both dictionaries
        return sDic == tDic
