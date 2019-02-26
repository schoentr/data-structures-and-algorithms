from linked_list import LinkedList

# """
# 
# Can properly insert multiple nodes into the linked list
# """
# def test_exists():
def test_exists():
   assert LinkedList


def test_instantion():
   """Can successfully instantiate an empty linked list
   """
   assert LinkedList()


def test_insert_one():
   """Can properly insert into the linked list
    The head property will properly point to the first node in the linked list

   """
   fruits = LinkedList()
   fruits.insert('apples')
   expected = 'apples'
   actual = fruits.head.value
   assert expected == actual


def test_insert_two():
   """Can Properly insert mutilple nodes into the linked list
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
   """Will return true when finding a value within the linked list that exists
    Will return false when searching for a value in the linked list that does not exist 
   """
   fruits = LinkedList()
   fruits.insert('apples')
   fruits.insert('bananas')
   assert fruits.includes('bananas')


def test_print():
   """
# Can properly return a collection of all the values that exist in the linked list
   """
   fruits = LinkedList()
   fruits.insert('apples')
   fruits.insert('bananas')
   assert fruits.print() == 'apples, bananas, '

def test_find_from_end_first():
   fruits = LinkedList()
   fruits.insert('apples')
   fruits.insert('bananas')
   fruits.insert('pears')
   fruits.insert('grapes')
   actual = fruits.find_from_end(2)
   assert 'bananas' == actual
def test_find_from_end_second():
   fruits = LinkedList()
   fruits.insert('apples')
   fruits.insert('bananas')
   fruits.insert('pears')
   fruits.insert('grapes')
   actual = fruits.find_from_end(1)
   assert 'pears' == actual
def test_find_from_end_exception():
   fruits = LinkedList()
   fruits.insert('apples')
   fruits.insert('bananas')
   fruits.insert('pears')
   fruits.insert('grapes')
   actual = fruits.find_from_end(5)
   assert 'exception' == actual
   