class LRUNode:
    def __init__(self, value: int, head: int | None = None, tail: int | None = None) -> None:
        self.value = value
        self.head = head
        self.tail = tail

class LRUCache:

    def __init__(self, capacity: int):
        self.cache: dict[int, LRUNode] = {}
        self.head = None
        self.tail = None
        self.capacity = capacity

    # Gets the node, maintaining order by popping + re-inserting
    def get(self, key: int) -> int:
        if key in self.cache:
            value = self._pop_node(key)
            self._insert_node(key, value)
            return value
        return -1

    # Inserts the node, maintaining order by poping + re-inserting
    # Or popping + inserting if len == capacity
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        elif key in self.cache:
            self._pop_node(key)
        elif len(self.cache) == self.capacity and self.head is not None:
            self._pop_node(self.head)
        self._insert_node(key, value)
        
    def _pop_node(self, key: int) -> int:
        node = self.cache.pop(key)
        if node.head is not None and node.head in self.cache:
            self.cache[node.head].tail = node.tail
        if node.tail is not None and node.tail in self.cache:
            self.cache[node.tail].head = node.head
        if self.tail == key:
            self.tail = node.head
        if self.head == key:
            self.head = node.tail
        return node.value

    def _insert_node(self, key: int, value: int) -> None:
        if self.tail is not None:
            self.cache[self.tail].tail = key
        self.cache[key] = LRUNode(value, self.tail, None)
        self.tail = key
        if self.head is None:
            self.head = key

