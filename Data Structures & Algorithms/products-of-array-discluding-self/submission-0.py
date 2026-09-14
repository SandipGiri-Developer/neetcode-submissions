class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if nums.count(0)>1:
            return [0]*n
        prefix = [1]
        sufix = [1]
        for i in range(1,n):
            prefix.append(prefix[i-1]*nums[i-1])
            sufix.append(sufix[i-1]*nums[n-i])
        sufix=sufix[::-1]
        for i in range(n):
            nums[i]=prefix[i]*sufix[i]
        return nums