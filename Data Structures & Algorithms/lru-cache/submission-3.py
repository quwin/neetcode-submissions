class LRUNode:
    def __init__(self,
        value: int,
        head: int | None = None,
        tail: int | None = None,
    ) -> None:
        self.head = head
        self.value = value
        self.tail = tail


class LRUCache:
    def __init__(self, capacity: int):
        self.cache: dict[int, LRUNode] = {}
        self.head: int | None = None  # Least recently used
        self.tail: int | None = None  # Most recently used
        self.capacity = capacity

    def _remove(self, key: int) -> None:
        node = self.cache[key]

        if node.head is not None:
            self.cache[node.head].tail = node.tail
        else:
            self.head = node.tail

        if node.tail is not None:
            self.cache[node.tail].head = node.head
        else:
            self.tail = node.head

    def _add_to_tail(self, key: int) -> None:
        node = self.cache[key]

        node.head = self.tail
        node.tail = None

        if self.tail is not None:
            self.cache[self.tail].tail = key
        else:
            self.head = key

        self.tail = key

    def _make_recent(self, key: int) -> None:
        if self.tail != key:
            self._remove(key)
            self._add_to_tail(key)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self._make_recent(key)
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache[key].value = value
            self._make_recent(key)
            return

        if len(self.cache) == self.capacity:
            lru_key = self.head
            assert lru_key is not None

            self.head = self.cache[lru_key].tail
            if self.head is not None:
                self.cache[self.head].head = None
            else:
                self.tail = None

            del self.cache[lru_key]

        self.cache[key] = LRUNode(value)
        self._add_to_tail(key)