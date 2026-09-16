class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        currmax=max(nums[:k])
        res.append(currmax)
        l=1
        for r in range(k,len(nums)):
            currmax = max(nums[l:r+1])
            l+=1
            res.append(currmax)
        return res