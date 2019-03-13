from trees.tree import  BinaryTree, BinarySearchTree

# from fizzbuzz import  fizzbuzz

def test_fizzbuzz_one():
   numbers = BinarySearchTree()
   numbers.add(1)
   numbers.add(3)
   numbers.add(28)
   numbers.add(90)
   numbers.add(10)
   numbers.add(18)
   numbers.add(21)
   numbers.add(65)
   numbers.add(100)
   expected = [1,'fizz','buzz','fizz','fizz',28,'buzz','fizzbuzz','buzz']
   numbers.fizzbuzz()
   actual = numbers.fizzbuzz()
   assert expected == actual
