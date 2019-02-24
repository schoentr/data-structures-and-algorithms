from linked_list import LinkedList

# """
# Can properly insert into the linked list
# The head property will properly point to the first node in the linked list
# Can properly insert multiple nodes into the linked list
# Will return true when finding a value within the linked list that exists
# Will return false when searching for a value in the linked list that does not exist
# Can properly return a collection of all the values that exist in the linked list"""
# def test_exists():
#    assert linked_list

def test_exists():
   assert LinkedList

def test_instantion():
   """Can successfully instantiate an empty linked list
   """
   assert LinkedList()

def test_insert_one():
   """

   """
   fruits = LinkedList()
   fruits.insert('apples')
   expected = 'apples'
   actual = fruits.head.value
   assert expected == actual

def test_insert_two():
   """

   """
   fruits = LinkedList()
   fruits.insert('apples')
   

   expected = 'apples'
   actual = fruits.head.value
   assert expected == actual
   fruits.insert('bananas')
   expected = 'bananas'
   actual = fruits.head._next.value
   assert expected == actual

def test_includes():
   fruits = LinkedList()
   fruits.insert('apples')
   fruits.insert('bananas')
   assert fruits.includes('bananas')

def test_print():
   fruits = LinkedList()
   fruits.insert('apples')
   fruits.insert('bananas')

   assert fruits.print() == 'apples, bananas, '