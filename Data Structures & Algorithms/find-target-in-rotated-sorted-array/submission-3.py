class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n==1 and nums[0] == target:
            return 0
        left,right=0,n-1

        while left<right:
            mid = left + (right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[left]>target and nums[right]>target:
                left=mid+1
            else:
                right=mid
        return -1