
from trees.tree import BinarySearchTree

def test_exists():
   assert BinarySearchTree


def test_instantion():
   """Can successfully instantiate an empty linked list
   """
   assert BinarySearchTree()


def test_add_one():

   fruits = BinarySearchTree()
   fruits.add('apples')
   expected = 'apples'
   actual = fruits.root.value
   assert expected == actual

def test_add_two_one_right():

   fruits = BinarySearchTree()
   fruits.add('apples')
   fruits.add('bananas')
   expected = 'bananas'
   actual = fruits.root.child_right.value
   assert expected == actual

def test_add_one_left_one_right():
   fruits = BinarySearchTree()
   fruits.add('bananas')
   fruits.add('apples')
   fruits.add('carrots')
   expected = 'bananas'
   actual = fruits.root.value
   assert expected == actual
   expected = 'apples'
   actual = fruits.root.child_left.value
   assert expected == actual
   expected = 'carrots'
   actual = fruits.root.child_right.value
   assert expected == actual

def test_cotains_true():
   fruits = BinarySearchTree()
   fruits.add('bananas')
   fruits.add('apples')
   fruits.add('carrots')
   fruits.add('mango')
   fruits.add('pear')
   fruits.add('cake')
   fruits.add('cookies')
   fruits.add('beer')
   fruits.add('whiskey')
   expected = True
   actual = fruits.contains('whiskey')
   assert expected == actual

def test_in_order():
   fruits = BinarySearchTree()
   fruits.add('bananas')
   fruits.add('apples')
   fruits.add('carrots')
   fruits.add('mango')
   fruits.add('pear')
   fruits.add('cake')
   fruits.add('cookies')
   fruits.add('beer')
   fruits.add('whiskey')
   expected = ['apples', 'bananas', 'beer', 'cake', 'carrots', 'cookies', 'mango', 'pear', 'whiskey']
   actual = fruits.in_order()
   assert expected == actual
  
  

def test_pre_order():
   fruits = BinarySearchTree()
   fruits.add('bananas')
   fruits.add('apples')
   fruits.add('carrots')
   fruits.add('mango')
   fruits.add('pear')
   fruits.add('cake')
   fruits.add('cookies')
   fruits.add('beer')
   fruits.add('whiskey')
   expected = ['bananas', 'apples', 'beer', 'cake', 'carrots', 'cookies', 'mango', 'pear', 'whiskey']
   actual = fruits.pre_order()
   assert expected == actual
  

def test_post_order():
   fruits = BinarySearchTree()
   fruits.add('bananas')
   fruits.add('apples')
   fruits.add('carrots')
   fruits.add('mango')
   fruits.add('pear')
   fruits.add('cake')
   fruits.add('cookies')
   fruits.add('beer')
   fruits.add('whiskey')
   expected = ['apples', 'beer', 'cake', 'carrots', 'cookies', 'mango', 'pear', 'whiskey', 'bananas']
   actual = fruits.post_order()
   assert expected == actual
  
def test_breadth_one():
   fruits = BinarySearchTree()
   fruits.add('bananas')
   fruits.add('apples')
   fruits.add('carrots')
   fruits.add('mango')
   fruits.add('pear')
   fruits.add('cake')
   fruits.add('cookies')
   fruits.add('beer')
   fruits.add('whiskey')
   expected = ['bananas', 'apples', 'carrots', 'cake', 'mango', 'beer', 'cookies', 'pear', 'whiskey']
   actual = fruits.breath_first()
   assert expected == actual

def test_breadth_two():
   fruits = BinarySearchTree()
   fruits.add(67)
   fruits.add(62)
   fruits.add(65)
   fruits.add(90)
   expected = [67,62,90,65]
   actual = fruits.breath_first()
   assert expected == actual

def test_height_one():
   numbers = BinarySearchTree()
   numbers.add(10)
   numbers.add(9)
   numbers.add(8)
   numbers.add(7)
   numbers.add(3)
   numbers.add(35)
   numbers.add(12)
   numbers.add(43)
   actual = numbers.find_height()
   assert  5    == actual

def test_height_two():
   numbers = BinarySearchTree()
   numbers.add(50)
   numbers.add(100)
   numbers.add(200)
   numbers.add(150)
   # numbers.add(5)
   # numbers.add(35)
   # numbers.add(13)
   # numbers.add(43)
   # numbers.add(4)
   # numbers.add(159)
   # numbers.add(33)
   # numbers.add(322)
   # numbers.add(543)
   # numbers.add(352)
   # numbers.add(123)
   # numbers.add(443)
   actual = numbers.find_height()
   assert  3 == actual

def test_height_three():
   numbers  =  BinarySearchTree()
   numbers.add(10)
   
   numbers.add(9)
   numbers.add(11)
   actual = numbers.find_height()
   assert 1 == actual
   
def test_height_four():
   numbers  =  BinarySearchTree()
   numbers.add(10)
   numbers.add(9)
   numbers.add(11)
   numbers.add(13)
   actual = numbers.find_height()
   assert 2 == actual
