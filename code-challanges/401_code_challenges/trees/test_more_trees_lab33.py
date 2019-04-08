from trees.tree import BinarySearchTree
import pytest

def test_class():
    assert BinarySearchTree

def test_traverse_in_order():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = list(tree.traverse_in_order())
  
    assert items == ['apples','bananas','cucumbers']

def test_traverse_for_loop_in_order():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = []

    for item in tree.traverse_in_order():
        items.append(item)

    assert items == ['apples','bananas','cucumbers']


def test_traverse_pre_order():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = list(tree.traverse_pre_order())
  
    assert items == ['bananas','apples','cucumbers']

def test_traverse_for_loop_pre_order():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = []

    for item in tree.traverse_pre_order():
        items.append(item)

    assert items == ['bananas','apples','cucumbers']


def test_traverse_post_order():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = list(tree.traverse_post_order())
  
    assert items == ['apples','cucumbers','bananas']

def test_traverse_for_loop_post_order():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = []

    for item in tree.traverse_post_order():
        items.append(item)

    assert items == ['apples','cucumbers','bananas']

def test_traverse_breath_first():
    tree = BinarySearchTree()
    tree.add('apples')
    tree.add('cucumbers')
    tree.add('bananas')

    items = list(tree.traverse_breath_first())
  
    assert items == ['apples','cucumbers','bananas']

def test_traverse_for_loop_post_order():
    tree = BinarySearchTree()
    tree.add('apples')
    tree.add('cucumbers')
    tree.add('bananas')

    items = []

    for item in tree.traverse_breath_first():
        items.append(item)

    assert items == ['apples','cucumbers','bananas']

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
   
    items = []

    for item in fruits.traverse_breath_first():
        items.append(item)
    assert expected == items
