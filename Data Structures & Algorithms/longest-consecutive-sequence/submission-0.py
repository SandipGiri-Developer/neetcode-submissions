class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums))
        ans = 1
        temp = 1
        n = len(nums)
        for i in range(n-1):
            if nums[i] + 1 == nums[i + 1] :
                temp = temp + 1
            else:
                temp = 1
            ans = max(ans , temp)    
        return ans   