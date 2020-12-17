"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.

Example:

The code below should first construct a linked list (x -> y -> z) and then delete `y` from the linked list by calling the function `delete_node`. It is your job to write the `delete_node` function.

```python
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)
```

*Note: We can do this in O(1) time and space! But be aware that our solution will have some side effects...*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def delete_node(node_to_delete):
    # Your code here
    if node_to_delete.next is None:
      #traverse to the node right before the tail so that we can change its next reference
      #this isnt possible because we dont have access to the head
      raise Exception('This function cant delete the tail')
    else:
      node_to_delete.value = node_to_delete.next.value
      node_to_delete.next = node_to_delete.next.next

def print_ll(head):
  #init a new variable to refer to the node we have access to
  current = head
  
  #use while loop to keep traversing until
  #`current` variable falls off the tail of the linked list
  while current is not None:  #can be written as `while current:` for less verbose syntax
    print(current.value)
    #update our `current` variable to refer to the next node in the linked list
    current = current.next


x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(z)
print_ll(x)
