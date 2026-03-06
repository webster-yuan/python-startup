
class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next



def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    cur = dummy
    while list1 and list2:
        if list1.val > list2.val:
            cur.next = list2
            list2 = list2.next
        else:
            cur.next = list1
            list1 = list1.next
        
        cur = cur.next

    cur.next = list1 if list1 else list2
    return dummy.next


def print_list(head:ListNode):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    
    print(res)

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
print_list(mergeTwoLists(l1, l2))  # [1,1,2,3,4,4]