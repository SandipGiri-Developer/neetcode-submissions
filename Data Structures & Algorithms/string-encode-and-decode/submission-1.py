from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            # Encode each string with "length<delimiter>string"
            ans += str(len(s)) + "rucha" + s
        return ans   

    def decode(self, s: str) -> List[str]:
        i, decoded = 0, []
        while i < len(s):
            # Find where the delimiter "rucha" appears
            j = s.find("rucha", i)
            # The number before "rucha" is the length of the string
            length = int(s[i:j])
            # Extract the string of that length after "rucha"
            decoded.append(s[j + 5: j + 5 + length])
            # Move to the next encoded part
            i = j + 5 + length
        return decoded

