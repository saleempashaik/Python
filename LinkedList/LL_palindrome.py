class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    def check(node, front):
        if not node:
            return True, front

        is_pal, last = check(node.next, front)
        if not is_pal or last.val != node.val:
            return False, last.next
        return True, last.next

    return check(head, head)[0]

# Example usage:
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(is_palindrome(head))