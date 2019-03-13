
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
