from typing import List, Optional

class ListNode:
    def __init__(self, data=0, nxt=None):
        self.data = data
        self.next = nxt
        
def print_list(l: Optional[ListNode]):
    print("----")
    while l:
        print(l.data)
        l = l.next

def solution(source: Optional[ListNode], front: Optional[ListNode], back: Optional[ListNode]) -> tuple[Optional[ListNode], Optional[ListNode]]:
    # 边界条件：空链表直接返回
    if not source:
        return None, None
    
    # 步骤1：复制整个原链表（避免修改原链表）
    dummy = ListNode(0)
    copy_cur = dummy
    original_cur = source
    while original_cur:
        copy_cur.next = ListNode(original_cur.data)
        copy_cur = copy_cur.next
        original_cur = original_cur.next
    copy_head = dummy.next  # 复制后的链表头
    
    # 步骤2：计算复制后链表的总长度
    count = 0
    cur = copy_head
    while cur:
        count += 1
        cur = cur.next
    
    # 步骤3：快慢指针找中间节点（基于复制后的链表）
    slow = fast = copy_head
    prev_slow = None  # 记录slow的前一个节点，用于切断连接
    while fast and fast.next:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next
    
    # 步骤4：确定前后半部分的分割点，并切断连接
    front_head: Optional[ListNode] = copy_head
    back_head: Optional[ListNode] = None
    
    if count % 2 == 1:
        # 奇数长度：前半部分到中间节点的前一个，后半部分从中间节点开始
        back_head = slow
        if prev_slow:
            prev_slow.next = None  # 切断前半部分和后半部分的连接
    else:
        # 偶数长度：前半部分到中间节点，后半部分从中间节点的下一个开始
        back_head = slow.next
        slow.next = None  # 切断前半部分和后半部分的连接
    
    # 打印结果（便于验证）
    print("前半部分：")
    print_list(front_head)
    print("后半部分：")
    print_list(back_head)
    
    return front_head, back_head


if __name__ == "__main__":
    # 测试用例1：奇数长度链表 1->2->3->4->5
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)
    print("测试用例1（1-2-3-4-5）：")
    front1, back1 = solution(head1, None, None)
    
    # 测试用例2：偶数长度链表 1->2->3->4
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    print("\n测试用例2（1-2-3-4）：")
    front2, back2 = solution(head2, None, None)
    
    # 验证原链表未被修改
    print("\n验证原链表1未被修改：")
    print_list(head1)
    print("验证原链表2未被修改：")
    print_list(head2)