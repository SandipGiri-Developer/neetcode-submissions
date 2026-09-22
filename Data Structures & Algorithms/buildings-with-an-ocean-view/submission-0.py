class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [-1]*len(heights)
        stack = []
        for i,num in enumerate(heights):
            while stack and heights[stack[-1]]<=num:
                idx = stack.pop()
                res[idx] = num
            stack.append(i)
        ans = []
        for i,n in enumerate(res):
            if n==-1:
                ans.append(i)
        return ans