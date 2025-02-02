# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def solution (head1,head2):
    dummy = ListNode(None)
    current = dummy
    print(current.value)
    print(head1.value,head2.value)
    while ( head1 and  head2):
        if head1.value < head2.value:
            current.next = head1
            head1 = head1.next
            print(head1.value)
        else:
            current.next = head2
            print(head2.value)
            head2 = head2.next
        current = current.next
    current.next = head1 if head1 is not None else head2

    return dummy.next


solution(ListNode(1),ListNode(2))


