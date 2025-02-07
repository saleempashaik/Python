# arr = [1, 2, 3, 4]


class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_ll(head):
    stk = []

    while head:
        stk.append(head)
        head = head.next

    dummy = Node(0)

    newhead = dummy
    while stk:
        # print(stk)
        node = stk.pop()
        node.next = None
        newhead.next = node
        newhead = newhead.next
    return dummy.next


def print_ll(head):
    while head:
        print(head.val)
        head = head.next


linkedlist = Node(1, Node(2, Node(3, Node(4, None))))

newnode = reverse_ll(linkedlist)
print(print_ll(newnode))
