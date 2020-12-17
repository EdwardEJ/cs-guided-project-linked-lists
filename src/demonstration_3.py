class Node:
  def __init__(self, value=None, next=None):
    self.value = value
    self.next = next
  def __str__(self):
    return f'{self.value}'

def find_length(head):
  count = 0
  current = head
  while current:
    count += 1
    current = current.next
  return count

def find_middle(head):
  # single pass answer
  # `two runner` approach
  slow = head
  fast = head

  #loop so long as fast is not None or fast's next is not None
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
  
  #at this point, fast has reached the end of the linked list
  return slow.value

  # len = find_length(head)
  # midpoint = len // 2
  # current = head
  # while midpoint != 0:
  #   current = current.next
  #   midpoint -= 1
  # return current

  
root = Node(3)
root.next = Node(4)
root.next.next = Node(5)
root.next.next.next = Node(6)
root.next.next.next.next = Node(7)

print(find_middle(root))