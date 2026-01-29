class DLinkedNode:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        self.size = 0

        # 给一个空投空尾，这样方便头插尾删
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1

        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int):
        node = self.cache.get(key)
        if node is not None:
            # 更新值，并移动到头部
            node.value = value
            self._move_to_head(node)
        else:
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            self.size += 1

            if self.size > self.capacity:
                # 超出容量，将删除尾部节点
                tail = self._remove_tail()
                del self.cache[tail.key]
                self.size -= 1

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node


def test_lru_basic():
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # 返回 1

    cache.put(3, 3)  # 淘汰 key=2
    assert cache.get(2) == -1

    cache.put(4, 4)  # 淘汰 key=1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    print("Basic test passed")


def test_lru_capacity_one():
    cache = LRUCache(1)

    cache.put(1, 1)
    cache.put(2, 2)  # 淘汰 1
    assert cache.get(1) == -1
    assert cache.get(2) == 2

    print("Capacity=1 test passed")


def test_lru_update():
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(1, 100)  # 更新 value + 刷新 LRU
    assert cache.get(1) == 100

    cache.put(2, 2)
    cache.put(3, 3)  # 淘汰 key=1（不是 2！）

    assert cache.get(1) == -1
    assert cache.get(2) == 2
    assert cache.get(3) == 3

    print("Update test passed")


if __name__ == '__main__':
    test_lru_basic()
    test_lru_capacity_one()
    test_lru_update()
