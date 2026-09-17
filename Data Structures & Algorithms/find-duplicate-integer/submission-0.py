class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        supposed = 0
        real = 0
        for n in range(len(nums)+1):
            supposed+=n+1
            real+=nums[n]
            if supposed!=real:
                return nums[n]
        return nums[n]