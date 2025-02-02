# array = [1, 2, 3]
# var = array[0] == 1
#
# print(var)
#
# def recurPrint(n,pointer = 0):
#     if pointer < n:
#         print(pointer)
#         return recurPrint(n,pointer+1)
#
# def recursiveMax(arr, curMax=float('-inf'), i = 0) -> int:
#     if i < len(arr):
#         print(f"in {i} iteration, {curMax} current Max Value")
#         return recursiveMax(arr, max(curMax, arr[i]), i + 1)
#     print(f"Outer look: in {i} iteration, {curMax} current Max Value")
#
#     return curMax
#
# print(recursiveMax([1,2,3]))



class ListNode(object):
  def __init__(self, x, next_node=None):
    self.value = x
    self.next = next_node

# def solution(head):
#     if head.next is None:
#         return (head.value)
#     return print(solution(head.next))

# def sumofLL(head):
#     if not head:
#         return 0
#     elif not head.next:
#         return head.value
#     else:
#         return head.value - int(head.next.value or 0) + sumofLL(head.next.next)

Node = ListNode(8,ListNode(6,ListNode(9)))
# print(solution(Node))

# print(sumofLL(Node))


def arrayify(head) -> [int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array

def
print(arrayify(Node))