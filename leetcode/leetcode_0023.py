class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        return f"{self.val} -> {self.next}"


def mergeLists(lists: List[ListNode]) -> ListNode:
    processed_lists = set()
    head = None
    ptr = None
    while True:
        # нахождение наименьшего
        node_value, index = None, None
        for ix, node in enumerate(lists):
            if (node is not None) and (node_value is None or node.val < node_value):
                node_value, index = node.val, ix
        
        if node_value is None:
            break
        
        # добавление в список
        if not head:
            head = ListNode(node_value)
            ptr = head
        else:
            ptr.next = ListNode(node_value)
            ptr = ptr.next
        
        # перемотка
        lists[index] = lists[index].next
    
    return head
