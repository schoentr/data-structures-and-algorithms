from trees.tree import BinarySearchTree, BinaryTree
from tree_intersection.tree_intersection import tree_intersection

def test_one():
    tree1=BinarySearchTree()
    tree2=BinarySearchTree()
    tree1.add(10)
    tree1.add(14)
    tree1.add(16)
    tree1.add(12)
    tree1.add(9)
    tree1.add(23)
    tree1.add(13)
    tree2.add(10)
    tree2.add(14)
    tree2.add(16)
    tree2.add(12)
    tree2.add(9)
    tree2.add(23)
    tree2.add(13)
    actual = tree_intersection(tree1,tree2)
    expected = [10, 9, 12, 13, 14, 16, 23]
    assert expected == actual
    assert (24 in expected) == False


def test_two():
    tree1=BinarySearchTree()
    tree2=BinarySearchTree()
    tree1.add('tim')
    tree1.add('tom')
    tree1.add('chris')
    tree1.add('jack')
    tree1.add('joe')
    tree1.add('pat')
    tree2.add('pat')
    tree2.add('pam')
    tree2.add('wer')
    tree2.add('jan')
    tree2.add('tom')
    tree2.add('tyler')
    tree2.add('bill')
    actual = tree_intersection(tree1,tree2)
    expected =['pat', 'pam', 'tom']
    assert  expected== actual
    assert ('chris' in expected) ==False 
def test_three():
    tree1=BinarySearchTree()
    tree2=BinarySearchTree()
    tree1.add(10)
    tree1.add(14)
    tree1.add(16)
    tree1.add(12)
    tree1.add(9)
    tree1.add(23)
    tree1.add(13)
    tree2.add(0)
    tree2.add(1)
    tree2.add(2)
    tree2.add(3)
    tree2.add(4)
    tree2.add(5)
    tree2.add(6)
    actual = tree_intersection(tree1,tree2)
    assert []== actual
    assert len(actual) == 0
