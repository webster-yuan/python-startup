class DLinkNode:
    def __init__(self, key:int=0, value:int=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
    
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key:int)->int:
        node = self.cache.get(key)
        if not node:
            # 没有找到，直接返回
            return -1
        
        # 找到了,直接将此节点移动到最前面
        self._move_to_head(node)
        return node.value
        
    def put(self, key:int, value:int):
        node = self.cache.get(key)
        if node:
            # 找到了,直接更新值,并放到最前面
            node.value = value
            self._move_to_head(node)
        else:
            # 没找到,创建一个节点,加入缓存,然后放在前面
            new_node = DLinkNode(key=key, value=value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            self.size +=1
            if self.size > self.capacity:
                # 超出容量,将删除尾部的节点,
                # 清除缓存中节点,大小减一
                tail = self._remove_tail()
                del self.cache[tail.key]
                self.size -=1
    
    def _move_to_head(self, node:DLinkNode):
        self._remove_node(node)
        self._add_to_head(node)
    
    def _remove_node(self,node:DLinkNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self,node:DLinkNode):
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
