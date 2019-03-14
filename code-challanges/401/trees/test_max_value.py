from trees.tree import BinarySearchTree


def test_max_one():
   nums = BinarySearchTree()
   nums.add(67)
   nums.add(62)
   nums.add(65)
   nums.add(90)
   expected = 90
   actual =nums.find_max_value()
   assert expected == actual
