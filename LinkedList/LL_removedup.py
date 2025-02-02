# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x, next=None):
    self.value = x
    self.next = next
def printLL(head):
    while head:
        print(head.value, end='->')
        head = head.next

def solution(head):
    if not head or not head.next:
        return head
    curr = head
    while curr.next is not None and curr is not None:
        if curr.value == curr.next.value:
            curr.next = curr.next.next

        curr = curr.next
    return head


head = ListNode(1, ListNode(2, ListNode(2, ListNode(3,ListNode(3)))))
LL = ListNode(1, ListNode(1))
printLL(solution(LL))

