from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.GreatMap = defaultdict(list)
    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.GreatMap[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        matrix = self.GreatMap[key]
        l,r=0,len(matrix)-1
        ans = ""
        while l<=r:
            mid = l+(r-l)//2
            if matrix[mid][0] == timestamp:
                return matrix[mid][1]
            elif matrix[mid][0]<timestamp:
                ans = matrix[mid][1]
                l = mid+1
            else:
                r=mid-1
        return ans
