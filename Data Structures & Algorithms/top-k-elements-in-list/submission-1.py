from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        most_common = sorted(count.keys(), key=lambda x: (-count[x], x))
        return most_common[:k]
        