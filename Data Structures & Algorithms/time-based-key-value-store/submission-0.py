class TimeMap:

    class TimeTree:
        def __init__(self, timestamp: int, val: str):
            self.timestamp = timestamp
            self.val = val
            self.left = None
            self.right = None

        def add(self, timestamp: int, val: str):
            if timestamp == self.timestamp:
                return
            elif timestamp < self.timestamp:
                if self.left is None:
                    self.left = TimeMap.TimeTree(timestamp, val)
                else:
                    self.left.add(timestamp, val)
            else:
                if self.right is None:
                    self.right = TimeMap.TimeTree(timestamp, val)
                else:
                    self.right.add(timestamp, val)
        
        def get(self, timestamp: int, maxVal: "") -> str:
            if timestamp == self.timestamp:
                return self.val
            elif timestamp < self.timestamp:
                if self.left is None:
                    return maxVal
                else:
                    return self.left.get(timestamp, maxVal)
            else:
                if self.right is None:
                    return self.val
                else:
                    return self.right.get(timestamp, self.val)

    class TimeRoot:
        def __init__(self):
            self.root = None
        def add(self, timestamp: int, val: str):
            if self.root is None:
                self.root = TimeMap.TimeTree(timestamp, val)
            else:
                self.root.add(timestamp, val)
        def get(self, timestamp) -> str:
            if self.root is None:
                return ""
            else:
                return self.root.get(timestamp, "")

    def __init__(self):
        self.maps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.maps.setdefault(key, TimeMap.TimeRoot()).add(timestamp, value)

    def get(self, key: str, timestamp: int) -> str:
        return self.maps.setdefault(key, TimeMap.TimeRoot()).get(timestamp)
