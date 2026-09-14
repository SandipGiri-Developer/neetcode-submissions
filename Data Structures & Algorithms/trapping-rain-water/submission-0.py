class Solution:
    def trap(self, height: List[int]) -> int:
        rmax = lmax= []
        maxx = -1
        n=len(height)
        res=0
        for i in height:
            if maxx<i:
                maxx=i
            lmax.append(maxx)
        maxx=-1
        for i in height[::-1]:
            if maxx<i:
                maxx=i
            rmax.append(maxx)
        rmax=rmax[::-1]
        for i in range(n):
            water = min(lmax[i],rmax[i])-height[i]
            if water>0:
                res+=water
        return res
