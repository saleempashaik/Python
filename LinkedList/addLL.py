class Node:
    def __init__(self, data, nextV = None):
        self.data = data
        self.next = nextV

def sum_list_recursive(head):
    if head is None:
        return 0  # Base case: empty list
    elif head.next is None:
        return head.data
    else:
        return head.data + sum_list_recursive(head.next)

# Create a linked list
head = Node(1,Node(2,Node(3)))
# head.next = Node(2)
# head.next.next = Node(3)

# Calculate the sum of the linked list using the recursive function
result = sum_list_recursive(head)

print("Sum of the linked list:", result)