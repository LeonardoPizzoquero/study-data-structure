"""
  BIG O COMPLEXITY:
    show_list: O(n)
    append: O(1)
    pop: O(n)
    prepend: O(1)
    pop_first: O(1)
    get_by_index: O(n)
    get_by_value: O(n)
    set: O(n)
    insert: O(n)
    remove: O(n)
    reverse: O(n)
"""

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
class LinkedList():
  """
  A class representing a linked list data structure.
  
  Attributes:
    head (Node): The first node of the linked list.
    tail (Node): The last node of the linked list.
    length (int): The number of nodes in the linked list.
  """
  
  def __init__(self, value):
    """
    Initializes a new instance of the LinkedList class.
    
    Args:
      value: The value to be stored in the first node of the linked list.
    """
    new_node = Node(value)
    self.tail = new_node
    self.head = new_node
    self.length = 1
    
  def show_list(self):
    """
    Prints the values of all nodes in the linked list.
    """
    temp = self.head
    
    while temp is not None:
      print(temp.value)
      temp = temp.next
    
  def append(self, value):
    """
    Appends a new node with the given value to the end of the linked list.
    
    Args:
      value: The value to be stored in the new node.
      
    Returns:
      True if the operation is successful, False otherwise.
    """
    new_node = Node(value)
    
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    
    self.length += 1
    
    return True
  
  def pop(self):
    """
    Removes and returns the last node from the linked list.
    
    Returns:
      The removed node if the linked list is not empty, None otherwise.
    """
    if self.length == 0:
      return None
    
    temp = self.head
    pre = self.head
    
    while (temp.next):
      pre = temp
      temp = temp.next
    
    self.tail = pre
    self.tail.next = None
    self.length -= 1
    
    if self.length == 0:
      self.head = None
      self.tail = None
      
    return temp
  
  def prepend(self, value):
    """
    Prepends a new node with the given value to the beginning of the linked list.
    
    Args:
      value: The value to be stored in the new node.
      
    Returns:
      True if the operation is successful, False otherwise.
    """
    new_node = Node(value)
    
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
      
    self.length += 1
    
    return True
  
  def pop_first(self):
    """
    Removes and returns the first node from the linked list.
    
    Returns:
      The removed node if the linked list is not empty, None otherwise.
    """
    if self.length == 0:
      return None
  
    temp = self.head
    self.head = self.head.next
    temp.next = None
    
    self.length -= 1
    
    if self.length == 0:
      self.tail = None
    
    return temp
    
  def get_by_index(self, index):
    """
    Returns the node at the specified index in the linked list.
    
    Args:
      index (int): The index of the node to be retrieved.
      
    Returns:
      The node at the specified index if it exists, None otherwise.
    """
    if index < 0 or index >= self.length:
      return None 

    if index == 0:
      return self.head
    
    if index == self.length - 1:
      return self.tail

    temp = self.head
    
    for _ in range(index):
      temp = temp.next
      
    return temp
  
  def get_by_value(self, value):
    """
    Returns the first node with the specified value in the linked list.
    
    Args:
      value: The value to search for.
      
    Returns:
      The first node with the specified value if it exists, None otherwise.
    """
    if self.length == 0:
      return None 

    temp = self.head
    
    while temp is not None:
      if temp.value == value:
        return temp
      
      temp = temp.next
      
    return temp
  
  def set(self, index, value):
    """
    Sets the value of the node at the specified index in the linked list.
    
    Args:
      index (int): The index of the node to be updated.
      value: The new value to be stored in the node.
      
    Returns:
      True if the operation is successful, False otherwise.
    """
    temp = self.get_by_index(index)
    
    if temp:
      temp.value = value
      return True
    
    return False
  
  def insert(self, index, value):
    """
    Inserts a new node with the given value at the specified index in the linked list.
    
    Args:
      index (int): The index at which the new node should be inserted.
      value: The value to be stored in the new node.
      
    Returns:
      True if the operation is successful, False otherwise.
    """
    if index < 0 or index > self.length:
      return False
    
    if index == 0:
      return self.prepend(value)
    
    if index == self.length:
      return self.append(value)
    
    new_node = Node(value)
    temp = self.get_by_index(index - 1)
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    
    return True
  
  def remove(self, index):
    """
    Removes and returns the node at the specified index in the linked list.
    
    Args:
      index (int): The index of the node to be removed.
      
    Returns:
      The removed node if it exists, None otherwise.
    """
    if index < 0 or index >= self.length:
      return None
    
    if index == 0:
      return self.pop_first()
    
    if index == self.length - 1:
      return self.pop()
    
    temp = self.get_by_index(index - 1)
    removed = temp.next
    temp.next = removed.next
    removed.next = None
    self.length -= 1
    
    return removed
  
  def reverse(self):
    """
    Reverses the order of nodes in the linked list.
    
    Returns:
      None if the linked list is empty, otherwise the reversed linked list.
    """
    if self.length == 0:
      return None
    
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = temp.next
    before = None
    
    for _ in range(self.length):
      after = temp.next
      temp.next = before
      before = temp
      temp = after
    
ll = LinkedList(1)