class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        stack = []
        for i,num in enumerate(heights):
            while stack and heights[stack[-1]]<=num:
                 stack.pop()
            stack.append(i)
        return stack
        