class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            if target - i in numbers and numbers.index(i) < numbers.index(target - i):
                i,j = numbers.index(i),numbers.index(target - i)
                numbers.clear()
                numbers.extend([i + 1,j + 1])
                return numbers
        return numbers        


        