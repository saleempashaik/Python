# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))
# ll = curLL
# while ll:
#     print(str(ll.val) + "->")
#     ll = ll.next

def getNo(LL: ListNode):
        curr = LL
        no = 0
        while curr:
            no = curr.val + no * 10
            # print(f"no value is {no}")
            curr = curr.next

        # print(no)

        target = 0
        while no != 0:
            target = (no % 10) + (target * 10)
            # print(f"target value {target}")
            no = no // 10
        return target

print(getNo(l1))
print(getNo(l2))



def createList(i):
    if i == 0:
        return None
    # Optional = ListNode(i%10)
    Optional = ListNode((i % 10), createList(i // 10))
    return Optional

# print(createList(243))
ll = createList(getNo(l1)+getNo(l2))
while ll:
    print(str(ll.val))
    ll = ll.next