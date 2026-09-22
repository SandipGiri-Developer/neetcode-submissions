class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        resMap = defaultdict(lambda:-1)
        for n in nums2:
            while stack and stack[-1]<n:
                num = stack.pop()
                resMap[num]=n
            stack.append(n)
        res = []
        for n in nums1:
            res.append(resMap[n])
        return res