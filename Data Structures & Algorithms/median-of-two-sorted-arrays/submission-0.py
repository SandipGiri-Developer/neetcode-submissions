class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        n1,n2=0,0
        while n1<len(nums1) and n2<len(nums2):
            if nums1[n1]<nums2[n2]:
                res.append(nums1[n1])
                n1+=1
            else:
                res.append(nums2[n2])
                n2+=1
        res = res+nums1[n1:]
        res += nums2[n2:]
        n = len(res)
        if n%2==0:
            return (res[n//2]+res[n//2-1])/2
        return res[n//2]