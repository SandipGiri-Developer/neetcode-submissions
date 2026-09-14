class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mp = {')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in mp.values():
                st.append(ch)
            elif not st or mp[ch] != st.pop():
                return False
        return not st