class BinaryTree():
    def __init__(self):
        self.root = None

    def in_order(self, node = None):

        """
        This Method traverses across the tree in Order.
         LEFT -> RIGHT -> ROOT   
        """
        rtn = []
        if node is None:
            node=  self.root
        if node.child_left:
            rtn +=self.in_order(node.child_left)
        rtn.append(node.value)
        if node.child_right:
            rtn += self.in_order(node.child_right)
        return rtn

    def post_order(self, node = None):
        """
        This Method traverses across the tree post-order.
        
        """
        rtn = []
        if node is None:
            node= self.root
        if node.child_left:
            rtn += self.in_order(node.child_left)
        if node.child_right:
            rtn += self.in_order(node.child_right)
        rtn.append(node.value)
        return rtn

    def pre_order(self, node = None):
        """
        This Method traverses across the tree pre-order.
         Root -> Left -> Right
        """
        rtn = []
        if node is None:
            node=  self.root
        rtn.append(node.value)
        if node.child_left:
            rtn += self.in_order(node.child_left)
        if node.child_right:
            rtn += self.in_order(node.child_right)
        return rtn

class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None
    
    def add(self, value):
        """ 
        This take in a value and creates a Node with the value and passes to the add_node method]
        
        Arguments:
            value  -- [any data type]
        """

        node=Node(value)
        self._add_node(self.root, node)

    def _add_node(self, curr, node):
        """
        This is a private method used to add nodes to the tree
        
        Arguments:
            curr {node} -- [the current node being evaluated]
            node {node} -- [the node being added to the tree]
        """

        if not self.root:
            self.root = node
        if not curr:
            curr = self.root
        if curr.value > node.value:
            if curr.child_left is None:
                curr.child_left = node
            else:
                self._add_node(curr.child_left,node)
        if curr.value < node.value:
            if curr.child_right is None:
                curr.child_right = node
            else:
                self._add_node(curr.child_right,node)
    
    def contains(self,value, curr=None):
        """ 
        Arguments:
            value {} -- [any data type  which will be stored in the node]
        
        Keyword Arguments:
            curr {node} -- [the current node that is being evaluated]
        
        Returns:
            [Boolean] -- [True if value is in the tree, False if not in the tree]
        """

        if curr is None:
            curr = self.root
        if value is curr.value:
            return True
        if value > curr.value and curr.child_right :
                return self.contains(value, curr.child_right)
        elif curr.child_left:
                return self.contains(value, curr.child_left)
        return False
        
        



        
class Node():

    def __init__(self, value):
        """Creates all nodes for the tree
        
        Arguments:
            value  -- [Any value you want to be held in the node]
        """
        self.value = value
        self.child_left = None
        self.child_right = None
    
    def __repr__(self):
        return 'Node - '+ self.data
    
    def __str__(self):
        return 'Node - '+ self.data
