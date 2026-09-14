class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mp = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in mp and st[-1]==mp[i] and st:
                st.pop()
            else:
                st.append(i)
        if not st:
            return True
        return False