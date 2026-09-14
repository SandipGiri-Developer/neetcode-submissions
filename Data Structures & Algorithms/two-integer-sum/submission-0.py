class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lenN = len(nums)
        List =[]
        for i in range(0,lenN):
            secN = target - nums[i]
            for j in range(i+1,lenN):
                if nums[j] == secN:
                    List=[i,j]
                    return List
        return List               