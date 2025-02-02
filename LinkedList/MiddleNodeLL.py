class ListNode(object):
    def __init__(self, x, next = None):
        self.value = x
        self.next = next

def MiddleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print(slow.value)

def MiddleNode_firstmiddle(head):
    dummy = ListNode(None)
    dummy.next = head
    slow = fast = dummy
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print(slow.value)

node = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
MiddleNode(node)
MiddleNode_firstmiddle(node)