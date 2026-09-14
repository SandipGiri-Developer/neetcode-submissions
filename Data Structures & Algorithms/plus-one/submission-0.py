class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s += str(i)
        s = int(s) + 1
        s = str(s)
        digits = []
        for i in s:
            digits.append(int(i))
        return digits    
        