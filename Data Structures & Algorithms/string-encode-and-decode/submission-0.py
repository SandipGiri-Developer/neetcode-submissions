class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += "rucha"
            ans += s
            
        return ans[5:]   

    def decode(self, s: str) -> List[str]:
        return s.split("rucha")
