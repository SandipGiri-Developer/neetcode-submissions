class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l,r=1,res
        while l<=r:
            mid = l+(r-l)//2
            summ = 0
            for p in piles:
                if p%mid==0:
                    summ+=p//mid
                else:
                    summ+=(p//mid+1)
            if summ<=h:
                res = min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res