class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        try:
            return f"Node({self.value}) -> {self.next}"  # recursion!
        except RecursionError:
            return f"Can't do recursive print: List is too big"


class LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        if iterable:
            self.create_from_iterable(iterable)

    def create_from_iterable(self, iterable):
        iterator = iterable.__iter__()
        first_value = next(iterator)
        self.head = Node(first_value)
        current_node = self.head
        for value in iterator:
            current_node.next = Node(value)
            current_node = current_node.next

    def reverse(self):
        self.head = self.reverse_list(self.head)

    def get_tail(self):
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        return ptr

    def __add__(self, other):
        ptr = self.get_tail()
        ptr.next = other.head
        return self

    def __iter__(self):
        ptr = self.head
        yield ptr
        while ptr.next:
            ptr = ptr.next
            yield ptr

    def search(self, value):
        for node in self.__iter__():
            if node.value == value:
                return node

    def pop(self, value):
        node = self.search(value)


    @staticmethod
    def reverse_list(head):
        """Fantasic code!"""
        new_head = None  # ptr on previous item
        while head:
            head.next, head, new_head = new_head, head.next, head  # look Ma, no temp vars!
        return new_head

    def __repr__(self):
        return self.head.__repr__()


L1 = LinkedList(range(10))
print(L1)
L2 = LinkedList(range(10, 20))
print(L2)
print(L1 + L2)
for i in L1:
    print(type(i), i)
