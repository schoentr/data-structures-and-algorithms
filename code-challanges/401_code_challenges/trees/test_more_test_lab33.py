from trees.tree import BinarySearchTree
import pytest

def test_class():
    assert BinarySearchTree

def test_traverse():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = list(tree.traverse_in_order())
  
    assert items == ['apples','bananas','cucumbers']

def test_traverse_for_loop():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = []

    for item in tree.traverse_in_order():
        items.append(item)

    assert items == ['apples','bananas','cucumbers']

