class MinHeap:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        # O(1)
        if self.is_empty():
            raise IndexError("Heap is empty")

        return self.data[0]

    def push(self, val):
        # O(log n)
        self.data.append(val)
        # 新元素可能破坏“父 ≤ 子”，只需一路向上修复
        self._sift_up(len(self.data) - 1)

    def pop(self):
        # O(log n)
        if self.is_empty():
            raise IndexError("Heap is empty")

        root = self.data[0]
        last = self.data.pop()
        if not self.is_empty():
            self.data[0] = last
            # 用最后一个元素顶替 root，可能比子节点大
            self._sift_down(0)

        return root

    def _sift_up(self, cur_index):
        while cur_index > 0:
            parent_index = (cur_index - 1) // 2
            if self.data[parent_index] <= self.data[cur_index]:
                # 如果当前节点的值比父节点的值小，因为维护的是最小堆，堆顶就应该是小值
                break

            # 交换两个位置的值
            self.data[parent_index], self.data[cur_index] = self.data[cur_index], self.data[parent_index]
            # cur_index 上移动
            cur_index = parent_index

    def _sift_down(self, cur_index):
        n = len(self.data)
        while True:
            smallest = cur_index
            left_child = 2 * cur_index + 1
            right_child = 2 * cur_index + 2

            if left_child < n and self.data[left_child] < self.data[cur_index]:
                smallest = left_child
            if right_child < n and self.data[right_child] < self.data[cur_index]:
                smallest = right_child

            if smallest == cur_index:
                break
            self.data[cur_index], self.data[smallest] = self.data[smallest], self.data[cur_index]
            cur_index = smallest


def test_min_heap():
    heap = MinHeap()

    heap.push(5)
    heap.push(3)
    heap.push(8)
    heap.push(1)
    heap.push(2)

    assert heap.peek() == 1
    assert heap.pop() == 1
    assert heap.pop() == 2
    assert heap.pop() == 3
    assert heap.pop() == 5
    assert heap.pop() == 8

    print("MinHeap test passed")


if __name__ == "__main__":
    test_min_heap()
