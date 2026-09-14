class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0) + 1
        dic = dict(sorted(dic.items(), key=lambda item:item[1]))   
        ans = list(dic.keys())
        return ans[k-1:] 