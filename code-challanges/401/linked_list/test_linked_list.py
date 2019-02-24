om linked_list import LinkedList

"""
Can properly insert into the linked list
The head property will properly point to the first node in the linked list
Can properly insert multiple nodes into the linked list
Will return true when finding a value within the linked list that exists
Will return false when searching for a value in the linked list that does not exist
Can properly return a collection of all the values that exist in the linked list"""

def test_exists():
   assert linked_list

def test_instantion():
   """Can successfully instantiate an empty linked list
   """
   assert LinkedList()

def test_insert_one():
   """

   """
   fruit = LinkedList()
   fruits.insert('apples')
   expected = 'apples'
   actual = fruits.head.value
   assert expected == actual

def test_insert_two():
   """

   """
   fruit = LinkedList()
   fruits.insert('apples')
   fruits.insert('bananas')

   expected = 'apples'
   actual = fruits.head.value
   assert expected == actual

   expected = 'bananas'
   actual = fruits.head.value
   assert expected == actual

def test_includes():

   assert fruits.test_includes('bananas')

def test_print():
   assert fruits.print() == 'apples, bananans, '