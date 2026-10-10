from collections import deque;

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.lru = deque([])
        self.updateMap = {}
        # In terms of recency, O(1) get with O(n) put is trivial
        # To achieve O(1) average put, a deque (FILO) can be used
        # But how can the deque reflect updates from get()
        # When updated, put it at end of deque, 
        # and ignore stale deque entries

    def get(self, key: int) -> int:
        if key in self.cache:
            self.updateRecency(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.updateRecency(key)
        self.cache[key] = value
        if len(self.cache) <= self.capacity:
            return
        # Else pop deque until a non stale entry is found
        # remove the key for that entry
        while self.lru:
            leastRecent = self.lru.popleft()
            self.updateMap[leastRecent] -= 1
            if self.updateMap[leastRecent] == 0:
                del self.cache[leastRecent]
                break

    
    def updateRecency(self, key: int):
        current = self.updateMap.setdefault(key, 0)
        self.updateMap[key] = current + 1
        self.lru.append(key)

