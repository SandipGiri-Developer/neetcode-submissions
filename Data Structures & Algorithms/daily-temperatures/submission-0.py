class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        monotonic = []
        res = [0]*len(temp)
        for i,n in enumerate(temp):
            while monotonic and monotonic[-1][1]<n:
                idx = monotonic.pop()[0]
                res[idx] = abs(idx-i)
            monotonic.append([i,n])
        return res
        