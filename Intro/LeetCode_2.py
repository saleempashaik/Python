# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getNo(LL: ListNode):
        curr = LL
        no = 0
        while curr:
            no = curr.val + no * 10
            curr = curr.next

        target = 0
        while no != 0:
            target = (no % 10) + (target * 10)
            no = no // 10
        return target

    def creatList(i: int):
        if i == 0:
            return None
        Optional = ListNode(i % 10, createList(i // 10))

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNo(LL: ListNode):
            curr = LL
            no = 0
            while curr:
                no = curr.val + no * 10
                curr = curr.next

            target = 0
            while no != 0:
                target = (no % 10) + (target * 10)
                no = no // 10
            return target

        def createList(i: int):
            if i == 0:
                return None
            Optional = ListNode(i % 10, createList(i // 10))

        firstNo = getNo(l1)
        secondNo = getNo(l2)
        finalNo = firstNo + secondNo
        (createList(finalNo))
        return (Optional)


