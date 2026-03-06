class ListNode:
    def __init__(self, key:int ,next=None):
        self.key = key
        self.next = next
        
def reverse_list(head:ListNode):
    pre = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = pre
        pre = cur
        cur = next_node
    
    return pre

def print_list(head:ListNode):
    res = []
    while head:
        res.append(head.key)
        head = head.next
    
    print(res)

head = ListNode(1, ListNode(2, ListNode(3)))
print_list(reverse_list(head))