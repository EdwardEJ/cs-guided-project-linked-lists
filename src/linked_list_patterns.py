class LinkedListNode:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None


x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

y.prev = x
z.prev = y

def print_ll_reverse(tail):
  current = tail

  while current:
    print(current.value)
    current = current.prev

#traverse through a linked list and print value of each node
def print_ll(head):
  #init a new variable to refer to the node we have access to
  current = head
  
  #use while loop to keep traversing until
  #`current` variable falls off the tail of the linked list
  while current is not None:  #can be written as `while current:` for less verbose syntax
    print(current.value)
    #update our `current` variable to refer to the next node in the linked list
    current = current.next

print(print_ll(x))
print(print_ll_reverse(z))

