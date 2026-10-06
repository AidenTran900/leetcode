from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.last_used = deque()

    def updated(self, key):
        if key in self.last_used:
            self.last_used.remove(key)

        self.last_used.appendleft(key)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.updated(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.updated(key)
        else:
            if len(self.cache) >= self.capacity:
                last = self.last_used.pop()
                del self.cache[last]

            self.cache[key] = value
            self.updated(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)