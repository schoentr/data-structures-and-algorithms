from trees.tree  import BinarySearchTree, BinaryTree
from hashtable.hashtable import Hashtable


def tree_intersection(tree1,tree2):
    """ This function takes in two trees, and returns a list of values common between both trees     
    Arguments:
        {Tree}
        {Tree} 
    
    Returns:
        [List] -- [A list of all values that are the same in both trees]
    """

    rtn = []
    ht = Hashtable()
    tree_1_list = tree1.pre_order()
    tree_2_list = tree2.pre_order()
    for value in tree_1_list:
        ht.add(ht.hash(value),value)
    for value in tree_2_list:
        if ht.contains(ht.hash(value)):
            rtn.append(value)
    return rtn