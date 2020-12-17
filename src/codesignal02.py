# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    ListOne = l1
    ListTwo = l2
    newList = ListNode('x')
    tail = newList
    
    while ListOne and ListTwo:
        # temp_node = None
        
        if ListOne.value >= ListTwo.value:
            tail.next = ListTwo
            ListTwo = ListTwo.next
            # temp_node = ListTwo.next
            # tail.next = ListTwo
            # tail = ListTwo
            # ListTwo = temp_node
        elif ListOne.value <= ListTwo.value:
            tail.next = ListOne
            ListOne = ListOne.next
            # temp_node = ListOne.next
            # tail.next = ListOne
            # tail = ListOne
            # ListOne = temp_node
        tail = tail.next
    if ListOne is None:
        tail.next = ListTwo
    else:
        tail.next = ListOne
    return newList.next

l1: [1, 2, 3]
l2: [4, 5, 6]

l1: [1]
l2: [-1000000000, 1000000000]

l1: [-1, -1, 0, 1]
l2: [-1, 0, 0, 1, 1]