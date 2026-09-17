class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache =  {}
        self.size = 0
        self.recently_used = 10001

    def get(self, key: int) -> int:
        self.recently_used = min(self.recently_used,key)
        if key not in self.cache:
            return -1
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if self.size>=self.capacity:
            del self.cache[self.recently_used]
        self.cache[key]=value
        self.size+=1
        
