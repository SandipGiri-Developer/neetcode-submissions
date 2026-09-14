from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for s in strs:
            # Sort the string to get the anagram key
            key = ''.join(sorted(s))
            anagrams[key].append(s)
        
        return list(anagrams.values())
