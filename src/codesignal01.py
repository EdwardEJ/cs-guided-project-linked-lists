# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
        
def insertValueIntoSortedLinkedList(l, value):

    current = l
    if current is None:
        current = ListNode(value)
        return current
    
    #Check for insertion at head
    if current.value > value:
        new_node = ListNode(value)
        new_node.next = current
        return new_node
    
    while current:
        #Check for inseration at tail
        if current.next is None:
            new_node = ListNode(value)
            new_node.next = None
            current.next = new_node
            return l
        # Check for insertion in middle
        if current.value < value and current.next.value > value:
            new_node = ListNode(value)
            new_node.next = current.next
            current.next = new_node
            return l
        else:
            current = current.next
    
    
print(chr(ord('z') + 1))