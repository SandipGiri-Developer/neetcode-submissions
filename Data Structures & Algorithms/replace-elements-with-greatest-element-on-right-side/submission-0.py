class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        rightmax = -1
        ans =[-1]*n
        for i in range(n-1,-1,-1):
            ans[i]=rightmax
            rightmax = max(rightmax,arr[i])
        return ans