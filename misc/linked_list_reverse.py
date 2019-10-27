class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        try:
            return f"Node({self.value}) -> {self.next}"  # recursion!
        except RecursionError:
            return f"Can't do recursive print: List is too big"


def reverse_list(head):
    """Fantasic code!"""
    new_head = None  # ptr on previous item
    while head:
        head.next, head, new_head = new_head, head.next, head  # look Ma, no temp vars!
    return new_head


def reverse_list2(head):
    """Not so fantastic code"""
    new_head = None  # this is where we build the reversed list (reusing the existing nodes)
    while head:
        temp = head  # temp is a reference to a node we're moving from one list to the other
        head = temp.next  # the first two assignments pop the node off the front of the list
        temp.next = new_head  # the next two make it the new head of the reversed list
        new_head = temp
    return new_head


def ll_from_list(source_list):
    head = Node(source_list[0])
    current_node = head
    for item in source_list[1:]:
        current_node.next = Node(item)
        current_node = current_node.next
    return head


L = Node(5, Node(6, Node(7, Node(8))))
L = Node(5)
L = ll_from_list(range(300))

print(L)
print(reverse_list(L))

