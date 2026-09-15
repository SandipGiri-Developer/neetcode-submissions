class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return target==nums[0]
        left,right=0,len(nums)-1

        while left<right:
            mid = left + (right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[left]>target and nums[right]>target:
                left=mid+1
            else:
                right=mid
        return -1