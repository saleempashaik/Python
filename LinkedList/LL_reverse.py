class ListNode(object):
    def __init__(self, x, next = None):
        self.value = x
        self.next = next

def printLL(head):
    while head:
        print(head.value, end='->')
        head = head.next

#
def LL_reverse_R(node):
    if not node or not node.next:
        return node
    print(f"{node.value}, node value")
    newhead = LL_reverse_R(node.next)
    print(f"{node.next.value}, node next value")
    print(f"{newhead.value},newhead.value")
    node.next.next = node
    node.next = None
    print(f"{newhead.next.value}, newheads next value")
    print('-------------------')

    return newhead

L1 = ListNode(1,ListNode(2,ListNode(3)))

# printLL(L1)
# print()
printLL(LL_reverse_R(L1))