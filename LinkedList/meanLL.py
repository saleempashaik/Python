
class ListNode(object):
  def __init__(self, x, next_node=None):
    self.value = x
    self.next = next_node

def recurPrint(n,pointer = 0):
    if pointer < n:
        print(pointer)
        return recurPrint(n,pointer+1)

def meanLL(node, sum = 0, len = 0) -> int:
    if not node:
        return
    else:
        sum += node.value
        len += 1
        print(node.value)
        print(sum,len)
        return meanLL(node.next,sum,len )

    return sum//length

Node = ListNode(8,ListNode(6,ListNode(9)))

print(meanLL(Node))